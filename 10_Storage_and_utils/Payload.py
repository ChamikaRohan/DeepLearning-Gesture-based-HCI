class Payload:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Payload, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, first_gray=None, gesture_type=None, mode=None, model_path=None, gesture_frames=None, direction_frames=None):
        if not self.__initialized:
            self._first_gray = first_gray
            self._gesture_type = gesture_type
            self._mode = mode
            self._model_path = model_path
            self._gesture_frames = gesture_frames
            self._direction_frames = direction_frames
            self.__initialized = True

    # Getter and Setter for first_gray
    def get_first_gray(self):
        return self._first_gray

    def set_first_gray(self, first_gray):
        self._first_gray = first_gray

    # Getter and Setter for gesture_type
    def get_gesture_type(self):
        return self._gesture_type

    def set_gesture_type(self, gesture_type):
        self._gesture_type = gesture_type

    # Getter and Setter for mode
    def get_mode(self):
        return self._mode

    def set_mode(self, mode):
        self._mode = mode

    # Getter and Setter for model_path
    def get_model_path(self):
        return self._model_path

    def set_model_path(self, model_path):
        self._model_path = model_path

    # Getter and Setter for gesture_frames
    def get_gesture_frames(self):
        return self._gesture_frames

    def set_gesture_frames(self, gesture_frames):
        self._gesture_frames = gesture_frames

    # Getter and Setter for direction_frames
    def get_direction_frames(self):
        return self._direction_frames

    def set_direction_frames(self, direction_frames):
        self._direction_frames = direction_frames



# class Payload:
#     def __init__(self, first_gray=None, gesture_type=None, mode=None, model_path=None, gesture_frames=None, direction_frames=None):
#         self._first_gray = first_gray
#         self._gesture_type = gesture_type
#         self._mode = mode
#         self._model_path = model_path
#         self._gesture_frames = gesture_frames
#         self._direction_frames = direction_frames
#
#     # Getter and Setter for first_gray
#     def get_first_gray(self):
#         return self._first_gray
#
#     def set_first_gray(self, first_gray):
#         self._first_gray = first_gray
#
#     # Getter and Setter for gesture_type
#     def get_gesture_type(self):
#         return self._gesture_type
#
#     def set_gesture_type(self, gesture_type):
#         self._gesture_type = gesture_type
#
#     # Getter and Setter for mode
#     def get_mode(self):
#         return self._mode
#
#     def set_mode(self, mode):
#         self._mode = mode
#
#     # Getter and Setter for model_path
#     def get_model_path(self):
#         return self._model_path
#
#     def set_model_path(self, model_path):
#         self._model_path = model_path
#
#     # Getter and Setter for gesture_frames
#     def get_gesture_frames(self):
#         return self._gesture_frames
#
#     def set_gesture_frames(self, gesture_frames):
#         self._gesture_frames = gesture_frames
#
#     # Getter and Setter for direction_frames
#     def get_direction_frames(self):
#         return self._direction_frames
#
#     def set_direction_frames(self, direction_frames):
#         self._direction_frames = direction_frames



"""
# Example usage
payload = Payload()
payload2 = Payload()

# Set values
payload.set_first_gray("gray_value")
payload.set_gesture_type("swipe")
payload.set_mode("training")
payload2.set_model_path("path/to/model")
payload.set_gesture_frames(30)
payload.set_direction_frames(10)

# Get values
print(payload.get_first_gray())  # Output: gray_value
print(payload.get_gesture_type())  # Output: swipe
print(payload.get_mode())  # Output: training
print(payload2.get_model_path())  # Output: path/to/model
print(payload.get_gesture_frames())  # Output: 30
print(payload.get_direction_frames())  # Output: 10

print(payload2.get_first_gray())  # Output: gray_value
print(payload2.get_gesture_type())  # Output: swipe
print(payload2.get_mode())  # Output: training
print(payload.get_model_path())  # Output: path/to/model
"""

"""
payload = Payload(
        first_gray="fgfg",
        gesture_type="fhfhfh",
        mode="fdgfdfdgfdg",
        model_path="../1_Model_Binding/Media/10_gesture_model_25th_attempt.h5",
        gesture_frames={0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0},
        direction_frames="fdgfgfg")

print(payload.get_model_path())
"""