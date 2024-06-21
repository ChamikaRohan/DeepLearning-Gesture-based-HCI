import json
import os

"""
Function to load gesture_map from JSON file
"""
def load_gesture_map(file_path):
    with open(file_path, 'r') as f:
        gesture_map = json.load(f)
    print("Loaded custom gesture map: ", gesture_map)
    return gesture_map


"""
# Example usage: Load gesture_map from a file
folder_path = r'C:\\Users\M\Desktop\TestAppName'
os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist
file_path = os.path.join(folder_path, 'custom_gesture_map.json')

loaded_custom_gesture_map = load_gesture_map(file_path)
print("Loaded custom gesture map: ", loaded_custom_gesture_map)
"""