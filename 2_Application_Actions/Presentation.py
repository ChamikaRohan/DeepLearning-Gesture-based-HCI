import time

import pyautogui
from Utils.Focus_on_window import focus_on_window
from Utils.Powerpoint_mode_checker import is_fullscreen_mode

"""
Function to control presentation slides

Gesture Mapping:
0: Go to previous slide (left)
4: Go to next slide (right)
2: Enter slide show mode
3: Exit slide show mode
"""
def control_presentation(gesture):
    #Find and activae the presentation window
    window_titles = ["PowerPoint"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        return
    elif gesture == 0:
        print("Slide Show Mode On/Off")
        if is_fullscreen_mode():
            pyautogui.press("esc")  # If in full screen, exit full screen mode
        else:
            pyautogui.press("f5")
        time.sleep(1)
    elif gesture == 3:
        print("Switch to Next Slide")
        pyautogui.hotkey("right")
        time.sleep(0.5)
    elif gesture == 4:
        print("Switch to Previous Slide")
        pyautogui.hotkey("left")
        time.sleep(0.5)




