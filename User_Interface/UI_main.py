import sys
import cv2

from PyQt6.QtCore import Qt, QPoint,QTimer
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton, QButtonGroup, QSizeGrip
from PyQt6.QtGui import QIcon

import resources_rc
from User_Interface import *

sys.path.append('../10_Storage_and_utils')
from Payload import Payload

sys.path.append('../5_Mode_Selector')
from Mode_toggler import mode_toggler

sys.path.append('../1_Model_Binding')
from Utils.First_frame_getter import first_frame_getter

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set the window icon

        self.setWindowIcon(QIcon('Icons2/images/Logofyp.png'))

        self.switch_to_homePage()
        self.initialize_ui()

        # Hide the title bar
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # Make the window draggable
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.dragPosition = None

        self.ui.Restore_Button.clicked.connect(self.restore_or_maximize_window)
        self.ui.Home_Button.setChecked(True)

        self.ui.Library_Button_Container.setHidden(True)
        self.ui.Manual_Button_Container.setHidden(True)
        self.ui.More_Menu_Widget.setHidden(True)

        self.ui.Library_Button.clicked.connect(self.show_Library_Button_Container)
        self.ui.Manual_Button.clicked.connect(self.show_Manual_Button_Container)
        self.ui.Information_Button.clicked.connect(self.show_center_menu)
        self.ui.Settings_Button.clicked.connect(self.show_center_menu)
        self.ui.More_Menu_close_Button.clicked.connect(self.More_Menu_Remover)

        Custom_Page_Buttons = [
            self.ui.Palm_Button,
            self.ui.Palm_Button_2,
            self.ui.Rock_Button,
            self.ui.Rock_Button_2,
            self.ui.Thumbs_Left_Button,
            self.ui.Thumbs_Left_Button_2,
            self.ui.V_Button,
            self.ui.V_Button_2,
            self.ui.L_Button,
            self.ui.L_Button_2,
            self.ui.Swag_Button,
            self.ui.Swag_Button_2,
            self.ui.C_Button,
            self.ui.C_Button_2,
            self.ui.Three_Fingers_Button,
            self.ui.Three_Fingers_Button_2,
            self.ui.Scissors_Button,
            self.ui.Scissors_Button_2

        ]

        for button in Custom_Page_Buttons:
            button.clicked.connect(self.switch_to_addCustomActionTypePage)

        self.ui.Back_Button_Custom.clicked.connect(self.switch_to_CustomPage)
        self.ui.Action_Type_ComboBox.currentIndexChanged.connect(self.on_combo_box_changed)

        self.ui.Home_Button.clicked.connect(self.switch_to_homePage)
        self.ui.Manual_Button.clicked.connect(self.switch_to_ManualPage)
        self.ui.Library_Button.clicked.connect(self.switch_to_LibraryPage)
        self.ui.Custom_Button.clicked.connect(self.switch_to_CustomPage)

        self.ui.Information_Button.clicked.connect(self.switch_to_InformationPage)
        self.ui.Settings_Button.clicked.connect(self.switch_to_SettingsPage)
        self.ui.Application_Button.clicked.connect(self.switch_to_ApplicationsPage)
        self.ui.Gestures_Button.clicked.connect(self.switch_to_GesturesPage)
        self.ui.AutoMode_Button.clicked.connect(self.switch_to_AutoModePage)
        self.ui.ManualMode_Button.clicked.connect(self.switch_to_ManualModePage)
        self.ui.DynamicMode_Button.clicked.connect(self.switch_to_DynamicModePage)

        self.ui.UTube_Button.clicked.connect(self.switch_to_Page4)
        self.ui.Vlc_Button.clicked.connect(self.switch_to_Page1)
        self.ui.Zoom_Button.clicked.connect(self.switch_to_Page3)
        self.ui.System_Button.clicked.connect(self.switch_to_Page5)
        self.ui.Reading_Button.clicked.connect(self.switch_to_Page6)
        self.ui.Powerpoint_Button.clicked.connect(self.switch_to_Page2)

        self.ui.BackButton1.clicked.connect(self.switch_to_ApplicationsPage)
        self.ui.BackButton2.clicked.connect(self.switch_to_ApplicationsPage)
        self.ui.BackButton3.clicked.connect(self.switch_to_ApplicationsPage)
        self.ui.BackButton4.clicked.connect(self.switch_to_ApplicationsPage)
        self.ui.BackButton5.clicked.connect(self.switch_to_ApplicationsPage)
        self.ui.BackButton7.clicked.connect(self.switch_to_ApplicationsPage)

        self.ui.Previous_Button.clicked.connect(self.switch_to_DynamicGestures)
        self.ui.Next_Button.clicked.connect(self.switch_to_DynamicGesturePage2)

        self.ui.Static_Button2.setCheckable(True)
        self.ui.Static_Button1.setCheckable(True)
        self.ui.Dynamic_Button2.setCheckable(True)
        self.ui.Dynamic_Button1.setCheckable(True)
        self.ui.Custom_Button.setCheckable(True)



        self.ui.Static_Button2.clicked.connect(self.switch_to_StaticGestures)
        self.ui.Static_Button1.clicked.connect(self.switch_to_StaticGestures)
        self.ui.Dynamic_Button2.clicked.connect(self.switch_to_DynamicGestures)
        self.ui.Dynamic_Button1.clicked.connect(self.switch_to_DynamicGestures)

        self.ui.Static_Button3.clicked.connect(self.switch_to_StaticMode)
        self.ui.Dynamic_Button3.clicked.connect(self.switch_to_DynamicMode)

        self.ui.Static_Button4.clicked.connect(self.switch_to_StaticMode_Of_Auto_Mode)
        self.ui.Dynamic_Button4.clicked.connect(self.switch_to_DynamicMode_Of_Auto_Mode)

        self.ui.Start_Button.clicked.connect(self.switch_to_Start_Application)
        # self.ui.Start_Button.clicked.connect(self.start_backend_main_thread)
        self.ui.Stop_Button.clicked.connect(self.switch_to_Stop_Application)

        self.button_group = QButtonGroup(self)
        self.button_group.addButton(self.ui.Information_Button)
        self.button_group.addButton(self.ui.Settings_Button)
        self.button_group.setExclusive(True)



        # Connect minimize to tray button
        self.ui.Minimize_To_Tray_Button.clicked.connect(self.open_min_window)
        self.min_window = None

        QSizeGrip(self.ui.frame_4)

        self.ui.Select_HotKey1_ComboBox.setPlaceholderText("Enter Key 1")
        self.ui.Select_HotKey2_ComboBox.setPlaceholderText("Enter Key 2")
        self.ui.Select_HotKey3_ComboBox.setPlaceholderText("Enter Key 3")

        self.ui.Select_Key_ComboBox.setPlaceholderText("Enter Key")

        self.ui.Application_Name_Text.setPlaceholderText("Enter Application Name")

        #Binding
        self.ui.Auto_Mode_Button.toggled.connect(self.Switch_mode)
        self.ui.Auto_Mode_Button_2.toggled.connect(self.Switch_gesture_type)

    def Switch_mode(self):
        payload = Payload()
        current_mode = payload.get_mode()
        new_mode = mode_toggler(current_mode)
        payload.set_mode(new_mode)

    def Switch_gesture_type(self):
        payload = Payload()
        current_gesture_type = payload.get_gesture_type()
        new_gesture_type = mode_toggler(current_gesture_type)
        payload.set_gesture_type(new_gesture_type)

    def on_combo_box_changed(self, index):
        if index == 0:
            self.ui.Action_Types_Stacked_Widget.setCurrentIndex(0)
        elif index == 1:
            self.ui.Action_Types_Stacked_Widget.setCurrentIndex(1)
        elif index == 2:
            self.ui.Action_Types_Stacked_Widget.setCurrentIndex(2)

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def initialize_ui(self):
        self.resize(800, 540)
        self.setWindowTitle("MotionPilot")

    def switch_to_StaticGestures(self):
        self.ui.Static_Dynamic_Gesture__Stacked_Widget.setCurrentIndex(0)
        self.ui.Static_Button1.setChecked(True)

    def switch_to_DynamicGestures(self):
        self.ui.Static_Dynamic_Gesture__Stacked_Widget.setCurrentIndex(1)
        self.ui.Dynamic_Gestures_Stacked_Widget.setCurrentIndex(0)
        self.ui.Dynamic_Button2.setChecked(True)

    def switch_to_DynamicGesturePage2(self):
        self.ui.Static_Dynamic_Gesture__Stacked_Widget.setCurrentIndex(1)
        self.ui.Dynamic_Gestures_Stacked_Widget.setCurrentIndex(1)
        self.ui.Dynamic_Button2.setChecked(True)
    def switch_to_StaticMode(self):
        self.ui.Gesture_Modes_Stacked_Widget.setCurrentIndex(0)



    def switch_to_StaticMode_Of_Auto_Mode(self):
        self.ui.Auto_Mode_Static_Dynamic_Stacked_Widget.setCurrentIndex(0)
        self.ui.Static_Button4.setChecked(True)
    def switch_to_DynamicMode_Of_Auto_Mode(self):
        self.ui.Auto_Mode_Static_Dynamic_Stacked_Widget.setCurrentIndex(1)
        self.ui.Dynamic_Button4.setChecked(True)

    def switch_to_DynamicMode(self):
        self.ui.Gesture_Modes_Stacked_Widget.setCurrentIndex(1)


    def Remove_Button_Check(self):
        self.ui.More_Menu_Widget.setHidden(True)
        self.button_group.setExclusive(False)
        self.ui.Information_Button.setChecked(False)
        self.ui.Settings_Button.setChecked(False)
        self.button_group.setExclusive(True)
        self.ui.Main_Body_Widget.setFocus()

    def More_Menu_Remover(self):
        self.Remove_Button_Check()
        self.initialize_ui()

    def switch_to_Start_Application(self):
        self.ui.Start_Stacked_Widget.setCurrentIndex(1)

    def switch_to_Stop_Application(self):
        self.ui.Start_Stacked_Widget.setCurrentIndex(0)

    def switch_to_homePage(self):
        self.ui.Main_Body_Page_Stack.setCurrentIndex(0)
        self.ui.Start_Stacked_Widget.setCurrentIndex(0)
        self.ui.Manual_Button_Container.setHidden(True)
        self.ui.Library_Button_Container.setHidden(True)
        self.ui.Manual_Button.setChecked(False)
        self.ui.Custom_Button.setChecked(False)

    def switch_to_CustomPage(self):
        self.ui.Main_Body_Page_Stack.setCurrentIndex(2)
        self.ui.Custom_Stacked_Widget.setCurrentIndex(0)
        self.ui.Manual_Button_Container.setHidden(True)
        self.ui.Library_Button_Container.setHidden(True)
        self.ui.Manual_Button.setChecked(False)
        self.ui.Custom_Button.setChecked(True)
        self.ui.Gestures_Button.setChecked(False)
        self.ui.Application_Button.setChecked(False)


    def switch_to_LibraryPage(self):
        self.ui.Main_Body_Page_Stack.setCurrentIndex(3)
        self.ui.Library_Stacked_Widget.setCurrentIndex(1)
        self.ui.Applications_Stacked_Widget.setCurrentIndex(0)
        self.ui.Gestures_Button.setChecked(False)
        self.ui.Application_Button.setChecked(True)
        self.ui.Manual_Button.setChecked(False)
        self.ui.Custom_Button.setChecked(False)

    def switch_to_ManualPage(self):
        self.ui.Main_Body_Page_Stack.setCurrentIndex(1)
        self.ui.Manual_Stacked_Widget.setCurrentIndex(1)
        self.ui.ManualMode_Button.setChecked(False)
        self.ui.AutoMode_Button.setChecked(True)
        self.ui.Custom_Button.setChecked(False)
        self.ui.Auto_Mode_Static_Dynamic_Stacked_Widget.setCurrentIndex(0)
        self.ui.Static_Button4.setChecked(True)

    def switch_to_addCustomActionTypePage(self):
        self.ui.Main_Body_Page_Stack.setCurrentIndex(2)
        self.ui.Custom_Stacked_Widget.setCurrentIndex(1)
        self.ui.Action_Types_Stacked_Widget.setCurrentIndex(0)
        self.ui.Action_Type_ComboBox .setCurrentIndex(0)


    def switch_to_InformationPage(self):
        self.ui.More_Menu_Stacked_Widget.setCurrentIndex(0)

    def switch_to_SettingsPage(self):
        self.ui.More_Menu_Stacked_Widget.setCurrentIndex(1)

    def switch_to_ApplicationsPage(self):
        self.ui.Library_Stacked_Widget.setCurrentIndex(1)
        self.ui.Applications_Stacked_Widget.setCurrentIndex(0)

    def switch_to_GesturesPage(self):
        self.ui.Library_Stacked_Widget.setCurrentIndex(0)
        self.ui.Static_Dynamic_Gesture__Stacked_Widget.setCurrentIndex(0)
        self.ui.Static_Button1.setChecked(True)

    def switch_to_AutoModePage(self):
        self.ui.Manual_Stacked_Widget.setCurrentIndex(1)
        self.ui.Auto_Mode_Static_Dynamic_Stacked_Widget.setCurrentIndex(0)
        self.ui.Static_Button4.setChecked(True)


    def switch_to_ManualModePage(self):
        self.ui.Manual_Stacked_Widget.setCurrentIndex(0)

    def switch_to_DynamicModePage(self):
        self.ui.Manual_Stacked_Widget.setCurrentIndex(2)
        self.ui.Gesture_Modes_Stacked_Widget.setCurrentIndex(0)
        self.ui.Static_Button3.setChecked(True)

    def switch_to_Page1(self):
        self.ui.Applications_Stacked_Widget.setCurrentIndex(1)

    def switch_to_Page2(self):
        self.ui.Applications_Stacked_Widget.setCurrentIndex(2)

    def switch_to_Page3(self):
        self.ui.Applications_Stacked_Widget.setCurrentIndex(3)

    def switch_to_Page4(self):
        self.ui.Applications_Stacked_Widget.setCurrentIndex(4)

    def switch_to_Page5(self):
        self.ui.Applications_Stacked_Widget.setCurrentIndex(5)

    def switch_to_Page6(self):
        self.ui.Applications_Stacked_Widget.setCurrentIndex(6)

    def show_center_menu(self):
        self.ui.More_Menu_Widget.setHidden(False)

    def show_Library_Button_Container(self):
        self.ui.Library_Button_Container.setHidden(False)
        self.ui.Manual_Button_Container.setHidden(True)

    def show_Manual_Button_Container(self):
        self.ui.Manual_Button_Container.setHidden(False)
        self.ui.Library_Button_Container.setHidden(True)

    # Code to make the window draggable
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPosition = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.MouseButton.LeftButton:
            if self.dragPosition is not None:
                self.move(event.globalPosition().toPoint() - self.dragPosition)
                event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.dragPosition = None
            event.accept()

    # Code to connect another window
    def open_min_window(self):
        from Min_tray import MinimizeWindow
        if self.min_window is None:
            self.min_window = MinimizeWindow()

        self.min_window.show_pages()
        self.min_window.show()
        self.close()

    # def start_backend_main_thread(self):
    #     initiate_payload()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

