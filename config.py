import os
from dotenv import load_dotenv

load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

BASE_URL = "https://integrate.api.nvidia.com/v1"

MODEL_NAME = "nvidia/nemotron-3-ultra-550b-a55b"

if not NVIDIA_API_KEY:
    raise ValueError(
        "NVIDIA_API_KEY not found. Please add it to your .env file."
    )
