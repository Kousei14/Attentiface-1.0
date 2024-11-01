from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from license import Login

class Expire:
    def __init__(self, root):
        self.root = root
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

        self.bg_mainscreen = PhotoImage(file=r"backgrounds\bg_expiration.png")
        canvas1 = tk.Canvas(root, width=1280, height=720, background="red", highlightthickness=0)
        canvas1.pack()
        canvas1.create_image(0, 0, image=self.bg_mainscreen, anchor="nw")
        
        bg_label = tk.Label(self.root, border=0, bg="red", image=self.bg_mainscreen)
        bg_label.pack(fill=BOTH, expand=True)

        # button renew

        img1_inactive = Image.open(r"icons\renew_inactive.png")
        img1_inactive = img1_inactive.resize((177, 89))

        img1_active = Image.open(r"icons\renew_active.png")
        img1_active = img1_active.resize((177, 89))

        root.img1_inactive = ImageTk.PhotoImage(img1_inactive)
        root.img1_active = ImageTk.PhotoImage(img1_active)

        def on_enter_renew(event):
            button_renew.config(image=root.img1_active)

        def on_inactive_renew(event):
            button_renew.config(image=root.img1_inactive)

        def pressed_renew(event):
            button_renew.config(image=root.img1_inactive)

        def unpressed_renew(event):
            button_renew.config(image=root.img1_active)

        button_renew = Button(root, image=root.img1_inactive, bg="black", borderwidth=0, width=200,
                              highlightthickness=0, height=200, bd=0, relief="raised", activebackground="black")
        button_renew.bind("<Enter>", on_enter_renew)
        button_renew.bind("<Leave>", on_inactive_renew)
        button_renew.bind("<Button-1>", pressed_renew)
        button_renew.bind("<ButtonRelease-1>", unpressed_renew)
        button_renew.place(x=390, y=275, width=177, height=45)

        # button enter_key

        img3_inactive = Image.open(r"icons\enterKey_inactive.png")
        img3_inactive = img3_inactive.resize((177, 89))

        img3_active = Image.open(r"icons\enterKey_active.png")
        img3_active = img3_active.resize((177, 89))

        root.img3_inactive = ImageTk.PhotoImage(img3_inactive)
        root.img3_active = ImageTk.PhotoImage(img3_active)

        def on_enter_student(event):
            button_student.config(image=root.img3_active)

        def on_inactive_student(event):
            button_student.config(image=root.img3_inactive)

        def pressed_student(event):
            button_student.config(image=root.img3_inactive)

        def unpressed_student(event):
            button_student.config(image=root.img3_active)

        button_student = Button(root, image=root.img3_inactive, bg="black", borderwidth=0, width=200,
                                highlightthickness=0, height=200, bd=0, relief="raised", activebackground="black",
                                command=self.activate)
        button_student.bind("<Enter>", on_enter_student)
        button_student.bind("<Leave>", on_inactive_student)
        button_student.bind("<Button-1>", pressed_student)
        button_student.bind("<ButtonRelease-1>", unpressed_student)
        button_student.place(x=390, y=345, width=177, height=45)

        # button close
        img2_inactive = Image.open(r"buttons\close_inactive.png")
        img2_inactive = img2_inactive.resize((25, 25))

        img2_active = Image.open(r"buttons\close_active.png")
        img2_active = img2_active.resize((25, 25))

        root.img2_inactive = ImageTk.PhotoImage(img2_inactive)
        root.img2_active = ImageTk.PhotoImage(img2_active)

        def on_enter_close(event):
            button_close.config(image=root.img2_active)

        def on_inactive_close(event):
            button_close.config(image=root.img2_inactive)

        def pressed_close(event):
            button_close.config(image=root.img2_inactive)

        def unpressed_close(event):
            button_close.config(image=root.img2_active)

        button_close = Button(root, image=root.img2_inactive, bg="black", borderwidth=0, width=200,
                              highlightthickness=0, height=200, bd=0, relief="raised", activebackground="black",
                              command=self.close)
        button_close.bind("<Enter>", on_enter_close)
        button_close.bind("<Leave>", on_inactive_close)
        button_close.bind("<Button-1>", pressed_close)
        button_close.bind("<ButtonRelease-1>", unpressed_close)
        button_close.place(x=870, y=20, width=25, height=25)

    def close(self):
        self.root.destroy()

    def activate(self):
        self.root.destroy()
        self.win = Tk()
        self.main_S = Login(self.win)
        self.win.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = Expire(root)
    root.mainloop()
