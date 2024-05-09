import keyboard
import time

def check_backtick_pressed(timeout=0.5):
    start_time = time.time()
    while True:
        if keyboard.is_pressed('`'):
            return True
        if time.time() - start_time >= timeout:
            return False