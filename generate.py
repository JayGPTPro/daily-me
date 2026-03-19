"""
Nano Banana 2 - Image Generator
Uses Google Gemini API to generate images from text prompts.
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image
import io

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key or api_key == "YOUR_API_KEY_HERE":
    print("ERROR: You need to set your API key!")
    print("Open the .env file and replace YOUR_API_KEY_HERE with your actual key.")
    sys.exit(1)

# Connect to Google AI
client = genai.Client(api_key=api_key)

# Create output folder for generated images
output_dir = Path("generated_images")
output_dir.mkdir(exist_ok=True)


def generate_image(prompt: str, reference_images: list = None) -> Optional[str]:
    """
    Generate an image from a text prompt, optionally using reference images.

    Args:
        prompt: Description of the image you want to create
        reference_images: List of file paths to reference images

    Returns:
        Path to the saved image, or None if failed
    """
    print(f"Generating image: '{prompt}'...")
    if reference_images:
        print(f"Using {len(reference_images)} reference image(s)")

    try:
        # Build content parts: reference images + text prompt
        contents = []
        if reference_images:
            for img_path in reference_images:
                img = Image.open(img_path)
                # Convert to RGB if needed (handles RGBA, palette, etc.)
                if img.mode not in ("RGB", "L"):
                    img = img.convert("RGB")
                # Resize if too large (Gemini has limits)
                max_size = 1024
                if max(img.size) > max_size:
                    img.thumbnail((max_size, max_size))
                buf = io.BytesIO()
                img.save(buf, format="JPEG")
                contents.append(types.Part.from_bytes(
                    data=buf.getvalue(),
                    mime_type="image/jpeg",
                ))
            contents.append(prompt)
        else:
            contents = prompt

        response = client.models.generate_content(
            model="gemini-3.1-flash-image-preview",
            contents=contents,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE", "TEXT"],
            ),
        )

        # Find the image in the response
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                # Save the image
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                safe_name = "".join(c if c.isalnum() or c == " " else "" for c in prompt[:40])
                safe_name = safe_name.strip().replace(" ", "_")
                filename = output_dir / f"{safe_name}_{timestamp}.png"

                image = Image.open(io.BytesIO(part.inline_data.data))
                image.save(filename)

                print(f"Image saved to: {filename}")
                return str(filename)

        print("No image was generated. Try a different prompt.")
        return None

    except Exception as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    print("=" * 50)
    print("  Nano Banana 2 - Image Generator")
    print("=" * 50)
    print()

    if len(sys.argv) > 1:
        # Get prompt from command line arguments
        prompt = " ".join(sys.argv[1:])
        generate_image(prompt)
    else:
        # Interactive mode
        print("Type a description of the image you want to create.")
        print("Type 'quit' to exit.\n")

        while True:
            prompt = input("Describe your image > ").strip()
            if prompt.lower() in ("quit", "exit", "q"):
                print("Bye!")
                break
            if prompt:
                generate_image(prompt)
                print()
