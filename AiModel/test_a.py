import PIL
import requests
import torch
from io import BytesIO
from diffusers import StableDiffusionInstructPix2PixPipeline

def download_image(url):
    response = requests.get(url)
    return PIL.Image.open(BytesIO(response.content)).convert("RGB")

img_url = "https://huggingface.co/datasets/diffusers/diffusers-images-docs/resolve/main/mountain.png"



image.show()