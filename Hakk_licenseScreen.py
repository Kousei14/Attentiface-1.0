from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from Attentiface import splash_screen
from tkinter import messagebox

class Login:
    def __init__(self, root):
        self.root = root
        window_width = 920
        window_height = 575
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width/2)-(window_width/2)
        y_coor = (screen_height/2)-(window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor","red")
        self.root.overrideredirect(1)
        self.root.iconbitmap('attentiface_icon.ico')

        self.bg_mainscreen = PhotoImage(file="bg_login.png")
        canvas1 = tk.Canvas(root, width=1280, height=720, background="red",highlightthickness=0)
        canvas1.pack()
        canvas1.create_image(0,0, image=self.bg_mainscreen ,anchor="nw")
        
        bg_label = tk.Label(self.root, border=0, bg="red",image=self.bg_mainscreen)
        bg_label.pack(fill=BOTH, expand=True)

        #Username
        self.var_username=StringVar()
        unsername_txt=tk.Entry(root,textvariable=self.var_username,width=20,bd=0,font=("Montserrat",12, "bold"))
        canvas1.create_window(730, 185, window=unsername_txt)
        #Password
        self.var_password=StringVar()
        password_txt=tk.Entry(root,textvariable=self.var_password,width=20,bd=0,font=("Montserrat",12, "bold"))
        canvas1.create_window(730, 265, window=password_txt)
        #Licence Key
        self.var_license=StringVar()
        license_txt=tk.Entry(root,textvariable=self.var_license,width=20,bd=0,font=("Montserrat",12, "bold"))
        canvas1.create_window(730, 355, window=license_txt)

        #button activate

        img1_inactive=Image.open(r"ICONS_2\activate_inactive.png")
        img1_inactive=img1_inactive.resize((177,89))

        img1_active=Image.open(r"ICONS_2\activate_active.png")
        img1_active=img1_active.resize((177,89))

        root.img1_inactive=ImageTk.PhotoImage(img1_inactive)
        root.img1_active=ImageTk.PhotoImage(img1_active)

        def on_enter_student(event):
                    button_student.config(image=root.img1_active)
        def on_inactive_student(event):
                    button_student.config(image=root.img1_inactive)
        def pressed_student(event):
                    button_student.config(image=root.img1_inactive)
        def unpressed_student(event):
                    button_student.config(image=root.img1_active)
        button_student=Button(root,image=root.img1_inactive,bg="black",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="black", command=self.main_window)
        button_student.bind("<Enter>",on_enter_student)
        button_student.bind("<Leave>",on_inactive_student)
        button_student.bind("<Button-1>",pressed_student)
        button_student.bind("<ButtonRelease-1>",unpressed_student)
        button_student.place(x=632,y=393,width=177,height=45)

        #button close
        img2_inactive=Image.open(r"pictures\close_inactive.png")
        img2_inactive=img2_inactive.resize((25,25))

        img2_active=Image.open(r"pictures\close_active.png")
        img2_active=img2_active.resize((25,25))

        root.img2_inactive=ImageTk.PhotoImage(img2_inactive)
        root.img2_active=ImageTk.PhotoImage(img2_active)

        def on_enter_close(event):
                    button_close.config(image=root.img2_active)
        def on_inactive_close(event):
                    button_close.config(image=root.img2_inactive)
        def pressed_close(event):
                    button_close.config(image=root.img2_inactive)
        def unpressed_close(event):
                    button_close.config(image=root.img2_active)
        button_close=Button(root,image=root.img2_inactive,bg="black",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="black", command=self.close)
        button_close.bind("<Enter>",on_enter_close)
        button_close.bind("<Leave>",on_inactive_close)
        button_close.bind("<Button-1>",pressed_close)
        button_close.bind("<ButtonRelease-1>",unpressed_close)
        button_close.place(x=870,y=20,width=25,height=25)
    def close(self):
            self.root.destroy()
    def main_window(self):
            messagebox.showinfo("Attentiface V 1.0","Your subscription is now activated",parent=self.root)
            self.root.destroy()
            self.win=Tk()
            self.main_S=splash_screen(self.win)
            self.win.mainloop()    

if __name__ == "__main__":
    root=Tk()
    obj=Login(root)
    root.mainloop()