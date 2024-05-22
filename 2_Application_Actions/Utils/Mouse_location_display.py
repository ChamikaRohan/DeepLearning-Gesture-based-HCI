import pyautogui
import tkinter as tk


def show_mouse_location():
    # Create a tkinter window
    root = tk.Tk()
    root.title("Mouse Location")

    # Function to update the mouse coordinates label
    def update_label():
        x, y = pyautogui.position()
        label.config(text=f"Mouse Location: X={x}, Y={y}")
        root.after(100, update_label)  # Update every 100 milliseconds

    # Label to display mouse coordinates
    label = tk.Label(root, text="")
    label.pack(padx=10, pady=10)

    # Start updating the label
    update_label()

    # Run the tkinter event loop
    root.mainloop()


# Call the function to start showing the mouse location
show_mouse_location()
