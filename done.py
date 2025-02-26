import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

class Done:
    def __init__(self, root, path):
        self.root = root
        self.path = path

        # Configurations
        window_width = 350
        window_height = 350
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width / 2) - (window_width / 2)
        y_coor = (screen_height / 2) - (window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor","red")
        self.root.overrideredirect(1)

        # Background
        bg_label = Label(
            self.root, 
            border = 0, 
            bg = "red")
        bg_label.pack(
            fill = BOTH, 
            expand = True)

        # Done stamp
        done_img = Image.open(r"{}".format(path)).resize((350,350))
        self.done_img = ImageTk.PhotoImage(done_img)
        button_done = Button(
            self.root,
            image = self.done_img,
            bg = "red",
            borderwidth = 0,
            width = 350,
            highlightthickness = 0,
            height = 350,
            bd = 0,
            relief = "raised",
            activebackground="red")
        button_done.place(
            x = 0,
            y = 0,
            width = 350,
            height = 350)

        self.root.after(
            5000, 
            self.root.destroy)

if __name__ == "__main__":
    root = tk.Tk()
    obj = Done(root, "icons\emails_sent.png")
    root.mainloop()
