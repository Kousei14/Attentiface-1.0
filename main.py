import tkinter as tk
from tkinter import *

from utils.utilities import animation_utils as animu
from menu import Menu

class Main:
    def __init__(self, root):
        self.root = root

        # Configurations
        window_width = 480
        window_height = 242
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width / 2) - (window_width / 2)
        y_coor = (screen_height / 2) - (window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.overrideredirect(1)
        self.root.wm_attributes("-transparentcolor", "red")

        animu(self.root).load_screen('loading_animations/splash_screen_loading.gif', self.open_menu)

    # Functions
    def open_menu(self):
        self.root.destroy()
        self.win = Tk()
        self.main = Menu(self.win)
        self.win.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    obj = Main(root)
    root.mainloop()
