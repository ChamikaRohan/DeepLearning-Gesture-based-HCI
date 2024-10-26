import cv2
import sys
import numpy as np
from tensorflow.keras.models import load_model
import mediapipe as mp
from collections import deque
import time

# Add paths for necessary utilities
sys.path.append('../1_Model_Binding')
from Utils.First_frame_getter import first_frame_getter
from Utils.Auto_first_frame_setter import auto_first_frame_setter

sys.path.append('../User_Interface')
from Window_pinner import window_pinner

sys.path.append('../10_Storage_and_utils')
from Payload import Payload

sys.path.append('../1_Model_Binding')
from Dynamic_gesture_prediction_func import predict_gesture_and_direction

sys.path.append('../3_Intended_Gesture_Mapping')
from dynamic_intended_gesture_mapping_func import intended_gesture_and_direction_map

sys.path.append('../8_Dynamic_Gesture_Recognition')
from Dynamic_gesture_extender import combined_gesture_number_finder

# Initialize video capture
cap = cv2.VideoCapture(0)

# Function to initialize payload values
def initiate_payload():
    payload = Payload()
    payload.set_first_gray(first_frame_getter(cap))
    payload.set_gesture_type(1)
    payload.set_mode(2)
    payload.set_model_path("../1_Model_Binding/Media/10_gesture_skelton_model_v13.h5")
    payload.set_gesture_frames({0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0})
    payload.set_direction_frames(deque())
    payload.set_custom_config_path('C:\\Users\\M\\Desktop\\MotionPilot')
    payload.set_hand_window_status(True)
    payload.set_application(1)
    return payload

# Initialize the payload
payload = initiate_payload()

# Function to run gesture recognition and accuracy calculation
def run_gesture_recognition(target_gestures):
    total_dynamic_predictions = 0
    correct_dynamic_gesture_predictions = 0
    recognized_dynamic_gesture_count = 0

    # Loop through predictions and calculate real-time accuracy for dynamic gestures only
    for gesture, direction in predict_gesture_and_direction(cap, payload.get_model_path(),
                                                            payload.get_first_gray(),
                                                            payload.get_gesture_type()):
        # Get intended gesture and direction
        intended_gesture, intended_direction = intended_gesture_and_direction_map(gesture, direction,
                                                                                  payload.get_gesture_frames(),
                                                                                  payload.get_direction_frames())
        # Determine the combined gesture number
        intended_combined_gesture = combined_gesture_number_finder(intended_gesture, intended_direction)

        # Only consider gestures in the dynamic range (10 to 50)
        if intended_combined_gesture is not None and 13 <= intended_combined_gesture <= 50:
            recognized_dynamic_gesture_count += 1
            total_dynamic_predictions += 1

            # Check if the recognized gesture is one of the target dynamic gestures
            if intended_combined_gesture in target_gestures:
                correct_dynamic_gesture_predictions += 1

            # Calculate accuracy based on correct predictions out of total recognized dynamic gestures
            current_dynamic_accuracy = correct_dynamic_gesture_predictions / recognized_dynamic_gesture_count if recognized_dynamic_gesture_count > 0 else 0

            # Print details for debugging
            print(f"Recognized Dynamic Gesture Count: {recognized_dynamic_gesture_count}")
            print(f"Correct Dynamic Gesture Predictions: {correct_dynamic_gesture_predictions}")
            print(f"Total Dynamic Predictions: {total_dynamic_predictions}")
            print(f"Current Real-Time Dynamic Accuracy: {current_dynamic_accuracy:.2f}")
            print("-" * 50)

            # Stop the loop if we have recognized 25 gestures
            if recognized_dynamic_gesture_count >= 25:
                break
        else:
            total_dynamic_predictions += 1

    # Return the results after recognizing 25 dynamic gestures
    final_accuracy = correct_dynamic_gesture_predictions / recognized_dynamic_gesture_count if recognized_dynamic_gesture_count > 0 else 0
    return recognized_dynamic_gesture_count, correct_dynamic_gesture_predictions, total_dynamic_predictions, final_accuracy

# First phase: target gestures {42, 43, 44, 45}
print("Starting second phase with target gestures: {18}")
first_phase_results = run_gesture_recognition({18})
# Wait for 5 seconds before moving to the next phase
print("Pausing for 5 seconds...")
time.sleep(5)

# Second phase: target gestures {10, 11, 12, 13}

print("Starting first phase with target gestures: {42}")
second_phase_results = run_gesture_recognition({42})

# Print results for the first phase
print("\nFirst Phase Results: Gesture Rock Left")
print(f"Final Recognized Dynamic Gesture Count: {first_phase_results[0]}")
print(f"Final Correct Dynamic Gesture Predictions: {first_phase_results[1]}")
print(f"Final Total Frame Predictions: {first_phase_results[2]}")
print(f"Final Dynamic Accuracy: {first_phase_results[3]:.2f}")

# Print results for the second phase
print("\nSecond Phase Results: Gesture Three Up")
print(f"Final Recognized Dynamic Gesture Count: {second_phase_results[0]}")
print(f"Final Correct Dynamic Gesture Predictions: {second_phase_results[1]}")
print(f"Final Total Frame Predictions: {second_phase_results[2]}")
print(f"Final Dynamic Accuracy: {second_phase_results[3]:.2f}")

# Release the video capture object
cap.release()
