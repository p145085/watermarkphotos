import os
from PIL import Image

def overlay_watermark(source_folder, destination_folder, watermark_path):
    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Load the watermark image
    watermark = Image.open(watermark_path).convert("RGBA")

    # Process each image in the source folder
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Open the source image
            source_path = os.path.join(source_folder, filename)
            with Image.open(source_path) as img:
                # Convert image to RGBA if it's not already
                if img.mode != 'RGBA':
                    img = img.convert('RGBA')

                # Resize watermark to fit the image (e.g., 1/4 of the image size)
                width, height = img.size
                wm_width = width // 4
                wm_height = int(wm_width * watermark.size[1] / watermark.size[0])
                wm_resized = watermark.resize((wm_width, wm_height), Image.LANCZOS)

                # Calculate position (bottom-right corner)
                position = (width - wm_width, height - wm_height)

                # Paste the watermark
                img.paste(wm_resized, position, wm_resized)

                # Save the result
                output_path = os.path.join(destination_folder, filename)
                img.save(output_path)

    print("Processing complete!")

# Usage
source_folder = "path/to/source/folder"
destination_folder = "path/to/destination/folder"
watermark_path = "path/to/watermark.png"

overlay_watermark(source_folder, destination_folder, watermark_path)
