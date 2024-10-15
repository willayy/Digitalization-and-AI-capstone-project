import torch, os
from diffusers import AutoPipelineForInpainting
from diffusers.utils import load_image, make_image_grid

DEVICE = "mps"

MODEL_PATH: str = "./local_models/kandinsky-2-2-decoder-inpaint"

os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"

pipeline = AutoPipelineForInpainting.from_pretrained(
    MODEL_PATH if os.path.exists(MODEL_PATH) else "kandinsky-community/kandinsky-2-2-decoder-inpaint",
    torch_dtype=torch.float32
)

if not os.path.exists(MODEL_PATH): pipeline.save_pretrained(MODEL_PATH)

pipeline.to(DEVICE)

pipeline.enable_sequential_cpu_offload(device=DEVICE)

# Memory saving measures
pipeline.enable_vae_tiling()
pipeline.enable_attention_slicing()

init_image = load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/inpaint.png")
mask_image = load_image("https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/diffusers/inpaint_mask.png")

prompt = "a black cat with glowing eyes, cute, adorable, disney, pixar, highly detailed, 8k"

negative_prompt = "bad anatomy, deformed, ugly, disfigured"

image = pipeline(prompt=prompt, negative_prompt=negative_prompt, image=init_image, mask_image=mask_image).images[0]

make_image_grid([init_image, mask_image, image], rows=1, cols=3)