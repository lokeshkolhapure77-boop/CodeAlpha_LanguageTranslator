import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Get the NVIDIA API key
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")

# NVIDIA OpenAI-compatible API endpoint
BASE_URL = "https://integrate.api.nvidia.com/v1"

# Model name
MODEL_NAME = "nvidia/nemotron-3-ultra-550b-a55b"

# Check if API key exists
if not NVIDIA_API_KEY:
    raise ValueError(
        "NVIDIA_API_KEY not found. Please add it to your .env file."
    )