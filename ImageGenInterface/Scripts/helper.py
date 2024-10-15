
import os
import torch
import argparse
from argparse import ArgumentParser

STANDARD_NEGATIVE_PROMPT = """
    watermarked,
    cartoonish,
    low quality,
    pixelated,
    blurry,
    distorted,
    not realistic,
    dark
"""

def hardware_accelerate_if_available() -> str:
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

    return DEVICE

def enable_memory_save_mode(pipeline) -> None:

    CUDA_AVAILABLE = torch.cuda.is_available()
    MPS_AVAILABLE = torch.backends.mps.is_available()
    # If using GPU or MPS, enable sequential CPU offload to reduce memory usage
    if CUDA_AVAILABLE or MPS_AVAILABLE: pipeline.enable_sequential_cpu_offload(device=DEVICE)
    # Memory saving measures
    pipeline.enable_vae_tiling()
    pipeline.enable_attention_slicing()

def __common_arg_parser() -> ArgumentParser:
    """
    Initializes an ArgumentParser for an AI image generation / inpainting script
    using the runwayml/stable-diffusion-inpainting and runwayml/stable-diffusion-v1-5
    """

    parser = argparse.ArgumentParser(description="An image inpainting script based on the diffusers module")

    parser.add_argument(
        "-p",
        type=bool,
        required=False,
        default=False,
        action="store_true",
        help="Enable performance mode (WARNING: Takes up a lot of memory)"
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
        help="The image mask for the initial image, only used for inpainting jobs."
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
        default=0.8, 
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

    parser.add_argument(
        "-show",
        type=bool,
        required=False,
        default=False,
        action="store_true",
        help="(Optional) Show image when its generated."
    )


    return parser

def init_inpainting_parser() -> ArgumentParser:

    parser = __common_arg_parser()

    parser.add_argument(
        "-inp",
        type=bool,
        required=True,
        action="store_true",
        help="Inpainting mode"
    )

    parser.add_argument(
        "--mask_image",
        type=str,
        required=True,
        help="The path to the mask image given to the AI model."
    )

    return parser
