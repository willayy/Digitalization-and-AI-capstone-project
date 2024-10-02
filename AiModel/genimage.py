import torch
import os
from PIL.Image import Image as Img
from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image

STANDARD_NEGATIVE_PROMPT = """
    more than 4 legs,
    less than 4 legs
"""

def generate_image(
        prompt: str,
        image: Img, 
        show_image: bool, 
        save_image_path: str = "", 
        strength: float = 0.8, 
        num_inf: int = 50, 
        guidance: float = 7.5, 
        neg_prompt= STANDARD_NEGATIVE_PROMPT
    ) -> None:

    MODEL_PATH: str = "./local_models/stable-diffusion-v1-5"
    DEVICE: str = ""
    CUDA = torch.cuda.is_available()
    MPS = torch.backends.mps.is_available()

    # Check if cuda is available
    if CUDA:

        print("CUDA is available")

        DEVICE = "cuda"
        
    # Check if MPS is available
    elif MPS:
            
        print("MPS is available")

        DEVICE = "mps"

        # Let MPS use all available memory, may cause system failure
        os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"

    # If neither CUDA or MPS is available, run on CPU
    else:

        print("CUDA and MPS is unavailable, running CPU model.")

        num_threads = os.cpu_count()

        torch.set_num_threads(num_threads)  # Adjust based on your CPU

        DEVICE = "cpu"

    # Run the model using a diffusers pipeline
    pipe: StableDiffusionImg2ImgPipeline = StableDiffusionImg2ImgPipeline.from_pretrained(
        MODEL_PATH if os.path.exists(MODEL_PATH) else "runwayml/stable-diffusion-v1-5",
        torch_dtype = torch.float32 
    )

    # Disable this subdue warning
    pipe.tokenizer.clean_up_tokenization_spaces = False

    # Save the model locally if it doesn't exist
    if not os.path.exists(MODEL_PATH): pipe.save_pretrained(MODEL_PATH)

    # Set the device for the model
    # The diffuser docs say that i should use this AFTER enabling the sequential cpu offload
    # But this throws an exception, so i'm doing it before which works fine.
    # Im already seeing a substantial memory reduction with the whole setup so it's fine for now.
    pipe.to(DEVICE)

    # If using GPU or MPS, enable sequential CPU offload to reduce memory usage
    if CUDA or MPS: 
        pipe.enable_sequential_cpu_offload(device=DEVICE)
        
    # Memory saving measures
    pipe.enable_vae_tiling()
    pipe.enable_attention_slicing()

    # Prepare image, no clue if resizing and converting to RGB is necessary but it's in the example code on the diffuser docs
    init_image = image.convert("RGB")
    init_image = init_image.resize((768, 512))

    # Generate image
    generated_image = pipe(prompt=prompt, image=image, strength=strength, num_inference_steps=num_inf, guidance_scale=guidance, negative_prompt=neg_prompt).images[0]

    print("model has finished running.")

    # Display the image
    if show_image:
        generated_image.show()
        print("image shown.")

    # Save the image
    if save_image_path != "":
        generated_image.save(save_image_path)
        print("image saved.")

    return generated_image

generate_image("Fill in background with a Cozy, Modern, European, Living Room", Image.open("AiModel/Trials/table.jpg"), "true")
