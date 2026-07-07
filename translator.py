from openai import OpenAI
from config import NVIDIA_API_KEY, BASE_URL, MODEL_NAME

# Create the NVIDIA client
client = OpenAI(
    base_url=BASE_URL,
    api_key=NVIDIA_API_KEY,
)

def translate_text(text, source_language, target_language):
    """
    Translate text using NVIDIA Nemotron.
    """

    prompt = f"""
You are a professional translator.

Translate the following text from {source_language} to {target_language}.

Rules:
- Return ONLY the translated text.
- Do not explain anything.
- Preserve punctuation.
- Preserve formatting.

Text:
{text}
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2,
            max_tokens=1000
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"Error: {e}"