import os
import cv2
import shutil

# Function to rotate images and save to new folders
def rotate_images_and_save(original_dir, rotated_dir):
    # Create rotated_dir if it doesn't exist
    if not os.path.exists(rotated_dir):
        os.makedirs(rotated_dir)

    # List subdirectories (gestures) in the original directory
    gestures = os.listdir(original_dir)

    for gesture in gestures:
        gesture_original_path = os.path.join(original_dir, gesture)
        gesture_rotated_path = os.path.join(rotated_dir, gesture)

        # Create rotated gesture folder if it doesn't exist
        if not os.path.exists(gesture_rotated_path):
            os.makedirs(gesture_rotated_path)

        # List images in the original gesture folder
        images = os.listdir(gesture_original_path)

        for image_name in images:
            # Read the image
            image_path = os.path.join(gesture_original_path, image_name)
            image = cv2.imread(image_path)

            # Rotate the image (example: 90 degrees clockwise)
            rotated_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE  )

            # Save the rotated image to the new folder
            rotated_image_path = os.path.join(gesture_rotated_path, image_name)
            cv2.imwrite(rotated_image_path, rotated_image)

# Paths to original and rotated folders
original_dataset_dir = 'dataset/original'
rotated_dataset_dir = 'dataset/rotated'

# Rotate images and save to new folders
rotate_images_and_save(original_dataset_dir, rotated_dataset_dir)

print("Images rotated and saved to new folders.")
