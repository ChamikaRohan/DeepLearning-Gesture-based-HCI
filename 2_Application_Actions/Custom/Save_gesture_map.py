import json
import os

"""
Function to save custom gesture map as JSON file local storage
"""
def save_gesture_map(file_path, gesture_map):
    with open(file_path, 'w') as f:
        json.dump(gesture_map, f, indent=4)
    print(f"Custom gesture map successfully saved to {file_path}")


"""
# Example usage: Save gesture_map to a file
gesture_map = {
    0: "space",    # Play/Stop the movie
    1: "up",       # Example: Increase volume
    2: "down",     # Example: Decrease volume
    3: "right",    # Example: Seek forward
    4: "left",     # Example: Seek backward
    5: "enter",    # Example: Full screen
    6: "esc",      # Example: Exit full screen
    7: "m",        # Example: Mute/Unmute
    8: "p",        # Example: Pause
    9: "s"         # Example: Stop
}

folder_path = r'C:\\Users\M\Desktop\TestAppName'
os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist
file_path = os.path.join(folder_path, 'custom_gesture_map.json')

save_gesture_map(file_path, gesture_map)

"""

