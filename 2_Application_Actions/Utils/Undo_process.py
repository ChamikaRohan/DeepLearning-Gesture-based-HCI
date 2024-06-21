import pyautogui

def undo_application(side_effected_gesture, application):
    if application == 0:
        if side_effected_gesture == 0:
            #Play/Stop
            print("Undo operation is not needed")
        elif side_effected_gesture == 4:
            #Decrease system volume
            pyautogui.scroll(-1)
            print("Undo performed: System Volume Decreased")
        elif side_effected_gesture == 2:
            #Increase system volume
            pyautogui.scroll(1)
            print("Undo performed: System Volume Increased")
        elif side_effected_gesture == 3:
            #Assuming user on nomral screen mode -> undo going to full screen mode
            pyautogui.press("f")
            print("Undo performed: Escaped from full screen mode")
        elif side_effected_gesture == 6:
            #Seeking Forward
            pyautogui.keyDown('ctrl')
            pyautogui.press('left')
            pyautogui.keyUp('ctrl')
            print("Undo performed: Seeking Backward")
        elif side_effected_gesture == 7:
            #Seeking Backward
            pyautogui.keyDown('ctrl')
            pyautogui.press('right')
            pyautogui.keyUp('ctrl')
            print("Undo performed: Seeking Forward")
        if side_effected_gesture == 5:
            print("Undo operation is not possible")

    elif application == 2:
        if side_effected_gesture == 5:
            print("Undo operation is not possible")
        elif side_effected_gesture == 3:
            #Simulate undoing Alt+Tab (reverse tabbing order)
            pyautogui.keyDown('shift')
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')
            pyautogui.keyUp('shift')
            print("Undo performed: Reverse tabbing order")
        elif side_effected_gesture == 4:
            pyautogui.hotkey('volumedown')
            print("Undo performed: Decrease System Volume")
        elif side_effected_gesture == 0:
            pyautogui.hotkey('volumeup')
            print("Undo performed: Increase System Volume")
        elif side_effected_gesture == 2:
            #Activate sleep mode
            print("Undo operation is not needed")
        elif side_effected_gesture == 6:
            #Open Task Manager
            pyautogui.hotkey("alt", "f4")
            print("Undo performed: Closed Task Manager")
        # elif side_effected_gesture == 7:
            # Yet to develop a method to cancel voice commands anytime

    elif application == 4:
        if side_effected_gesture == 0:
            pyautogui.press("esc")
            print("Undo performed: Escaped from slide show mode")
        elif side_effected_gesture == 3:
            pyautogui.hotkey("left")
            print("Undo performed: Switch to Previous Slide")
        elif side_effected_gesture == 4:
            pyautogui.hotkey("right")
            print("Undo operation is not needed")

    elif application == 3:
        if side_effected_gesture == 4:
            pyautogui.scroll(80)
            for _ in range(10):
                pyautogui.scroll(50)
            print("Undo performed: Scrolling up")
        elif side_effected_gesture == 0:
            pyautogui.scroll(-80)
            for _ in range(10):
                pyautogui.scroll(-50)
            print("Undo performed: Scrolling down")
        elif side_effected_gesture == 3:
            print("Undo operation is not needed")
        elif side_effected_gesture == 2:
            pyautogui.hotkey("ctrl", "+")
            print("Undo performed: Zooming in")
        elif side_effected_gesture == 5:
            # Assuming user on nomral screen mode -> undo going to full screen mode
            pyautogui.hotkey("f11")
            print("Undo performed: Exit from full screen mode")
        # elif side_effected_gesture == 7:
        #     Yet to develop a method to cancel voice commands anytime

    elif application == 5:
        if side_effected_gesture == 4:
            pyautogui.scroll(80)
            for _ in range(10):
                pyautogui.scroll(50)
            print("Undo performed: Scrolling up")
        elif side_effected_gesture == 0:
            pyautogui.scroll(-80)
            for _ in range(10):
                pyautogui.scroll(-50)
            print("Undo performed: Scrolling down")
        # elif side_effected_gesture == 3:
        #     Yet to develop a method to cancel voice commands anytime
        elif side_effected_gesture == 2:
            pyautogui.press("f")
        elif side_effected_gesture == 5:
            print("Undo operation is not needed")
        elif side_effected_gesture == 6:
            # Assuming video already stopped -> undo starting to play video
            pyautogui.press('space')
            print("Undo performed: Stop video")
        elif side_effected_gesture == 7:
            print("Undo operation is not possible")

    else:
        print("No application to undo")