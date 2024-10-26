import time

import sys

from Application_Actions.MediaPlayer_dynamic import dynamic_control_media_player
from Application_Actions.Presentation_dynamic import dynamic_control_presentation
from Application_Actions.Reading_dynamic import dynamic_control_reading
from Application_Actions.Zoom_dynamic import dynamic_control_zoom
from Application_Actions.Youtube_dynamic import dynamic_control_youtube
from Application_Actions.System_dynamic import dynamic_control_system

sys.path.append('../2_Application_Actions/Utils')
from Current_application_checker import get_active_application

sys.path.append('../10_Storage_and_utils')
from Payload import Payload

def dynamic_select_function(argument, gestures):
    switcher = {
        0: dynamic_control_media_player,
        1: dynamic_control_system,
        2: dynamic_control_reading,
        3: dynamic_control_presentation,
        4: dynamic_control_youtube,
        5: dynamic_control_zoom,
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
    print("Inside tha navigator")
    payload = Payload()
    if gesture is not None:
        print("Calling the function for active application")
        active_application = get_active_application()
        print("Active application is :", active_application)
        if active_application is not None:
            print("Switching to the application")
            payload.set_application(active_application)
            dynamic_select_function(active_application, gesture)

    return
