from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk

from utils.utilities import image_utils as imgu
from register import Register
from choose import Choose
from photos import Photos
from attendance import Attendance

class Menu:
    def __init__(self, root):
        self.root = root
        self.imgu = imgu()

        # Configurations
        window_width = 800
        window_height = 450
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width / 2) - (window_width / 2)
        y_coor = (screen_height / 2) - (window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor", "red")
        self.root.overrideredirect(1)

        # Background
        self.bg = PhotoImage(
            file = r"backgrounds\bg_menu.png"
        )
        canvas = tk.Canvas(
            root,
            width = 1280,
            height = 720,
            background = "red",
            highlightthickness = 0
        )
        canvas.pack()
        canvas.create_image(
            0, 0,
            image = self.bg,
            anchor = "nw"
        )
        bg_label = tk.Label(
            self.root, 
            border = 0, 
            bg = "red", 
            image = self.bg
        )
        bg_label.pack(
            fill = BOTH, 
            expand = True
        )

        # Logo
        attentiface_banner = Image.open(r"icons\attentiface_banner.png").resize((230, 67))
        attentiface_banner = ImageTk.PhotoImage(attentiface_banner)
        attentiface_banner_logo = Button(
            self.root, 
            image = attentiface_banner, 
            bg = "black", 
            borderwidth = 0, 
            width = 200,
            highlightthickness = 0, 
            height = 200, 
            bd = 0, 
            relief = "sunken", 
            activebackground = "black"
        )
        attentiface_banner_logo.attentiface_banner = attentiface_banner
        attentiface_banner_logo.place(
            x = 500, 
            y = 190, 
            width = 230, 
            height = 67
        )

        # Buttons
        # --- Register
        self.imgu.setup_button(
            self.root,
            img_path_inactive = r"icons/register_inactive.png", 
            img_path_active = r"icons/register_active.png", 
            button_x = 80, 
            button_y = 50, 
            button_width = 230, 
            button_height = 67, 
            img_width = 230, 
            img_height = 67, 
            command = self.register
        )
        
        # --- Face Scan
        self.imgu.setup_button(
            self.root,
            img_path_inactive = r"icons/face_scan_inactive.png", 
            img_path_active = r"icons/face_scan_active.png", 
            button_x = 80, 
            button_y = 119, 
            button_width = 230, 
            button_height = 67, 
            img_width = 230, 
            img_height = 67, 
            command = self.choose
        )

        # --- Photos
        self.imgu.setup_button(
            self.root,
            img_path_inactive = r"icons/photos_inactive.png", 
            img_path_active = r"icons/photos_active.png", 
            button_x = 80, 
            button_y = 188, 
            button_width = 230, 
            button_height = 67, 
            img_width = 230, 
            img_height = 67, 
            command = self.photos
        )

        # --- Records
        self.imgu.setup_button(
            self.root,
            img_path_inactive = r"icons/records_inactive.png", 
            img_path_active = r"icons/records_active.png", 
            button_x = 80, 
            button_y = 257, 
            button_width = 230, 
            button_height = 67, 
            img_width = 230, 
            img_height = 67, 
            command = self.attendance
        )

        # --- Exit
        self.imgu.setup_button(
            self.root,
            img_path_inactive = r"icons/exit_inactive.png", 
            img_path_active = r"icons/exit_active.png", 
            button_x = 80, 
            button_y = 326, 
            button_width = 230, 
            button_height = 67, 
            img_width = 230, 
            img_height = 67, 
            command = self.exit
        )

    # Functions
    def register(self):
        self.new_window = Toplevel(self.root)
        self.register_screen = Register(self.new_window)

    def choose(self):
        self.new_window = Toplevel(self.root)
        self.choose_screen = Choose(self.new_window)

    def photos(self):
        self.new_window = Toplevel(self.root)
        self.photos_screen = Photos(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.attend_screen = Attendance(self.new_window)

    def exit(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Menu(root)
    root.mainloop()

