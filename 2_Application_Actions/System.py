import pyautogui
from Utils.Focus_on_window import focus_on_window
from Utils.Powerpoint_mode_checker import is_fullscreen_mode
import time

# Global variable to store the previous hand position
previous_position = pyautogui.position()

"""
Function to control system functionalities

Gesture Mapping:
0: Go to previous slide (left)
4: Go to next slide (right)
2: Enter slide show mode
3: Exit slide show mode
"""
def control_system(gesture):
    if gesture == None:
        return
    elif gesture == 5:
        print("Taking a screenshot")
        pyautogui.hotkey("winleft", "printscreen")
        time.sleep(1)
    elif gesture == 3:
        print("Switch between applications")
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
    if gesture == 4:
        print("Scrolling down")
        pyautogui.scroll(-80)
        for _ in range(10):
            pyautogui.scroll(-50)
    elif gesture == 0:
        print("Scrolling up")
        pyautogui.scroll(80)
        for _ in range(10):
            pyautogui.scroll(50)
    # elif gesture == 2:
    #     print("Activate sleep mode")
    #     pyautogui.hotkey("winleft", "x")
    #     pyautogui.typewrite("u")
    #     pyautogui.typewrite("s")

