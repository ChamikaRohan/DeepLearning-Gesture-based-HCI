import pyautogui
import time

"""
Function to control presentation slides

Gesture Mapping:
0: Go to previous slide (left)
1: Go to next slide (right)
2: Enter slide show mode
3: Exit slide show mode
"""
def control_presentation(gesture):
    if gesture == 0:
        # Go to previous slide
        print("Go to Previous Slide")
        pyautogui.hotkey("left")
    elif gesture == 1:
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
    time.sleep(1)  # Add a small delay after each action

