 
import torch
import sys
import io
import requests
from PIL.Image import Image
from diffusers.utils import load_image, make_image_grid
from requests import Response
from diffusers import AutoPipelineForImage2Image
from diffusers import DiffusionPipeline

#----------------------------------------------------------- CUDA Model -----------------------------------------------------------#

def run_cuda_model(prompt: str, image: Image) -> Image:

    # Load a pretrained model
    pipeline = AutoPipelineForImage2Image.from_pretrained(
        "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16, use_safetensors=True
    )

    pipeline.enable_model_cpu_offload()

    init_image = load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/cat.png")

    prompt = "cat wizard, gandalf, lord of the rings, detailed, fantasy, cute, adorable, Pixar, Disney, 8k"

    image = pipeline(prompt, image=init_image).images[0]

    return image

#----------------------------------------------------------- MPS Model --------------------------------------------------------------#

def run_mps_model(prompt):

    # Set the MPS high watermark to 0.0 to avoid out-of-memory errors
    PYTORCH_MPS_HIGH_WATERMARK_RATIO=0.0

    pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")

    pipe = pipe.to("mps")

    # Recommended if your computer has < 64 GB of RAM
    pipe.enable_attention_slicing()

    prompt = "a photo of an astronaut riding a horse on mars"

    image = pipe(prompt).images[0]

    return image

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

prompt = "cat wizard, gandalf, lord of the rings, detailed, fantasy, cute, adorable, Pixar, Disney, 8k"
image = load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/cat.png")

return_image: Image = None

# Check if cuda is available
if torch.cuda.is_available():

    print("CUDA is available, running CUDA model.")

    return_image = run_cuda_model(prompt, image)

elif sys.platform == "darwin":

    print("MPS is available, running MPS model.")

    return_image = run_mps_model(prompt)

else:
    
    print("CUDA and MPS are unavailable, running fake model.")
    
    return_image = run_fake_model(prompt)


image.show()