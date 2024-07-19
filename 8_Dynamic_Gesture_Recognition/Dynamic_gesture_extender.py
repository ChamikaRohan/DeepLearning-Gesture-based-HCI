gesture_map = {
    0: 'Gesture Palm',
    1: 'Gesture Thumbs Up',
    2: 'Gesture Rock',
    3: 'Gesture Thumbs Left',
    4: 'Gesture V',
    5: 'Gesture L',
    6: 'Gesture Swag',
    7: 'Gesture C',
    8: 'Gesture Three Fingers',
    9: 'Gesture Scissor'
}

# Extended gesture map for combinations
extended_gesture_map = {
    (0, 'Static'): 0,
    (0, 'Left'): 10,
    (0, 'Right'): 11,
    (0, 'Up'): 12,
    (0, 'Down'): 13,
    (1, 'Static'): 1,
    (1, 'Left'): 14,
    (1, 'Right'): 15,
    (1, 'Up'): 16,
    (1, 'Down'): 17,
    (2, 'Static'): 2,
    (2, 'Left'): 18,
    (2, 'Right'): 19,
    (2, 'Up'): 20,
    (2, 'Down'): 21,
    (3, 'Static'): 3,
    (3, 'Left'): 22,
    (3, 'Right'): 23,
    (3, 'Up'): 24,
    (3, 'Down'): 25,
    (4, 'Static'): 4,
    (4, 'Left'): 26,
    (4, 'Right'): 27,
    (4, 'Up'): 28,
    (4, 'Down'): 29,
    (5, 'Static'): 5,
    (5, 'Left'): 30,
    (5, 'Right'): 31,
    (5, 'Up'): 32,
    (5, 'Down'): 33,
    (6, 'Static'): 6,
    (6, 'Left'): 34,
    (6, 'Right'): 35,
    (6, 'Up'): 36,
    (6, 'Down'): 37,
    (7, 'Static'): 7,
    (7, 'Left'): 38,
    (7, 'Right'): 39,
    (7, 'Up'): 40,
    (7, 'Down'): 41,
    (8, 'Static'): 8,
    (8, 'Left'): 42,
    (8, 'Right'): 43,
    (8, 'Up'): 44,
    (8, 'Down'): 45,
    (9, 'Static'): 9,
    (9, 'Left'): 46,
    (9, 'Right'): 47,
    (9, 'Up'): 48,
    (9, 'Down'): 49
}

def combined_gesture_number_finder(intended_gesture, intended_direction):
    if intended_gesture is None:
        return None

    #Check if the combination exists in the extended map
    combined_gesture = (intended_gesture, intended_direction)
    if combined_gesture in extended_gesture_map:
        return extended_gesture_map[combined_gesture]

    #Return none if no combination exists
    return None
