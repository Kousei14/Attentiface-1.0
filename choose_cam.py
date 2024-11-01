from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from recognize_cam1 import In
from recognize_cam2 import Out

class Choose:
    def __init__(self, root):

        self.root = root
        window_width = 500
        window_height = 125
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width/2)-(window_width/2)
        y_coor = (screen_height/2)-(window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor","red")
        self.root.overrideredirect(1)

        self.choose_mainscreen = PhotoImage(file="bg_chooseAttendance.png")
        choose_label = tk.Label(self.root, border=0, bg="red",image=self.choose_mainscreen)
        choose_label.pack(fill=BOTH, expand=True)

        #IN button

        img_in=Image.open(r"ICONS_2\cam1_inactive.png")
        img_in=img_in.resize((160,85))

        img_in_active=Image.open(r"ICONS_2\cam1_active.png")
        img_in_active=img_in_active.resize((160,85))

        root.img_in=ImageTk.PhotoImage(img_in)
        root.img_in_active=ImageTk.PhotoImage(img_in_active)

        def on_enter_in(event):
            button_student.config(image=root.img_in_active)
        def on_inactive_in(event):
            button_student.config(image=root.img_in)

        button_student=Button(root,image=root.img_in,bg="black",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="black",command=self.attendance_in)
        button_student.bind("<Enter>",on_enter_in)
        button_student.bind("<Leave>",on_inactive_in)
        button_student.place(x=40,y=27,width=160,height=85)

        #OUT button

        img_out=Image.open(r"ICONS_2\cam2_inactive.png")
        img_out=img_out.resize((160,85))

        img_out_active=Image.open(r"ICONS_2\cam2_active.png")
        img_out_active=img_out_active.resize((160,85))

        root.img_out=ImageTk.PhotoImage(img_out)
        root.img_out_active=ImageTk.PhotoImage(img_out_active)

        def on_enter_out(event):
            button_choose.config(image=root.img_out_active)
        def on_inactive_out(event):
            button_choose.config(image=root.img_out)

        button_choose=Button(root,image=root.img_out,bg="black",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="black",command=self.attendance_out)
        button_choose.bind("<Enter>",on_enter_out)
        button_choose.bind("<Leave>",on_inactive_out)
        button_choose.place(x=317,y=27,width=160,height=85)

        #BACK button

        img_back=Image.open(r"ICONS_2\back_inactive.png")
        img_back=img_back.resize((100,54))

        root.img_back=ImageTk.PhotoImage(img_back)
        button_reset=Button(root,image=root.img_back,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="black",command=self.back)
        button_reset.place(x=224,y=40,width=60,height=54)

    def attendance_in(self):
        In_Screen = In()

    def attendance_out(self):
        Out_Screen = Out()

    def back(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=Choose(root)
    root.mainloop()