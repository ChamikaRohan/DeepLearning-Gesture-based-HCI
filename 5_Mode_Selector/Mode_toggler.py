import sys
sys.path.append('../4_Voice_Assistance')
from Switched_mode_notifyer import speak_mode

def mode_toggler(mode):
    if mode == 1:
        mode = 2
    elif mode == 2:
        mode = 1
    speak_mode(mode)
    return mode