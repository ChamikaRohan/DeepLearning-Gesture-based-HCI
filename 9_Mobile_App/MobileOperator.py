import sys

sys.path.append('../10_Storage_and_utils')
from Payload import Payload

sys.path.append('../2_Application_Actions/Utils')
from Current_application_checker import get_active_application

from Mobile_Application_Actions.Mobile_media_player import mobile_control_media_player
from Mobile_Application_Actions.Mobile_presentation import mobile_control_presentation
from Mobile_Application_Actions.Mobile_reading import mobile_control_reading
from Mobile_Application_Actions.Mobile_system import mobile_control_system
from Mobile_Application_Actions.Mobile_youtube import mobile_control_youtube
from Mobile_Application_Actions.Mobile_zoom import mobile_control_zoom

def select_function(argument, gestures):
    switcher = {
        0: mobile_control_media_player,
        1: mobile_control_system,
        2: mobile_control_reading,
        3: mobile_control_presentation,
        4: mobile_control_youtube,
        5: mobile_control_zoom,
        6: default_function,
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

def mobileoperator(action):
    active_application = get_active_application()
    if active_application is not None:
        select_function(active_application, action)
