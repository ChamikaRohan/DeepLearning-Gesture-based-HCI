import pyautogui
import time
from FocusOnWindow import focus_on_window

"""
Function to control presentation slides

Gesture Mapping:
0: Go to previous slide (left)
4: Go to next slide (right)
2: Enter slide show mode
3: Exit slide show mode
"""
def control_presentation(gesture):
    # Find the active window
    window_titles = ["PowerPoint"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        print("None")
    elif gesture == 0:
        # Go to previous slide
        print("Go to Previous Slide")
        pyautogui.hotkey("left")
    elif gesture == 4:
        # Go to next slide
        print("Go to Next Slide")
        pyautogui.hotkey("right")
    elif gesture == 2:
        # Enter full screen mode
        print("Enter Slide Show Mode")
        pyautogui.press("f5")
    elif gesture == 3:
        # Exit full screen mode
        print("Exit Slide Show Mode")
        pyautogui.press("esc")

