import pyautogui
import time
import pygetwindow as gw

"""
Function to control media player

Gesture Mapping:
Gesture 0: Stop the media (specific player dependent)
Gesture 1: Play/Pause the media (specific player dependent)
Gesture 2: Increase system volume
Gesture 3: Decrease system volume
"""
def control_media_player(gesture):
    # Find the active window
    active_window = gw.getActiveWindow()
    print(active_window)
    if gesture == 0:
        # Stop media
        pyautogui.press("space")
        print("Media Stopped/Paused")
    elif gesture == 1:
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
    time.sleep(1)  # Add a small delay after each action

time.sleep(2)
control_media_player(2)