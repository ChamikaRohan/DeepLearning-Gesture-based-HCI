import time
import sys

from MediaPlayer import control_media_player
from Presentation import control_presentation
from System import control_system
from Reading import control_reading
from Youtube import control_youtube
from Zoom import control_zoom
from Custom_application import control_custom_application

sys.path.append('../2_Application_Actions/Utils')
from Current_application_checker import get_active_application

sys.path.append('../10_Storage_and_utils')
from Payload import Payload

def select_function(argument, gestures):
    switcher = {
        0: control_media_player,
        1: control_system,
        2: control_reading,
        3: control_presentation,
        4: control_youtube,
        5: control_zoom,
        6: control_custom_application,
        7: default_function,
        8: default_function,
        9: default_function
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, default_function)
    # Execute the function with the provided gestures argument
    return func(gestures)

def default_function(gesture):
    print("Invalid action called!")

def navigator(gesture):
    payload = Payload()
    print("inside tha navigator")
    if gesture is not None:
        print("calling the function for active applicattion")
        active_application = get_active_application()
        payload.set_application(active_application)
        print("active application is :", active_application)
        if active_application is not None:
            select_function(active_application, gesture)
            print("Switching to the application")

    return
