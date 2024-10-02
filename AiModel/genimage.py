import torch
import os
from PIL.Image import Image as Img
from diffusers import StableDiffusionImg2ImgPipeline

def generate_image(prompt: str, image: Img, show_image: str, save_image_path: str, strength: float = 0.8, num_inf: int = 50, guidance: float = 7.5, neg_prompt="chandeliers, zoomed out, tables that doesnt have four legs") -> None:

    MODEL_PATH: str = "./local_models/stable-diffusion-v1-5"
    DEVICE: str = ""
    CUDA = torch.cuda.is_available()
    MPS = torch.backends.mps.is_available()

    # Check if cuda is available
    if CUDA:

        print("CUDA is available")

        DEVICE = "cuda"
        
    elif MPS:
            
        print("MPS is available")

        DEVICE = "mps"

    else:

        print("CUDA is unavailable, running CPU model.")

        num_threads = os.cpu_count()

        torch.set_num_threads(num_threads)  # Adjust based on your CPU

        DEVICE = "cpu"

    # Run the model
    pipe: StableDiffusionImg2ImgPipeline = StableDiffusionImg2ImgPipeline.from_pretrained(
        MODEL_PATH if os.path.exists(MODEL_PATH) else "runwayml/stable-diffusion-v1-5"
    )

    pipe.tokenizer.clean_up_tokenization_spaces = False

    pipe.to(DEVICE)

    if not os.path.exists(MODEL_PATH): pipe.save_pretrained(MODEL_PATH)

    if CUDA or MPS: pipe.enable_sequential_cpu_offload(device=DEVICE)

    generated_image = pipe(prompt=prompt, image=image, strength=strength, num_inference_steps=num_inf, guidance_scale=guidance, negative_prompt=neg_prompt).images[0]

    print("model has finished running.")

    # Display the image
    if show_image == "true":
        generated_image.show()
        print("image shown.")

    # Save the image
    if save_image_path != "":
        generated_image.save(save_image_path)
        print("image saved.")

    return generated_image


