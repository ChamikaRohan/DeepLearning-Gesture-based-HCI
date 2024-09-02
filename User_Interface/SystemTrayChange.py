
# Static gestures
def TraySelection(gesture_type,mode,application):
    
    #Gesture type : 1-Static Gestures 2-Dynamic Gestures
    if gesture_type == 1:
        # Manual mode
        if mode == 1:
            if application == 0:
                n = 3
            if application == 1:
                n = 5
            if application == 2:
                n = 1
            if application == 3:
                n = 0
            if application == 4:
                n = 2
            if application == 5:
                n = 6
            if application == 6:
                n = 7
            if application == 7:
                n = 7

        # Automode
        if mode == 2:
            if application == 0:
                n = 3
                
            #No application
            if application == 1:
                n = 4
            if application == 2:
                n = 5
            if application == 3:
                n = 1
            if application == 4:
                n = 0
            if application == 5:
                n = 2
            if application == 6:
                n = 6
            if application == 7:
                n = 7

    if gesture_type == 2:
        # Manual mode
        if mode == 1:
            if application == 0:
                n = 12
            if application == 1:
                n = 11
            if application == 2:
                n = 10
            if application == 3:
                n = 9
            if application == 4:
                n = 13
            if application == 5:
                n = 14
            if application == 6:
                n = 7
            if application == 7:
                n = 7

        # Automode
        if mode == 2:
            if application == 0:
                n = 12
                
            #No application
            if application == 1:
                n = 8
            if application == 2:
                n = 11
            if application == 3:
                n = 10
            if application == 4:
                n = 9
            if application == 5:
                n = 13
            if application == 6:
                n = 14
            if application == 7:
                n = 7

    return n



