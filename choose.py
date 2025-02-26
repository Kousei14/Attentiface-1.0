from tkinter import *
import tkinter as tk

from utils.utilities import image_utils as imgu
from recognize_cam import Recognize

class Choose:
    def __init__(self, root):
        self.root = root
        self.imgu = imgu()

        # Configurations
        window_width = 500
        window_height = 125
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width / 2) - (window_width / 2)
        y_coor = (screen_height / 2) - (window_height / 2)

        
        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor","red")
        self.root.overrideredirect(1)

        # Background
        self.bg = PhotoImage(
            file = r"backgrounds\bg_choose.png")
        
        # Background Label
        bg_label = tk.Label(
            self.root, 
            border = 0, 
            bg = "red",
            image = self.bg)
        bg_label.pack(
            fill = BOTH, 
            expand = True)

        # Buttons
        # --- Cam 1
        self.imgu.setup_button(
            root = root,
            img_path_inactive = r"icons\cam1_inactive.png",
            img_path_active = r"icons\cam1_active.png",
            button_x = 40,
            button_y = 27,
            button_width = 160,
            button_height = 85,
            img_width = 160,
            img_height = 85,
            command = self.recognize
        )

        # --- Cam 2
        self.imgu.setup_button(
            root = root,
            img_path_inactive = r"icons\cam2_inactive.png",
            img_path_active = r"icons\cam2_active.png",
            button_x = 317,
            button_y = 27,
            button_width = 160,
            button_height = 85,
            img_width = 160,
            img_height = 85,
            command = self.recognize
        )

        # --- Back
        self.imgu.setup_button_v3(
            root = root,
            img_path = r"icons\back_inactive.png",
            x = 224,
            y = 40,
            img_width = 100,
            img_height = 54,
            button_width = 60,
            button_height = 54,
            command = self.close,
            bg = "white",
            borderwidth = 0,
            highlightthickness = 0,
            bd = 0,
            relief = "raised",
            activebackground = "black"
        )

    def recognize(self):
        recognize_screen = Recognize()

    def close(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Choose(root)
    root.mainloop()