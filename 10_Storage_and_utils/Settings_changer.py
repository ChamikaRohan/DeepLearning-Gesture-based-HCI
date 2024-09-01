import keyboard
from Payload import Payload
import sys
import cv2

sys.path.append('../5_Mode_Selector')
from Mode_toggler import mode_toggler

# Define the mode changer function
def settings_changer():
    payload = Payload()
    def change_mode(event):
        current_mode = payload.get_mode()
        new_mode = mode_toggler(current_mode)
        payload.set_mode(new_mode)
        print(f"Mode changed from {current_mode} to: {new_mode}")
    def change_gesture_type(event):
        current_gesture_type = payload.get_gesture_type()
        new_gesture_type = mode_toggler(current_gesture_type)
        payload.set_gesture_type(new_gesture_type)
        print(f"Gesture type changed from {current_gesture_type} to: {new_gesture_type}")

    # keyboard.on_press_key('s', change_mode)
    # keyboard.on_press_key('g', change_gesture_type)



