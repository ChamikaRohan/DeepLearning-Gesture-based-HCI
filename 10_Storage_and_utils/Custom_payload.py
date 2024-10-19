class CustomPayload:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CustomPayload, cls).__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if not self.__initialized:
            # Dictionary to store data for each gesture number
            self._gestures = {}
            self.__initialized = True

    def set_gesture_data(self, gesture_number, action_type=None, press_val=None,
                         hotKey_val_1=None, hotKey_val_2=None, hotKey_val_3=None,
                         scroll_val=None):
        """Store data for a specific gesture number."""
        self._gestures[gesture_number] = {
            "action_type": action_type,
            "press_val": press_val,
            "hotKey_val_1": hotKey_val_1,
            "hotKey_val_2": hotKey_val_2,
            "hotKey_val_3": hotKey_val_3,
            "scroll_val": scroll_val
        }

    def get_gesture_data(self, gesture_number):
        """Retrieve data for a specific gesture number."""
        return self._gestures.get(gesture_number, {})

    def remove_gesture_data(self, gesture_number):
        """Remove data for a specific gesture number."""
        if gesture_number in self._gestures:
            del self._gestures[gesture_number]

    def get_all_gestures(self):
        """Get all stored gesture data."""
        return self._gestures

    def get_all_gestures(self):
        """Get all stored gesture data."""
        return self._gestures

    def get_action_specific_data(self):
        """Return action-specific values for all gestures, including action type."""
        all_gesture_data = {}

        for gesture_number, gesture_data in self._gestures.items():
            action_type = gesture_data.get("action_type")
            action_data = {"action_type": action_type}  # Include action type

            if action_type == "Press":
                action_data["press_val"] = gesture_data.get("press_val")

            elif action_type == "HotKey":
                action_data["hotKey_val_1"] = gesture_data.get("hotKey_val_1")
                action_data["hotKey_val_2"] = gesture_data.get("hotKey_val_2")
                action_data["hotKey_val_3"] = gesture_data.get("hotKey_val_3")

            elif action_type == "Scroll":
                action_data["scroll_val"] = gesture_data.get("scroll_val")

            all_gesture_data[gesture_number] = action_data  # Store data with gesture number

        return all_gesture_data
