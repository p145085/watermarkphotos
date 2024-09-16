This script does the following:

It imports the necessary modules: os for file operations and PIL (Python Imaging Library) for image processing.
The overlay_watermark function takes three parameters: the source folder path, the destination folder path, and the path to the watermark image.
It creates the destination folder if it doesn't exist.
It loads the watermark image and converts it to RGBA mode to preserve transparency.
It iterates through each image in the source folder.
For each image, it:
Opens the image
Resizes the watermark to 1/4 of the image width (maintaining aspect ratio)
Positions the watermark in the bottom-right corner
Pastes the watermark onto the image
Saves the result in the destination folder
Finally, it prints a completion message.
To use this script, you'll need to:

Install the Pillow library if you haven't already: pip install Pillow
Replace the placeholder paths with your actual folder and watermark paths
Run the script
This script assumes that your watermark is a PNG file with transparency. If your watermark is in a different format or you want to adjust its size or position, you can modify the script accordingly.
