import os
from PIL import Image


def resize_images_in_directory(directory, new_width, new_height):
    # List all files in the directory
    files = os.listdir(directory)

    # Loop through each file
    for file in files:
        # Check if the file is an image (you can add more image extensions if needed)
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            # Open the image file
            input_path = os.path.join(directory, file)
            image = Image.open(input_path)

            # Resize the image
            resized_image = image.resize((new_width, new_height))

            # Overwrite the original image with the resized one
            resized_image.save(input_path)

    print("All files resized successfully!")

# Example usage:
input_directory = r'C:\Users\chiara\Documents\FINAL YEAR\FYP\dataset\10 gestures modified\test\test\9'
new_width = 75
new_height = 75
resize_images_in_directory(input_directory, new_width, new_height)
