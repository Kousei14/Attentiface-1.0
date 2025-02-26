from tkinter import *
import tkinter as tk
from tkinter import messagebox

from utils.utilities import image_utils as imgu
from main import Main

class License:
    def __init__(self, root):
        self.root = root
        self.imgu = imgu()

        # Configurations
        window_width = 920
        window_height = 575
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width / 2) - (window_width / 2)
        y_coor = (screen_height / 2) - (window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor", "red")
        self.root.overrideredirect(1)
        self.root.iconbitmap(r'logos\attentiface_icon_v2.ico')

        # Background
        self.bg = PhotoImage(
            file = r"backgrounds\bg_license.png"
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

        # Username Textbox
        self.var_username = StringVar()
        self.imgu.setup_textbox(
            root,
            canvas = canvas, 
            variable = self.var_username, 
            x = 730, 
            y = 185
        )

        # Password Textbox
        self.var_password = StringVar()
        self.imgu.setup_textbox(
            root,
            canvas = canvas, 
            variable = self.var_password, 
            x = 730, 
            y = 265
        )

        # License Textbox
        self.var_license = StringVar()
        self.imgu.setup_textbox(
            root,
            canvas = canvas, 
            variable = self.var_license, 
            x = 730, 
            y = 355
        )

        # Activate Button
        self.imgu.setup_button(
            self.root,
            img_path_inactive = r"icons\activate_inactive.png", 
            img_path_active = r"icons\activate_active.png", 
            button_x = 632, 
            button_y = 393, 
            button_width = 177, 
            button_height = 45, 
            img_width = 177, 
            img_height = 89, 
            command = self.open_main
        )

        # Close Button
        self.imgu.setup_button(
            self.root,
            img_path_inactive = r"buttons\close_inactive.png", 
            img_path_active = r"buttons\close_active.png", 
            button_x = 870, 
            button_y = 20, 
            button_width = 25, 
            button_height = 25, 
            img_width = 25, 
            img_height = 25, 
            command = self.close
        )

    # Functions
    def close(self):
        self.root.destroy()

    def open_main(self):
        messagebox.showinfo(
            "Attentiface V 1.0", 
            "Your subscription is now activated", 
            parent = self.root
        )
        self.root.destroy()
        self.win = Tk()
        self.main = Main(self.win)
        self.win.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = License(root)
    root.mainloop()
