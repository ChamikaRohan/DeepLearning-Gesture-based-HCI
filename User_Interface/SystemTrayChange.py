
# Static gestures
def TraySelection(gesture_type,mode,application):
    print("I am called...")
    #Gesture type : 1-Static Gestures 2-Dynamic Gestures
    if gesture_type == 1:
        # Manual mode
        if mode == 1:
            if application == 0:
                n = 3
            elif application == 1:
                n = 5
            elif application == 2:
                n = 1
            elif application == 3:
                n = 0
            elif application == 4:
                n = 2
            elif application == 5:
                n = 6
            elif application == 6:
                n = 7
            elif application == 7:
                n = 7

        # Automode
        if mode == 2:
            if application == 0:
                n = 3
                
            #No application
            elif application == 1:
                n = 4
            elif application == 2:
                n = 5
            elif application == 3:
                n = 1
            elif application == 4:
                n = 0
            elif application == 5:
                n = 2
            elif application == 6:
                n = 6
            elif application == 7:
                n = 7
            else:
                n = 4


    if gesture_type == 2:
        print("Im called from manual")
        # Manual mode
        if mode == 1:
            if application == 0:
                n = 12
            elif application == 1:
                n = 11
            elif application == 2:
                n = 10
            elif application == 3:
                n = 9
            elif application == 4:
                n = 13
            elif application == 5:
                n = 14
            elif application == 6:
                n = 7
            elif application == 7:
                n = 7

        # Automode
        if mode == 2:
            if application in [0, 10, 11, 12, 13]:
                n = 12
            elif application == 1:
                n = 8
            elif application in [2, 18, 19, 20, 21]:
                n = 11
            elif application in [3, 22, 23, 24, 25]:
                n = 10
            elif application in [4, 26, 27, 28, 29]:
                n = 9
            elif application in [5, 30, 31, 32, 33]:
                n = 13
            elif application in [6, 34, 35, 36, 37]:
                n = 14
            else:
                n = 8

    return n


def Auto_Manual_Selection(mode):
    # mode : 1-Manual 2-Auto
    if (mode == 1):
        x = False
    if (mode == 2):
        x = True

    return x


def Dynamic_Static_Selection(gesture):
    # Gesture type : 1-Static Gestures 2-Dynamic Gestures
    if (gesture == 1):
        x = True
    if (gesture == 2):
        x = False

    return x



