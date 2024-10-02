import torch
import os
from PIL.Image import Image as Img
from diffusers import StableDiffusionImg2ImgPipeline

def generate_image(prompt: str, image: Img, show_image: str, save_image_path: str, strength: float = 0.8, num_inf: int = 50, guidance: float = 7.5, neg_prompt="more than a single furniture") -> None:

    model_path = "./AiModel/local_models/stable-diffusion-v1-5"

    device: str = ""

    CUDA = torch.cuda.is_available()
    MPS = torch.backends.mps.is_available()

    # Check if cuda is available
    if CUDA:

        print("CUDA is available")

        device = "cuda"
        
    elif MPS:
            
        print("MPS is available")

        device = "mps"

    else:

        print("CUDA is unavailable, running CPU model.")

        num_threads = os.cpu_count()

        torch.set_num_threads(num_threads)  # Adjust based on your CPU

        device = "cpu"

    # Run the model
    pipe: StableDiffusionImg2ImgPipeline = StableDiffusionImg2ImgPipeline.from_pretrained(
        model_path if os.path.exists(model_path) else "runwayml/stable-diffusion-v1-5"
    )

    pipe.to(device)

    if CUDA:

        pipe.enable_sequential_cpu_offload()

    if MPS:

        pipe.enable_sequential_cpu_offload(device="mps")


    if not os.path.exists(model_path):

        pipe.save_pretrained(model_path)

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


