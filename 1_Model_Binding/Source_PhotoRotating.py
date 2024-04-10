from PIL import Image
import os


def flip_images_in_directory(directory):
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Filter out only the image files
    image_files = [file for file in files if file.endswith(('jpg', 'jpeg', 'png', 'bmp'))]

    # Loop through each image file
    for file_name in image_files:
        try:
            # Open the image file
            image_path = os.path.join(directory, file_name)
            image = Image.open(image_path)

            # Flip the image horizontally
            flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)

            # Save the flipped image, overwriting the original
            flipped_image.save(image_path)

            print(f"Flipped: {file_name}")

        except Exception as e:
            # If there's an error, print it
            print(f"Error processing {file_name}: {e}")


# Provide the path to the directory containing the images
directory_path = r'C:\Users\M\Desktop\test\thumbs'

# Call the function to flip images in the directory
flip_images_in_directory(directory_path)
