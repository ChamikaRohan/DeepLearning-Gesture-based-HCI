import traceback

class Payload:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Payload, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self, first_gray=None, gesture_type=None, mode=None, model_path=None, gesture_frames=None, direction_frames=None, custom_config_path=None, hand_window_status=None, application=None):
        if not self.__initialized:
            self._first_gray = first_gray
            self._gesture_type = gesture_type
            self._mode = mode
            self._model_path = model_path
            self._gesture_frames = gesture_frames
            self._direction_frames = direction_frames
            self._custom_config_path = custom_config_path
            self._hand_window_status = hand_window_status
            self._application = application
            self.is_first_time_gesture_type = True
            self.is_first_time_mode = True
            self.__initialized = True

    # Getter and Setter for first_gray
    def get_first_gray(self):
        return self._first_gray

    def set_first_gray(self, first_gray):
        self._first_gray = first_gray

    # Getter and Setter for gesture_type with change tracking and stack trace
    def get_gesture_type(self):
        return self._gesture_type

    def set_gesture_type(self, gesture_type):
        if self._gesture_type != gesture_type:
            print(f"gesture_type changed from {self._gesture_type} to {gesture_type}")
            print("Stack trace where change occurred:")
            traceback.print_stack(limit=3)  # Print a short stack trace
        self._gesture_type = gesture_type

    # Getter and Setter for mode with change tracking and stack trace
    def get_mode(self):
        return self._mode

    def set_mode(self, mode):
        if self._mode != mode:
            print(f"mode changed from {self._mode} to {mode}")
            print("Stack trace where change occurred:")
            traceback.print_stack(limit=3)  # Print a short stack trace
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

    # Getter and Setter for custom_config_path
    def get_custom_config_path(self):
        return self._custom_config_path

    def set_custom_config_path(self, custom_config_path):
        self._custom_config_path = custom_config_path

    # Getter and Setter for hand_window_status
    def get_hand_window_status(self):
        return self._hand_window_status

    def set_hand_window_status(self, hand_window_status):
        self._hand_window_status = hand_window_status

    # Getter and Setter for application (New attribute)
    def get_application(self):
        return self._application

    def set_application(self, application):
        self._application = application
