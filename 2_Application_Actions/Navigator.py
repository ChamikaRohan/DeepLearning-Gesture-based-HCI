from MediaPlayer import control_media_player
from Presentation import control_presentation
from System import control_system
from Reading import control_reading
from Youtube import control_youtube
import sys

sys.path.append('../2_Application_Actions/utils')
from Button_press_checker import check_backtick_pressed

def select_function(argument, gestures):
    switcher = {
        0: control_media_player,
        1: control_system,
        2: control_reading,
        3: control_presentation,
        4: control_youtube
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, default_function)
    # Execute the function with the provided gestures argument
    return func(gestures)

def default_function(gesture):
    print("Invalid action called!")

state = False
choice = None
def navigator(gesture):
    global state, choice
    if(state == False):
        print("Please select an application to control:")
        print("0: Media Player")
        print("1: System")
        print("2: Reading")
        print("3: Presentation")
        print("4: Youtube")
        choice = int(input("Enter the number corresponding to the application: ").strip())
        state = True
    else:
        select_function(choice, gesture)
