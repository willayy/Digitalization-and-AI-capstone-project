import PIL
import requests
import torch
from io import BytesIO
from diffusers import StableDiffusionInstructPix2PixPipeline

def download_image(url):
    response = requests.get(url)
    return PIL.Image.open(BytesIO(response.content)).convert("RGB")

img_url = "https://huggingface.co/datasets/diffusers/diffusers-images-docs/resolve/main/mountain.png"

image = download_image(img_url).resize((512, 512))

pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(
    "timbrooks/instruct-pix2pix", #torch_dtype=torch.float16
)

pipe = pipe.to("cpu")

prompt = "make the mountains snowy"

image = pipe(prompt=prompt, image=image).images[0]

image.show()