import sys

sys.path.append('../4_Voice_Assistance')
from Switched_application_notifyer import speak_application

memory = None
state = False
action =None

def dynamic_select_function(argument, gestures):
    switcher = {
        10: dynamic_control_media_player,
        12: dynamic_default_function,
        13: dynamic_default_function,
        14: dynamic_default_function,
        15: dynamic_default_function,
        16: dynamic_default_function,
        17: dynamic_default_function,
        18: dynamic_default_function,
        19: dynamic_default_function
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, dynamic_default_function)
    # Execute the function with the provided gestures argument
    return func(gestures)

def dynamic_default_function(gesture):
    print("Invalid dynamic action called!")

def dynamic_orchestrator(gesture):
    global memory, state, action

    print("Current dynamic action:", action)
    print("What memory has:", memory)

    if state == False:
        if gesture is not None:
            if memory is not None:
                if gesture == 1:
                    state = True
                    action = memory
                    print("Successfully switched to application "+ str(action))
                    dynamic_select_function(action, gesture)
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
            dynamic_select_function(action, gesture)
            if gesture ==1:
                if memory is not None:
                    #undo_application(memory, action)
                    state = False
                    dynamic_orchestrator(gesture)
                    print("Switching to new application...........")
            if gesture != 1:
                memory =  gesture