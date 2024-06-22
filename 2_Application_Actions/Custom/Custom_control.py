import pyautogui
import sys

sys.path.append('../../2_Application_Actions')
from Utils.Focus_on_window import focus_on_window

def custom_application_mapper(gesture, custom_window_title, gesture_map):
    #Find and activate the custom application window
    window_titles = [f'{custom_window_title}']
    for title in window_titles:
        focus_on_window(title)

    if gesture is None:
        return

    gesture_data = gesture_map.get(str(gesture), None)

    if gesture_data:
        for action_type, action_value in gesture_data.items():
            if action_type == "press":
                pyautogui.press(action_value)
                print(f"Performed action 'press {action_value}' for gesture {gesture}")
            elif action_type == "hotkey":
                pyautogui.hotkey(*action_value)
                print(f"Performed action 'hotkey {action_value}' for gesture {gesture}")
            elif action_type == "scroll":
                if action_value == "1":
                    pyautogui.scroll(80)
                    for _ in range(10):
                        pyautogui.scroll(50)
                    print(f"Performed action 'scroll up' for gesture {gesture}")
                elif action_value == "-1":
                    pyautogui.scroll(-80)
                    for _ in range(10):
                        pyautogui.scroll(-50)
                    print(f"Performed action 'scroll down' for gesture {gesture}")
            else:
                print(f"No valid action type found for gesture {gesture}")
    else:
        print(f"No action mapped for gesture {gesture}")



"""
gesture_map = {
    "0": { "press": "x" },
    "1": { "hotkey": ["ctrl", "v"] },
    "2": { "press": "1" },
    "3": { "press": "=" },
    "4": { "scroll": "1" },
    "5": { "scroll": "-1" },
    "6": {},
    "7": {},
    "8": {},
    "9": {}
}

# Simulate gesture input (replace with actual gesture recognition logic)
gesture = "3"
custom_window_title = "YourCustomApp"

# Call the function with the gesture map
control_custom_application(gesture, custom_window_title, gesture_map)
"""
