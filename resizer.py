# Python program used to batch resize images without anti-aliasing in a directory tree using Pillow (PIL) library.
# This is done in order to maintain the pixelated look of the images when upscaled.
# To install Pillow, run 'pip install Pillow' in the terminal.
# This program will resize all PNG and JPG images in the 'sprites' directory and its subdirectories by a factor of specified by the user

from PIL import Image
import os

# Define the directory containing your images
input_dir = "sprites"  # This is the directory where the original images are stored.
output_dir = "resized_sprites"  # This is the directory where the resized images will be saved.
new_size_multiplier = 10  # This multiplier will enlarge each dimension (width and height) of the image by 10 times.

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)  # Creates the output directory if it doesn't exist yet. If it does exist, nothing happens due to 'exist_ok=True'.

# Walk through the directory tree
for root, dirs, files in os.walk(input_dir):  # os.walk() is used to generate file names in a directory tree. It walks through each directory and subdirectory within the input_dir.
    for filename in files:  # Loop through each file found in the current directory.
        if filename.endswith('.png') or filename.endswith('.jpg'):  # This checks if the file is a PNG or JPG image. Only these files will be processed.
            try:
                img_path = os.path.join(root, filename)  # Combine the directory path (root) with the filename to get the full path to the image.
                img = Image.open(img_path)  # Open the image file using Pillow's Image class. This loads the image into memory.

                # Upsize the image without anti-aliasing
                new_size = (img.width * new_size_multiplier, img.height * new_size_multiplier)  # Calculate the new dimensions of the image by multiplying the width and height by the size multiplier.
                upsized_img = img.resize(new_size, Image.NEAREST)  # Resize the image to the new dimensions using the 'NEAREST' method. 'NEAREST' means nearest neighbor interpolation, which avoids anti-aliasing and keeps the image pixelated.

                # Save the upsized image to a corresponding subdirectory in the output folder
                relative_path = os.path.relpath(root, input_dir)  # Compute the relative path from the current directory to the input directory. This maintains the folder structure.
                output_subdir = os.path.join(output_dir, relative_path)  # Combine the output directory with the relative path to create the subdirectory path where the resized image will be saved.
                os.makedirs(output_subdir, exist_ok=True)  # Ensure the output subdirectory exists; create it if necessary.
                output_path = os.path.join(output_subdir, filename)  # Combine the output subdirectory with the original filename to get the full path where the resized image will be saved.
                upsized_img.save(output_path)  # Save the resized image to the specified path.

                print(f"Processed and saved: {output_path}")  # Print a message to confirm that the image was processed and saved successfully.

            except Exception as e:  # This block catches any errors that occur during image processing.
                print(f"Error processing {filename}: {e}")  # If there's an error, print a message showing which file failed and what the error was.

print("Batch resizing complete!")  # After all files have been processed, print a final message to indicate the operation is complete.
