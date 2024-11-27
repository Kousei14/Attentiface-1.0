import sqlite3
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

class DB_Credentials:
    def __init__(self,root):
        self.root=root
        window_width = 520
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width/2)-(window_width/2)
        y_coor = (screen_height/2)-(window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor","red")
        self.root.overrideredirect(1)
        self.root.iconbitmap('attentiface_icon.ico')

        self.varEmail = StringVar()
        self.varPass = StringVar()

        img=Image.open(r"pictures/log_in.png")
        self.photoimg=ImageTk.PhotoImage(img)

        canvas=Canvas(root,width=520,height=300,bd=0,highlightthickness=0,background="red")
        canvas.pack(fill=BOTH,expand=TRUE)
        canvas.create_image(0,0, image=self.photoimg,anchor="nw")

        # E_MAIL
        Email_txt=tk.Entry(root,textvariable=self.varEmail,width=17,bd=0,font=("Montserrat",10, "bold"))
        canvas.create_window(252, 108, window=Email_txt)
        # Password
        Password_txt=tk.Entry(root,textvariable=self.varPass,width=17,bd=0,font=("Montserrat",10, "bold"))
        canvas.create_window(263, 177, window=Password_txt)

        # save
        img_save=Image.open(r"pictures\save1.png")
        img_save=img_save.resize((70,35))

        root.img_save=ImageTk.PhotoImage(img_save)
        button_save=Button(root,image=root.img_save,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white",command=self.Insert_DB)
        button_save.place(x=117,y=210,width=70,height=35)

        # update
        img_update=Image.open(r"pictures\update1.png")
        img_update=img_update.resize((70,35))

        root.img_update=ImageTk.PhotoImage(img_update)
        button_update=Button(root,image=root.img_update,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white",command=self.Update_DB)
        button_update.place(x=217,y=210,width=70,height=35)

        # exit
        img_exit=Image.open(r"pictures\exit1.png")
        img_exit=img_exit.resize((70,35))

        root.img_exit=ImageTk.PhotoImage(img_exit)
        button_exit=Button(root,image=root.img_exit,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white",command=self.close)
        button_exit.place(x=317,y=210,width=70,height=35)

    def create_DB(self):
        conn = sqlite3.connect("Credentials_Database")
        cursor = conn.cursor()

        cursor.execute(""" CREATE TABLE IF NOT EXISTS credentials
                                    (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                    E_mail varchar(45) NOT NULL, 
                                    Password varchar(45) NOT NULL 
                                    ) """)
        cursor.execute(""" CREATE TABLE IF NOT EXISTS Time_limit
                            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Start_time varchar(45) NOT NULL, 
                            End_time varchar(45) NOT NULL 
                            ) """)

        conn.commit()

        for row in cursor.execute("SELECT * FROM credentials"):
            print(row)
        for row1 in cursor.execute("SELECT * FROM Time_limit"):
            print(row1)
    
    def Insert_DB(self):
        if self.varEmail.get()=="" or self.varPass.get()=="":
            messagebox.showerror("Input Validation","Please fill-in all the required fields",parent=self.root)
        else:
            try:
                connection = sqlite3.connect('Credentials_Database')
                cursor = connection.cursor()

                cursor.execute('SELECT COUNT(*) FROM credentials')
                count = cursor.fetchone()[0]

                if count < 1:
                    # INSERT DATA
                    sql_insert=f""" INSERT INTO credentials( 
                                                E_mail, 
                                                Password) VALUES
                                                ("{str(self.varEmail.get())}","{str(self.varPass.get())}") """

                    cursor.execute(sql_insert)
                    for row in cursor.execute("SELECT * FROM credentials"):
                        print(row)
                    messagebox.showinfo("Input Validation","Successfully inputted e-mail & password")
                else:
                    messagebox.showerror("Input Validation", "You can only provide one e-mail. To change current e-mail, update instead of save")
            except Exception as es:
                messagebox.showerror("Error Prompt",f"Error: {str(es)}",parent=self.root)
            connection.commit()

    def Update_DB(self):
        if self.varEmail.get()=="" or self.varPass.get()=="":
            messagebox.showerror("Input Validation","Please fill-in all the required fields",parent=self.root)
        else:
            try:
                connection = sqlite3.connect('Credentials_Database')
                cursor = connection.cursor()
                # UPDATE DATA
                ID=1
                sql_update=f""" UPDATE credentials SET E_mail="{str(self.varEmail.get())}", Password="{str(self.varPass.get())}" """

                cursor.execute(sql_update)
                for row in cursor.execute("SELECT * FROM credentials"):
                    print(row)
                messagebox.showinfo("Input Validation","Successfully updated e-mail & password")
            except Exception as es:
                    messagebox.showerror("Error Prompt",f"Error: {str(es)}",parent=self.root)
            connection.commit()

    def close(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=DB_Credentials(root)
    root.mainloop()