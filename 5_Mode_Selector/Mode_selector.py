import sys
sys.path.append('../4_Voice_Assistance')
from Switched_mode_notifyer import speak_mode
def mode_selector():
    print("Please choose a mode:")
    print("1. Manual Mode")
    print("2. Auto Mode")
    mode = int(input("Enter your choice (1 or 2): "))
    speak_mode(mode)
    return mode
