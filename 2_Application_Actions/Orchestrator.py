from MediaPlayer import control_media_player
from Presentation import control_presentation

memory = None
state = False
action =None

def select_function(argument, gestures):
    switcher = {
        0: default_function,
        2: control_media_player,
        3: control_presentation,
        4: default_function,
        5: default_function
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, default_function)
    # Execute the function with the provided gestures argument
    return func(gestures)

def default_function(gesture  ):
    print("Invalid action called!")

def orchestrator(gesture):
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
                    select_function(action, gesture  )
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
            if gesture ==1:
                if memory is not None:
                    state = False
                    orchestrator(gesture)
                    print("Switching to new application...........")
            if gesture != 1:
                memory =  gesture

