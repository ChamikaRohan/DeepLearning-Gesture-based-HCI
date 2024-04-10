import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import cv2

# Load the trained model
model = load_model("Media/3_gesture_model_2.h5")

# Load and preprocess the image
img_path = ('Images/image5.png')
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# Apply thresholding to create a binary image
_, binary_img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)

# Resize the binary image to match the model's input size
resized_img = cv2.resize(binary_img, (64, 64))

# Convert grayscale to RGB by repeating the single channel
img_rgb = cv2.cvtColor(resized_img, cv2.COLOR_GRAY2RGB)

# Expand dimensions to create a batch of 1 image
img_array = np.expand_dims(img_rgb, axis=0)
img_array = img_array.astype('float32') / 255.0  # Normalize to [0, 1]

# Make predictions
predictions = model.predict(img_array)

# Get the predicted class label
predicted_class = np.argmax(predictions)

# Map class indices to gesture names
gesture_names = {
    0: 'Gesture 1',
    1: 'Gesture 2',
    2: 'Gesture 3'
}

# Print the predicted gesture
print("Predicted Gesture:", gesture_names[predicted_class])