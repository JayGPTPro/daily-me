# How to Generate Images with Nano Banana 2 API

## What is this?
This folder contains a Python script (`generate.py`) that uses the Gemini API (Nano Banana 2) to generate images from text prompts. It can also use reference images to maintain consistency (e.g., keeping your face the same across generated images).

## Files You Need

Copy these 3 files into any project folder:

1. **`generate.py`** - The main script that generates images
2. **`.env`** - Contains your Gemini API key (never share this file!)
3. **`requirements.txt`** - Python dependencies list

## First Time Setup

Open Terminal and run:

```bash
pip3 install google-genai python-dotenv Pillow
```

This only needs to be done once on your computer.

## How to Use

### Option 1: Simple text prompt (no reference image)

```bash
cd /path/to/your/folder
python3 -c "
from generate import generate_image
generate_image('A photorealistic image of a golden sunset over the ocean')
"
```

### Option 2: With a reference image (keeps your face/product consistent)

```bash
cd /path/to/your/folder
python3 -c "
from generate import generate_image
generate_image(
    'Your prompt here describing the image you want',
    ['/full/path/to/reference-image.jpg']
)
"
```

### Option 3: With multiple reference images

```bash
cd /path/to/your/folder
python3 -c "
from generate import generate_image
generate_image(
    'Your prompt here',
    ['/path/to/image1.jpg', '/path/to/image2.jpg']
)
"
```

### Option 4: Interactive mode

```bash
cd /path/to/your/folder
python3 generate.py
```

Then type prompts one by one. Type `quit` to exit.

### Option 5: Quick one liner from command line

```bash
python3 generate.py "A cute monkey eating a banana in a jungle"
```

## Where Do Generated Images Go?

All generated images are saved in a `generated_images/` folder that is automatically created inside the folder where you run the script.

File names include part of your prompt + a timestamp so you can find them easily.

## Tips for Better Results

1. **Be specific** - "A photorealistic square image of..." works better than vague descriptions
2. **Mention the style** - Add "Ultra realistic photography" or "Cinematic lighting" at the end
3. **Use reference images** - When you need to keep a face or product consistent across multiple images
4. **Describe what you DON'T want** - "No text, no watermarks, no logos" helps avoid unwanted elements
5. **Specify dimensions** - Say "square image" or "wide horizontal image" or "vertical portrait image"

## Troubleshooting

- **"ERROR: You need to set your API key!"** - Make sure the `.env` file exists in the same folder and contains your key
- **"No image was generated"** - Try rephrasing your prompt, the AI might have flagged something
- **Import errors** - Run `pip3 install google-genai python-dotenv Pillow` again
