from tkinter import *
import tkinter as tk

from utils.utilities import image_utils as imgu
from license import License

class Expiration:
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
            file = r"backgrounds\bg_expiration.png"
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

        # Buttons
        # --- Renew Button
        self.imgu.setup_button(
            self.root,
            img_path_inactive = r"icons\renew_inactive.png",
            img_path_active = r"icons\renew_active.png",
            button_x = 390,
            button_y = 275,
            button_width = 177,
            button_height = 45,
            img_width = 177,
            img_height = 89,
            command = None
        )

        # --- Enter_Key Button
        self.imgu.setup_button(
            self.root,
            img_path_inactive = r"icons\enterKey_inactive.png",
            img_path_active = r"icons\enterKey_active.png",
            button_x = 390,
            button_y = 345,
            button_width = 177,
            button_height = 45,
            img_width = 177,
            img_height = 89,
            command = self.open_license
        )

        # --- Close Button
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

    def open_license(self):
        self.root.destroy()
        self.win = Tk()
        self.main = License(self.win)
        self.win.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = Expiration(root)
    root.mainloop()
