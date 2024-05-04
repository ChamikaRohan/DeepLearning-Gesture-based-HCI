import pyautogui
import time
from FocusOnWindow import focus_on_window

"""
Function to control media player

Gesture Mapping:
Gesture 0: Stop the media (specific player dependent)
Gesture 4: Play/Pause the media (specific player dependent)
Gesture 2: Increase system volume
Gesture 3: Decrease system volume
"""
def control_media_player(gesture):
    # Find the active window
    window_titles = ["Movies", "VLC media player"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        print("None")
    elif gesture == 0:
        # Stop media
        pyautogui.press("space")
        print("Media Stopped/Paused")
    elif gesture == 4:
        # Play/Pause media
        pyautogui.press("space")
        print("Media Play/Continue")
    elif gesture == 2:
        # Increase system volume
        pyautogui.press("volumeup")
        print("System Volume Increased")
    elif gesture == 3:
        # Decrease system volume
        pyautogui.press("volumedown")
        print("System Volume Decreased")
