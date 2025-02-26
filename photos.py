from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from PIL import Image, ImageTk

import os

class Photos:
    def __init__(self, root):
        self.root = root

        # Configurations
        window_width = 500
        window_height = 580
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coor = (screen_width / 2) - (window_width / 2)
        y_coor = (screen_height / 2) - (window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor", "red")
        self.root.title("Attentiface V 1.0")
        self.root.iconbitmap(r'logos/attentiface_icon_v2.ico')

        # Photo Grid
        self.images_list = []
        self.images_vars = []

        self.image_display_lbl = tk.Label(
            self.root
            )
        self.image_display_lbl.pack(
            side = tk.TOP, 
            fill = tk.X
            )

        self.canvas = tk.Canvas(
            self.root, 
            height = 60, 
            width = 500, 
            background = "white", 
            highlightthickness = 0
            )
        self.canvas.pack(
            side = tk.BOTTOM, 
            fill = tk.X
            )

        self.x_scroll = ttk.Scrollbar(
            self.root, 
            orient = 'horizontal'
            )
        self.x_scroll.pack(
            side = 'bottom', 
            fill = 'x'
            )
        self.x_scroll.config(
            command = self.canvas.xview
            )

        self.canvas.config(
            xscrollcommand = self.x_scroll.set
            )
        self.canvas.bind(
            '<Configure>', 
            lambda e: self.canvas.bbox('all')
            )

        self.slider = tk.Frame(
            self.canvas, 
            background = "red"
            )
        self.canvas.create_window(
            (0, 0), 
            window = self.slider, 
            anchor = tk.NW
            )

        self.load_images()
        self.display_image(0)

    # Functions
    def load_images(self):
        dir_path = "photo_data"
        images_files = os.listdir(dir_path)
        images_files = images_files[::100]
        for r in range(0, len(images_files)):
            self.images_list.append([
                ImageTk.PhotoImage(
                    Image.open(
                        os.path.join(
                            dir_path, 
                            images_files[r]
                        )
                    ).resize(
                        (50, 50), 
                        Image.Resampling.LANCZOS
                    )
                ),
                ImageTk.PhotoImage(
                    Image.open(
                        os.path.join(
                            dir_path, 
                            images_files[r]
                        )
                    ).resize(
                        (500, 500), 
                        Image.Resampling.LANCZOS
                    )
                )
            ])
            self.images_vars.append(f'img_{r}')

        for n in range(len(self.images_vars)):
            globals()[self.images_vars[n]] = tk.Button(
                self.slider, 
                image = self.images_list[n][0], 
                bd = 0,
                command = lambda n = n: self.display_image(n)
            )
            globals()[self.images_vars[n]].pack(
                side = tk.LEFT
                )

    def display_image(self, index):
        self.image_display_lbl.config(
            image = self.images_list[index][1]
            )

if __name__ == "__main__":
    root = Tk()
    obj = Photos(root)
    root.mainloop()
