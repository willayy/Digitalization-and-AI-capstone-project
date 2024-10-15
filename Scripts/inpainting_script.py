import torch, os, sys
from diffusers import AutoPipelineForInpainting
from diffusers.utils import load_image
from PIL import Image
from PIL.Image import Image
from helper import hardware_accelerate_if_available, enable_memory_save_mode, init_inpainting_parser

parser = init_inpainting_parser()

args = parser.parse_args()

# Constants for this model
MODEL_NAME: str = "runwayml/stable-diffusion-inpainting"
MODEL_PATH: str = f"./local_models/{MODEL_NAME}" # Path of local model

# Parse args
NEGATIVE_PROMPT: str = args.n_prompt
OBJ_IMAGE_PATH: str = args.init_image
MASK_IMAGE_PATH: str = args.mask_image
PROMPT: str = args.prompt
VANILLA: bool = not args.p
STRENGTH: float = args.strength
NUM_INF: int = args.num_inf
GUIDANCE: float = args.guidance
SHOW: bool = args.show

# Get device
DEVICE: str = hardware_accelerate_if_available()

# Setup pipeline
pipeline = AutoPipelineForInpainting.from_pretrained(
    MODEL_PATH if os.path.exists(MODEL_PATH) else "runwayml/stable-diffusion-inpainting",
    torch_dtype=torch.float32
)

# Save model if it isnt saved yet
if not os.path.exists(MODEL_PATH): pipeline.save_pretrained(MODEL_PATH)

# Tell the model to pipe to the right device
pipeline.to(DEVICE)

# Conditionally enable memory saving measures
if VANILLA: enable_memory_save_mode(pipeline)

# Initialize images from a path
init_image = load_image(Image.open(OBJ_IMAGE_PATH))
mask_image = load_image(Image.open(MASK_IMAGE_PATH))

# Resize image if needed
if init_image.height != 512 or init_image.width != 512: init_image = init_image.resize((512,512))
if mask_image.height != 512 or mask_image.width != 512: mask_image = mask_image.resize((512,512))

image: Image = pipeline(prompt=PROMPT, negative_prompt=NEGATIVE_PROMPT, image=init_image, mask_image=mask_image).images[0]

if SHOW: image.show()

sys.exit(0)
