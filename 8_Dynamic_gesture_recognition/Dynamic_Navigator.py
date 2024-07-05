import time

import sys

from Application_Actions.MediaPlayer_dynamic import dynamic_control_media_player
from Application_Actions.Presentation_dynamic import dynamic_control_presentation
from Application_Actions.Reading_dynamic import dynamic_control_reading

sys.path.append('../2_Application_Actions/Utils')
from Current_application_checker import get_active_application

def dynamic_select_function(argument, gestures):
    switcher = {
        0: dynamic_control_media_player,
        1: dynamic_default_function,
        2: dynamic_control_reading,
        3: dynamic_control_presentation,
        4: dynamic_default_function,
        5: dynamic_default_function,
        6: dynamic_default_function,
        7: dynamic_default_function,
        8: dynamic_default_function,
        9: dynamic_default_function
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, dynamic_default_function)
    # Execute the function with the provided gestures argument
    return func(gestures)

def dynamic_default_function(gesture):
    print("Invalid dynamic action called!")

def dynamic_navigator(gesture):
    print("inside tha navigator")
    if gesture is not None:
        print("calling the function for active application")
        active_application = get_active_application()
        print("active application is :", active_application)
        if active_application is not None:
            dynamic_select_function(active_application, gesture)
            print("Switching to the application")

    return
