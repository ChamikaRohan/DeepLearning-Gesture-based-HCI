import keyboard
from Payload import Payload
import sys
from threading import Thread

sys.path.append('../5_Mode_Selector')
from Mode_toggler import mode_toggler


# Define the mode changer function
def mode_changer():
    payload = Payload()
    def change_mode(event):
        current_mode = payload.get_mode()
        new_mode = mode_toggler(current_mode)
        payload.set_mode(new_mode)
        print(f"Mode changed from {current_mode} to: {new_mode}")

    # Hook the 's' key press event to the change_mode function
    keyboard.on_press_key('s', change_mode)

    # Block the main thread to keep the hook active
    keyboard.wait('esc')  # Use 'esc' to exit the program gracefully

