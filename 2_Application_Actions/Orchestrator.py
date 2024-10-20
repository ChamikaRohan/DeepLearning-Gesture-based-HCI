import sys
from MediaPlayer import control_media_player
from Presentation import control_presentation
from System import control_system
from Reading import control_reading
from Youtube import control_youtube
from Zoom import control_zoom
from Custom_application import control_custom_application

from Utils.Undo_process import undo_application

sys.path.append('../4_Voice_Assistance')
from Switched_application_notifyer import speak_application

memory = None
state = False
action =None

sys.path.append('../10_Storage_and_utils')
from Payload import Payload

def select_function(argument, gestures):
    switcher = {
        0: control_media_player,
        2: control_system,
        3: control_reading,
        4: control_presentation,
        5: control_youtube,
        6: control_zoom,
        7: control_custom_application,
        8: default_function,
        9: default_function
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, default_function)
    # Execute the function with the provided gestures argument
    return func(gestures)

def default_function(gesture):
    print("Invalid action called!")

def orchestrator(gesture):
    payload = Payload()
    global memory, state, action

    print("Current action:", action)
    print("What memory has:", memory)

    if state == False:
        if gesture is not None:
            if memory is not None:
                if gesture == 1:
                    state = True
                    action = memory
                    print("Successfully switched to to application "+ str(action))
                    select_function(action, gesture)
                    payload.set_application(action)
                    speak_application(action)
                else:
                    if gesture != 1:
                        action = None
                        memory = gesture
                        state = False
                        print("Need 1 to confirm!")
            else:
                if gesture != 1:
                    memory = gesture
                action = None
                state = False
        else:
            return
    else:
        if gesture is not None:
            select_function(action, gesture)
            payload.set_application(action)
            if gesture ==1:
                if memory is not None:
                    undo_application(memory, action)
                    state = False
                    orchestrator(gesture)
                    print("Switching to new application...........")
            if gesture != 1:
                memory =  gesture