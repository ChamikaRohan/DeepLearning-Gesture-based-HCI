import sys

from Application_Actions.MediaPlayer_dynamic import dynamic_control_media_player
from Application_Actions.Presentation_dynamic import dynamic_control_presentation
from Application_Actions.Reading_dynamic import dynamic_control_reading
from Application_Actions.Zoom_dynamic import dynamic_control_zoom
from Application_Actions.Youtube_dynamic import dynamic_control_youtube
from Application_Actions.System_dynamic import dynamic_control_system

sys.path.append('../4_Voice_Assistance')
from Dynamic_switched_application_notifyer import dynamic_speak_application

sys.path.append('../10_Storage_and_utils')
from Payload import Payload

# Initialize Payload instance
payload = Payload()

def dynamic_select_function(argument, gestures):
    switcher = {
        0: dynamic_control_media_player,
        10: dynamic_control_media_player,
        11: dynamic_control_media_player,
        12: dynamic_control_media_player,
        13: dynamic_control_media_player,

        2: dynamic_control_system,
        18: dynamic_control_system,
        19: dynamic_control_system,
        20: dynamic_control_system,
        21: dynamic_control_system,

        3: dynamic_control_reading,
        22: dynamic_control_reading,
        23: dynamic_control_reading,
        24: dynamic_control_reading,
        25: dynamic_control_reading,

        4: dynamic_control_presentation,
        26: dynamic_control_presentation,
        27: dynamic_control_presentation,
        28: dynamic_control_presentation,
        29: dynamic_control_presentation,

        5: dynamic_control_youtube,
        30: dynamic_control_youtube,
        31: dynamic_control_youtube,
        32: dynamic_control_youtube,
        33: dynamic_control_youtube,

        6: dynamic_control_zoom,
        34: dynamic_control_zoom,
        35: dynamic_control_zoom,
        36: dynamic_control_zoom,
        37: dynamic_control_zoom,

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

def dynamic_orchestrator(gesture):
    # Access Payload properties for state and memory
    state = payload.get_state()
    memory = payload.get_memory()
    action = payload.get_action()

    print("Current dynamic action:", action)
    print("What memory has:", memory)

    if not state:
        if gesture is not None:
            if memory is not None:
                if gesture in (1, 14, 15, 16, 17):
                    payload.set_state(True)
                    payload.set_action(memory)
                    print("Successfully switched to application " + str(action))
                    dynamic_select_function(action, gesture)
                    dynamic_speak_application(action)
                else:
                    if gesture not in (1, 14, 15, 16, 17):
                        payload.set_action(None)
                        payload.set_memory(gesture)
                        payload.set_state(False)
                        print("Need 1 to confirm!")
            else:
                if gesture not in (1, 14, 15, 16, 17):
                    payload.set_memory(gesture)
                payload.set_action(None)
                payload.set_state(False)
        else:
            return
    else:
        if gesture is not None:
            dynamic_select_function(action, gesture)
            if gesture in (1, 14, 15, 16, 17):
                if memory is not None:
                    # undo_application(memory, action)  # Assuming this function is defined elsewhere
                    payload.set_state(False)
                    dynamic_orchestrator(gesture)
                    print("Switching to new application...........")
            if gesture not in (1, 14, 15, 16, 17):
                payload.set_memory(gesture)
