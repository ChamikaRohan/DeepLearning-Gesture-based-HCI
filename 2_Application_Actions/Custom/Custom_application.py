import pyautogui
import time
import sys

sys.path.append('../../2_Application_Actions')
from Utils.Focus_on_window import focus_on_window

"""
Function to control custom application
"""

def control_custom_application(gesture, custom_window_title, gesture_map):
    # Find and activate the custom application window
    window_titles = [f'{custom_window_title}']
    for title in window_titles:
        focus_on_window(title)

    if gesture is None:
        return

    # Get the corresponding action from the gesture map
    action = gesture_map.get(gesture, None)

    if action:
        pyautogui.press(action)
        print(f"Performed action '{action}' for gesture {gesture}")
        time.sleep(1)
    else:
        print(f"No action mapped for gesture {gesture}")


"""
# Example 

gesture_map = {
    0: "space",  # Play/Stop the movie
    1: "up",  # Example: Increase volume
    2: "down",  # Example: Decrease volume
    3: "right",  # Example: Seek forward
    4: "left",  # Example: Seek backward
    5: "enter"  # Example: Full screen
}

custom_window_title = "My Custom Application"
gesture = 1  # Example gesture
control_custom_application(gesture, custom_window_title, gesture_map)

gesture = 4  # Example gesture
control_custom_application(gesture, custom_window_title, gesture_map)

gesture = 5  # Example gesture
control_custom_application(gesture, custom_window_title, gesture_map)
"""
