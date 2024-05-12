import glob
import os
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Specify the directory of images
image_dir = "/Users/lapyaephyo/Pictures/"
image_exts = ["jpg", "jpeg", "png"]  # Specify the file extension to search for

# Load the pretrained processor and model
processor = AutoProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base")

# Open a file to write the captions
with open("caption.txt", "w") as caption_file:
    # Iterate over each image file in the directory
    for image_ext in image_exts:
        for img_path in glob.glob(os.path.join(image_dir, f"*.{image_ext}")):
            # Load image
            raw_image = Image.open(img_path).convert("RGB")

            # Process the image
            inputs = processor(images=raw_image, return_tensors="pt")

            # Generate a caption for the image
            outputs = model.generate(**inputs, max_new_tokens=50)

            # Decode the generated tokens to text
            caption = processor.decode(outputs[0], skip_special_token=True)

            # Write the caption to the file, prepended by the image path
            caption_file.write(f"{os.path.basename(img_path)}: {caption}\n")
