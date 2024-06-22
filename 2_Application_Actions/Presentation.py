import time

import pyautogui
from Utils.Focus_on_window import focus_on_window

"""
Function to control presentation slides

Gesture Mapping:
4: Go to previous slide (left)
3: Go to next slide (right)
0: Enter slide show mode
5: Exit slide show mode
"""
def control_presentation(gesture):
    #Find and activate the presentation window
    window_titles = ["PowerPoint"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        return
    elif gesture == 0:
        print("Slide Show Mode On")
        pyautogui.press("f5")
        time.sleep(1)
    elif gesture == 5:
        print("Slide Show Mode Off")
        pyautogui.press("esc")
    elif gesture == 3:
        print("Switch to Next Slide")
        pyautogui.hotkey("right")
        time.sleep(0.5)
    elif gesture == 4:
        print("Switch to Previous Slide")
        pyautogui.hotkey("left")
        time.sleep(0.5)

