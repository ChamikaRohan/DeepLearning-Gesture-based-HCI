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
    elif gesture == 21 or gesture == 20:
        pyautogui.press("space")
        print("Play/Stop the movie")
        time.sleep(1)
    elif gesture == 28:
        pyautogui.scroll(1)
        print("Volume Increased")
        time.sleep(0.5)
    elif gesture == 29:
        pyautogui.scroll(-1)
        print("Volume Decreased")
        time.sleep(0.5)
    elif gesture == 32 or gesture == 33:
        pyautogui.press("f")
        print("Switch/exit full-screen mode")
        time.sleep(1)
    elif gesture == 22:
        pyautogui.keyDown('ctrl')
        pyautogui.press('right')
        pyautogui.keyUp('ctrl')
        print("Seeking Forward")
    elif gesture == 23:
        pyautogui.keyDown('ctrl')
        pyautogui.press('left')
        pyautogui.keyUp('ctrl')
        print("Seeking Backward")
    elif gesture == 30 or gesture == 31:
        print("Taking a screenshot")
        pyautogui.hotkey("winleft", "printscreen")
        time.sleep(1)
