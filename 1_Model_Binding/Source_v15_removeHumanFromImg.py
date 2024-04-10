import cv2
import numpy as np

# Load the image with the human
image_with_human = cv2.imread('Images/image_with_human.jpg')

# Load the background image
background = cv2.imread('Images/background.jpg')

# Convert both images to grayscale
gray_image_with_human = cv2.cvtColor(image_with_human, cv2.COLOR_BGR2GRAY)
gray_background = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

# Calculate the absolute difference between the two images
diff = cv2.absdiff(gray_image_with_human, gray_background)

# Apply a threshold to create a binary mask
_, mask = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)

# Invert the mask
mask_inv = cv2.bitwise_not(mask)

# Apply the mask to the image with the human
image_without_human = cv2.bitwise_and(image_with_human, image_with_human, mask=mask_inv)

# Display the result
cv2.imshow('Image with Human', image_with_human)
cv2.imshow('Background', background)
cv2.imshow('Image without Human', image_without_human)
cv2.waitKey(0)
cv2.destroyAllWindows()
