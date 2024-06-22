import os
from Save_gesture_map import save_gesture_map

"""
Generate a custom configuration JSON based on provided window titles and gestures.

Args:
- custom_window_titles (list): List of possible window titles.
- gestureX_act_type (str): Action type for gesture X.
- gestureX_act_keys (str or list): Keys for gesture X action.

Returns:
- dict: Generated custom configuration JSON.
"""

def custom_config_creator(custom_window_titles,
                           gesture0_act_type, gesture0_act_keys,
                           gesture1_act_type, gesture1_act_keys,
                           gesture2_act_type, gesture2_act_keys,
                           gesture3_act_type, gesture3_act_keys,
                           gesture4_act_type, gesture4_act_keys,
                           gesture5_act_type, gesture5_act_keys,
                           gesture6_act_type, gesture6_act_keys,
                           gesture7_act_type, gesture7_act_keys,
                           gesture8_act_type, gesture8_act_keys,
                           gesture9_act_type, gesture9_act_keys):

    gesture_map = {
        "0": { gesture0_act_type: gesture0_act_keys },
        "1": { gesture1_act_type: gesture1_act_keys },
        "2": { gesture2_act_type: gesture2_act_keys },
        "3": { gesture3_act_type: gesture3_act_keys },
        "4": { gesture4_act_type: gesture4_act_keys },
        "5": { gesture5_act_type: gesture5_act_keys },
        "6": { gesture6_act_type: gesture6_act_keys },
        "7": { gesture7_act_type: gesture7_act_keys },
        "8": { gesture8_act_type: gesture8_act_keys },
        "9": { gesture9_act_type: gesture9_act_keys }
    }

    custom_config = {
        "custom_window_title": custom_window_titles,
        "gesture_map": gesture_map
    }

    folder_path = r'C:\\Users\M\Desktop\MotionPilot'
    file_path = os.path.join(folder_path, 'custom_configs.json')
    save_gesture_map(file_path , custom_config)





"""
# Define custom window titles and gesture actions
custom_window_titles = ["Adobe Photoshop", "Hero12"]
gesture0_act_type, gesture0_act_keys = "press", "x"
gesture1_act_type, gesture1_act_keys = "hotkey", ["ctrl", "z"]
gesture2_act_type, gesture2_act_keys = "hotkey", ["ctrl", "alt", "z"]
gesture3_act_type, gesture3_act_keys = "press", "d"
gesture4_act_type, gesture4_act_keys = "hotkey", ["ctrl", "s"]
gesture5_act_type, gesture5_act_keys = "hotkey", ["ctrl", "shift", "s"]
gesture6_act_type, gesture6_act_keys = "press", "alt"
gesture7_act_type, gesture7_act_keys = "press", "shift"
gesture8_act_type, gesture8_act_keys = "press", "["
gesture9_act_type, gesture9_act_keys = "press", "]"

# Generate custom configuration JSON
custom_config_creator(
    custom_window_titles,
    gesture0_act_type, gesture0_act_keys,
    gesture1_act_type, gesture1_act_keys,
    gesture2_act_type, gesture2_act_keys,
    gesture3_act_type, gesture3_act_keys,
    gesture4_act_type, gesture4_act_keys,
    gesture5_act_type, gesture5_act_keys,
    gesture6_act_type, gesture6_act_keys,
    gesture7_act_type, gesture7_act_keys,
    gesture8_act_type, gesture8_act_keys,
    gesture9_act_type, gesture9_act_keys
)
"""


