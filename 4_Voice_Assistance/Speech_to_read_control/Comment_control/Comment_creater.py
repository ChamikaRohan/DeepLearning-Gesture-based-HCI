import time
import pyautogui
import sys

sys.path.append('../4_Voice_Assistance')
from Speech_to_text_generator import speech_to_text

def comment_creater(text):
    text = text.lower();
    if text == "top left":
        pyautogui.click(358, 153)
        pyautogui.click(500, 245)
        comment=speech_to_text()
        pyautogui.typewrite(comment, interval=0.1)
        pyautogui.press('esc')
        pyautogui.press('esc')

    elif text == "top right":
        pyautogui.click(358, 153)
        pyautogui.click(1130, 245)
        comment=speech_to_text()
        pyautogui.typewrite(comment, interval=0.1)
        pyautogui.press('esc')
        pyautogui.press('esc')

    elif text == "bottom left":
        pyautogui.click(358, 153)
        pyautogui.click(500, 920)
        comment=speech_to_text()
        pyautogui.typewrite(comment, interval=0.1)
        pyautogui.press('esc')
        pyautogui.press('esc')

    elif text == "bottom right":
        pyautogui.click(358, 153)
        pyautogui.click(1070, 920)
        comment = speech_to_text()
        pyautogui.typewrite(comment, interval=0.1)
        pyautogui.press('esc')
        pyautogui.press('esc')

    elif text == "middle" or text == "center":
        pyautogui.click(358, 153)
        pyautogui.click(850, 595)
        comment = speech_to_text()
        pyautogui.typewrite(comment, interval=0.1)
        pyautogui.press('esc')
        pyautogui.press('esc')

