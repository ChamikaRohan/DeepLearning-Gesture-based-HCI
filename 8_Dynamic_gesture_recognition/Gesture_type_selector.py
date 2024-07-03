import sys
sys.path.append('../4_Voice_Assistance')
from Switched_mode_notifyer import speak_mode
def gesture_type_selector():
    print("Welcome! Please choose the preferred gesture type:")
    print("1. Static Gestures")
    print("2. Dynamic Gestures")
    gesture_type = int(input("Enter your choice (1 or 2): "))
    #speak_mode(mode)
    return gesture_type
