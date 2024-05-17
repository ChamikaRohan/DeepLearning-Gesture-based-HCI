import pyautogui
from Utils.Focus_on_window import focus_on_window
import time

"""
Function to control media player

Gesture Mapping:
Gesture 0: Play/Stop the movie
Gesture 4: Volume Increased
Gesture 2: Volume Decreased
Gesture 3: Switch to full-screen mode
Gesture 6: Seek forward
Gesture 7: Seek backward
Gesture 5: Take a screenshot
"""
def control_media_player(gesture):
    #Find and activae the movie player window
    window_titles = ["Movies", "VLC media player"]
    for title in window_titles:
        focus_on_window(title)
    if gesture == None:
        return
    elif gesture == 0:
        pyautogui.press("space")
        print("Play/Stop the movie")
        time.sleep(1)
    elif gesture == 4:
        pyautogui.scroll(1)
        print("Volume Increased")
    elif gesture == 2:
        pyautogui.scroll(-1)
        print("Volume Decreased")
    elif gesture == 3:
        pyautogui.press("f")
        print("Switch to full-screen mode")
        time.sleep(1)
    elif gesture == 6:
        pyautogui.keyDown('ctrl')
        pyautogui.press('right')
        pyautogui.keyUp('ctrl')
        print("Seeking Forward")
    elif gesture == 7:
        pyautogui.keyDown('ctrl')
        pyautogui.press('left')
        pyautogui.keyUp('ctrl')
        print("Seeking Backward")
    elif gesture == 5:
        print("Taking a screenshot")
        pyautogui.hotkey("winleft", "printscreen")
        time.sleep(1)
