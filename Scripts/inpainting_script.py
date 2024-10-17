import torch, os, sys, argparse
from diffusers import StableDiffusionInpaintPipeline
from diffusers.utils import load_image
from PIL import Image
from PIL.Image import Image as Image_obj
from argparse import ArgumentParser

def hardware_accelerate_if_available() -> str:
    DEVICE: str = ""
    CUDA = torch.cuda.is_available()
    MPS = torch.backends.mps.is_available()

    # Check if cuda is available
    if CUDA:

        DEVICE = "cuda"
        
    # Check if MPS is available
    elif MPS:

        DEVICE = "mps"

        # Let MPS use all available memory, may cause system failure
        os.environ["PYTORCH_MPS_HIGH_WATERMARK_RATIO"] = "0.0"

    # If neither CUDA or MPS is available, run on CPU
    else:

        num_threads = os.cpu_count()

        torch.set_num_threads(num_threads-1)  # Adjust based on your CPU

        DEVICE = "cpu"

    return DEVICE

def enable_memory_save_mode(pipeline: StableDiffusionInpaintPipeline) -> None:
    CUDA_AVAILABLE = torch.cuda.is_available()
    MPS_AVAILABLE = torch.backends.mps.is_available()
    # If using GPU or MPS, enable sequential CPU offload to reduce memory usage
    if CUDA_AVAILABLE or MPS_AVAILABLE: pipeline.enable_sequential_cpu_offload(device=DEVICE)
    # Memory saving measures
    pipeline.enable_vae_tiling()
    pipeline.enable_attention_slicing()

def init_arg_parser() -> ArgumentParser:
    """
    Initializes an ArgumentParser for an AI image generation / inpainting script
    using the runwayml/stable-diffusion-inpainting and runwayml/stable-diffusion-v1-5
    """

    STANDARD_NEGATIVE_PROMPT = "watermarked, cartoonish, low quality, pixelated, blurry, distorted, un-realistic, dark"

    parser = argparse.ArgumentParser(description="An image inpainting script based on the diffusers module")

    parser.add_argument(
        "-p",
        required=False,
        default=False,
        action="store_true",
        help="Enable performance mode (WARNING: Takes up a lot of memory)"
    )

    parser.add_argument(
        "-show",
        required=False,
        default=False,
        action="store_true",
        help="(Optional) Show image when its generated."
    )

    parser.add_argument(
        "--init_image",
        type=str,
        required=True,
        help="The path to the initial image given to the AI model."
    )

    parser.add_argument(
        "--mask_image",
        type=str,
        required=True,
        help="The path to the mask image given to the AI model."
    )

    parser.add_argument(
        "--prompt",
        type=str,
        required=True,
        help="The prompt for the image inpainting"
    )

    parser.add_argument(
        "--n_prompt",
        type=str,
        required=False,
        default=STANDARD_NEGATIVE_PROMPT,
        help="(Optional) The negative prompt for the image inpainting, this tells the model what to avoid"
    )

    parser.add_argument(
        "--strength",
        type=float,
        required=False,
        default=1, 
        help="(Optional) The strength of the image inpainting, this controls how much creative liberty the model gets."
    )

    parser.add_argument(
        "--num_inf",
        type=int,
        required=False,
        default=50,
        help="(Optional) The number of inference cycles performed during inpainting, higher inference takes longer times but usually give more well defined pictures."
    )

    parser.add_argument(
        "--guidance",
        type=float,
        required=False,
        default=7.5,
        help="(Optional) The models guidance value, controls how much the model listens to the input prompt."
    )

    return parser

parser = init_arg_parser()

args = parser.parse_args()

# Constants for this model
MODEL_NAME: str = "stabilityai/stable-diffusion-2-inpainting" #"runwayml/stable-diffusion-inpainting" 
MODEL_PATH: str = f"./local_models/{MODEL_NAME}" # Path of local model

# Parse args
GUIDANCE: float = args.guidance
MASK_IMAGE_PATH: str = args.mask_image
NEGATIVE_PROMPT: str = args.n_prompt
NUM_INF: int = args.num_inf
OBJ_IMAGE_PATH: str = args.init_image
PROMPT: str = args.prompt
SHOW: bool = args.show
STRENGTH: float = args.strength
VANILLA: bool = not args.p

# Get device
DEVICE: str = hardware_accelerate_if_available()

# Setup pipeline
pipeline = StableDiffusionInpaintPipeline.from_pretrained(
    MODEL_PATH if os.path.exists(MODEL_PATH) else MODEL_NAME,
    torch_dtype=torch.float32
)

# Save model if it isnt saved yet
if not os.path.exists(MODEL_PATH): pipeline.save_pretrained(MODEL_PATH)

# Tell the model to pipe to the right device
pipeline.to(DEVICE)

# Conditionally enable memory saving measures
if VANILLA: enable_memory_save_mode(pipeline)

# Initialize images from a path
init_image = load_image(Image.open(OBJ_IMAGE_PATH)).resize((512,512))
mask_image = load_image(Image.open(MASK_IMAGE_PATH)).resize((512,512))

image: Image_obj = pipeline(
    prompt=PROMPT,
    negative_prompt=NEGATIVE_PROMPT,
    image=init_image, 
    mask_image=mask_image,
    strength=STRENGTH,
    num_inference_steps=NUM_INF,
    guidance_scale=GUIDANCE

).images[0]

if SHOW: image.show()

sys.exit(0)

#EXAMPLE USE: python3 inpainting_script.py -show --init_image Trials/original-image-small.jpg --mask_image Trials/original-image-small-mask.jpg --prompt "Place this table in an european livingroom, the tables leg should be on the floor" --n_prompt "Tables with objects under them"