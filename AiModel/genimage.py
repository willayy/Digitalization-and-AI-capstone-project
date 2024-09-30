 
import torch
import sys
import io
import requests
from PIL.Image import Image as Img
from diffusers.utils import load_image
from requests import Response
from diffusers import AutoPipelineForImage2Image
from diffusers import DiffusionPipeline
from PIL import Image

#----------------------------------------------------------- CUDA Model -----------------------------------------------------------#

def run_cuda_model(prompt: str, image: Img) -> Image:

    # Load a pretrained model
    pipeline: DiffusionPipeline = AutoPipelineForImage2Image.from_pretrained(
        "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16, use_safetensors=True
    )

    print(type(pipeline))

    pipeline.enable_model_cpu_offload()

    init_image = image

    ret_image = pipeline(prompt, image=init_image).images[0]

    return ret_image

#----------------------------------------------------------- Fake Model -----------------------------------------------------------#

# This model cant take images an input only a text prompt,
# this is just a prototype to show how off how Python can be used to interact with API's
# connected to a powerful model. This however would require more capital to run.

# The api endpoint address
API_URL: str = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"

# The API key to access the model
API_KEY: str = "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"

# Header for the JSON payload.
HEADER: dict = { "Authorization" : f"Bearer {API_KEY}" }

def run_fake_model(prompt: str) -> Image:

    response: Response = requests.post(API_URL, headers = HEADER, json={"inputs": prompt})

    content: bytes = response.content

    # Turn query result into image
    image = Image.open(io.BytesIO(content))

    return image

#----------------------------------------------------------- Main Function -----------------------------------------------------------#

def generate_image(prompt: str, image: Img, show_image: str, save_image_path: str) -> None:

    # The output image
    return_image: Img = None

    # Check if cuda is available
    if torch.cuda.is_available():

        print("CUDA is available, running CUDA model.")

        # Run the CUDA model
        return_image = run_cuda_model(prompt, image)
        
    else:

        print("CUDA is unavailable, running fake model.")

        # Run the fake model
        return_image = run_fake_model(prompt)

    print("model has finished running.")

    # Display the image
    if show_image == "true":
        return_image.show()
        print("image shown.")

    # Save the image
    if save_image_path != "":
        return_image.save(save_image_path)
        print("image saved.")

    print("terminating program.")

#----------------------------------------------------------- Script style --------------------------------------------------------------#

args = sys.argv

# Sanitize arguments
if args[1] == "help":
    print("Usage: python3 genimage.py <prompt> <image_path> <show_image> (optionally)-> <save_image_path>")
    sys.exit(0)

if args[3] != "true" and args[2] != "false":
    print("Invalid argument for show_image.")
    sys.exit(1)

prompt = args[1]

image_path = args[2]

show_image = args[3]

if len(args) == 5:
    save_image_path = args[4]
else:
    save_image_path = ""

if image_path != "":
    try:
        # Make PIL image from file
        image = load_image(image_path)
    except Exception as e:
        print(f"Error loading image, message: {e}")
        sys.exit(1)

generate_image(prompt, image, show_image, save_image_path)

sys.exit(0)