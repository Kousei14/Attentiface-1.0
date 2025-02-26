from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

from queries import Queries

class Host:
    def __init__(self,root):
        self.root = root
        self.q = Queries()

        # Configurations
        window_width = 520
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width / 2) - (window_width / 2)
        y_coor = (screen_height / 2) - (window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor","red")
        self.root.overrideredirect(1)
        self.root.iconbitmap(r'logos\attentiface_icon_v2.ico')

        # Background
        bg = Image.open(r"backgrounds/bg_login.png")
        self.photoimg = ImageTk.PhotoImage(bg)

        canvas = Canvas(
            root,
            width = 520,
            height = 300,
            bd = 0,
            highlightthickness = 0,
            background = "red")
        canvas.pack(
            fill = BOTH,
            expand = TRUE)
        canvas.create_image(
            0, 0,
            image = self.photoimg,
            anchor = "nw")

        # Text boxes
        # --- E-mail
        self.varEmail = StringVar()
        Email_txt = tk.Entry(
            root, 
            textvariable = self.varEmail,
            width = 17,
            bd = 0,
            font = ("Montserrat", 10, "bold"))
        canvas.create_window(
            252, 
            108, 
            window = Email_txt)

        # --- Password
        self.varPass = StringVar()
        Password_txt = tk.Entry(
            root,
            textvariable = self.varPass,
            width = 17,
            bd = 0,
            font = ("Montserrat", 10, "bold"))
        canvas.create_window(
            263, 
            177, 
            window = Password_txt)

        # Buttons
        # --- Save
        img_save = Image.open(r"buttons\save_v2.png").resize((70,35))
        img_save = ImageTk.PhotoImage(img_save)
        button_save = Button(
            root,
            image = img_save,
            bg = "white",
            borderwidth = 0,
            width = 200,
            highlightthickness = 0,
            height = 200,
            bd = 0,
            relief = "raised",
            activebackground = "white",
            command = self.insert)
        button_save.img_save = img_save
        button_save.place(
            x = 117,
            y = 210,
            width = 70,
            height = 35)

        # --- Update
        img_update = Image.open(r"buttons\update_v2.png").resize((70,35))
        img_update = ImageTk.PhotoImage(img_update)
        button_update = Button(
            root,
            image = img_update,
            bg = "white",
            borderwidth = 0,
            width = 200,
            highlightthickness = 0,
            height = 200,
            bd = 0,
            relief = "raised",
            activebackground = "white",
            command = self.update)
        button_save.img_update = img_update
        button_update.place(
            x = 217,
            y = 210,
            width = 70,
            height = 35)

        # --- Exit
        img_exit = Image.open(r"buttons\exit_v2.png").resize((70,35))
        img_exit = ImageTk.PhotoImage(img_exit)
        button_exit = Button(
            root,
            image = img_exit,
            bg = "white",
            borderwidth = 0,
            width = 200,
            highlightthickness = 0,
            height = 200,
            bd = 0,
            relief = "raised",
            activebackground = "white",
            command = self.close)
        button_exit.img_exit = img_exit
        button_exit.place(
            x = 317,
            y = 210,
            width = 70,
            height = 35)
    
    def insert(self):
        if self.varEmail.get() == "" or self.varPass.get() == "":
            messagebox.showerror("Input Validation",
                                 "Please fill-in all the required fields",
                                 parent = self.root)
        else:
            database = r"databases\Attentiface.db"
            table = "Credentials"
            self.q.insert(database, 
                          table,
                          columns = ["gmail_address", "gmail_api_code"],
                          values = [self.varEmail.get(), self.varPass.get()],
                          root = self.root)

    def update(self):
        if self.varEmail.get() == "" or self.varPass.get() == "":
            messagebox.showerror("Input Validation",
                                 "Please fill-in all the required fields",
                                 parent = self.root)
        else:
            database = r"databases\Attentiface.db"
            table = "Credentials"
            self.q.update(database,
                          table,
                          columns = ["gmail_address", "gmail_api_code"],
                          values = [self.varEmail.get(), self.varPass.get()],
                          on_key = 1,
                          root = self.root
                          )
            
    def close(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Host(root)
    root.mainloop()