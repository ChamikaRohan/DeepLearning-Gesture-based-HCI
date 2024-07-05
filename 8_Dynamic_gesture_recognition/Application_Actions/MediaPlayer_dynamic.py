import pyautogui
import sys

sys.path.append('../2_Application_Actions')
from Utils.Focus_on_window import focus_on_window

import time

"""
Function to control media player

Gesture Mapping:
Gesture 0: Play/Stop the movie
Gesture 4: Volume Increased
Gesture 2: Volume Decreased
Gesture 3: Switch/exit full-screen mode
Gesture 6: Seek forward
Gesture 7: Seek backward
Gesture 5: Take a screenshot
"""
def dynamic_control_media_player(gesture):
    #Find and activate the movie player window
    window_titles = ["Movies", "VLC media player"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        return
    elif gesture == 21:
        pyautogui.press("space")
        print("Play/Stop the movie")
        time.sleep(1)
    elif gesture == 28:
        pyautogui.scroll(1)
        print("Volume Increased")
    elif gesture == 29:
        pyautogui.scroll(-1)
        print("Volume Decreased")
    elif gesture == 20:
        pyautogui.press("f")
        print("Switch/exit full-screen mode")
        time.sleep(1)
    elif gesture == 19:
        pyautogui.keyDown('ctrl')
        pyautogui.press('right')
        pyautogui.keyUp('ctrl')
        print("Seeking Forward")
    elif gesture == 18:
        pyautogui.keyDown('ctrl')
        pyautogui.press('left')
        pyautogui.keyUp('ctrl')
        print("Seeking Backward")
    elif gesture == 32:
        print("Taking a screenshot")
        pyautogui.hotkey("winleft", "printscreen")
        time.sleep(1)
