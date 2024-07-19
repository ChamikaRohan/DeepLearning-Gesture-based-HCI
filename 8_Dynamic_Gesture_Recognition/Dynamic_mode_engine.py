import sys

from Dynamic_Orchestrator import dynamic_orchestrator
from Dynamic_Navigator import dynamic_navigator

def dynamic_engine(argument, gestures):
    switcher = {
        1: dynamic_navigator,
        2: dynamic_orchestrator,
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, dynamic_default_function)
    # Execute the function with the provided gestures argument
    return func(gestures)

def dynamic_default_function(gesture):
    print("Invalid dynamic action called!")