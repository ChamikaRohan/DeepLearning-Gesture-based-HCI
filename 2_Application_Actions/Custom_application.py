import os
import sys

sys.path.append('../../2_Application_Actions')
from Utils.Focus_on_window import focus_on_window
from Custom.Custom_control import custom_application_mapper
from Custom.Load_gesture_map import load_gesture_map
from Custom.Window_title_matcher import window_title_matcher

"""
Function to control media player application
"""
def control_custom_application(gesture):
    try:
        #Load configuration from JSON file
        folder_path = r'C:\\Users\M\Desktop\MotionPilot'
        file_path = os.path.join(folder_path, 'custom_configs.json')
        custom_config = load_gesture_map(file_path)

        #Find the custom application titles
        user_given_custom_window_titles = custom_config.get("custom_window_title", [])
        #Find the correct window title
        custom_window_title = window_title_matcher(user_given_custom_window_titles)

        #Find the custom gesture map
        gesture_map = custom_config.get("gesture_map", {})

        #Call custom_application_mapper function with loaded parameters
        custom_application_mapper(gesture, custom_window_title, gesture_map)

    except Exception as e:
        print(f"Error in controlling media player: {str(e)}")



"""
# Example usage:
gesture = "1"  # Replace with actual gesture input logic
control_custom_application(gesture)
"""


