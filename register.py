from tkinter import *
import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import cv2
from datetime import datetime
import sys
import glob
from itertools import count
import numpy as np
import threading
from splash_register import loadReg

stop=0

class Register:
    def __init__(self,root):
        self.root = root
        window_width = 1280
        window_height = 720
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width/2)-(window_width/2)
        y_coor = (screen_height/2)-(window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor","red")
        self.root.overrideredirect(1)
        self.root.iconbitmap(r'logos\attentiface_icon_v2.ico')

        self.var_ID=StringVar()
        self.var_keyID=StringVar()
        self.var_Name=StringVar()
        self.var_firstname=StringVar()
        self.var_middleI=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_photo=StringVar()

        self.bg_mainscreen = PhotoImage(file=r"backgrounds\bg_register.png")
        canvas1 = tk.Canvas(root, width=1280, height=720, background="red",highlightthickness=0)
        canvas1.pack()
        canvas1.create_image(0,0, image=self.bg_mainscreen ,anchor="nw")
        
        bg_label = tk.Label(self.root, border=0, bg="red",image=self.bg_mainscreen)
        bg_label.pack(fill=BOTH, expand=True)

    # ENTRY FORM
        # Employee ID
        Employee_ID_txt=tk.Entry(root,textvariable=self.var_ID,width=15,bd=0,font=("Montserrat",11, "bold"))
        canvas1.create_window(136, 125, window=Employee_ID_txt)

        # Last Name
        Lastname_txt=tk.Entry(root,textvariable=self.var_Name,width=15,bd=0,font=("Montserrat",11, "bold"))
        canvas1.create_window(136, 191, window=Lastname_txt)

        # First Name
        Firstname_txt=tk.Entry(root,textvariable=self.var_firstname,width=15,bd=0,font=("Montserrat",11, "bold"))
        canvas1.create_window(136, 257, window=Firstname_txt)

        # Middle Initial
        Middle_Initial_txt=tk.Entry(root,textvariable=self.var_middleI,width=15,bd=0,font=("Montserrat",11, "bold"))
        canvas1.create_window(136, 324, window=Middle_Initial_txt)

        # E-mail
        Email_txt=tk.Entry(root,textvariable=self.var_email,width=15,bd=0,font=("Montserrat",11, "bold"))
        canvas1.create_window(136, 392, window=Email_txt)

        # Contact Number
        Contact_number_txt=tk.Entry(root,textvariable=self.var_phone,width=15,bd=0,font=("Montserrat",11, "bold"))
        canvas1.create_window(136, 458, window=Contact_number_txt)

        # Address
        Address_txt=tk.Entry(root,textvariable=self.var_address,width=15,bd=0,font=("Montserrat",11, "bold"))
        canvas1.create_window(136, 525, window=Address_txt)

        # Gender
        gender_cb=ttk.Combobox(root,textvariable=self.var_gender,width=14,font=("Montserrat",11, "bold"),state="readonly")
        gender_cb["values"]=(" Select Gender"," Male"," Female")
        gender_cb.current(0)
        canvas1.create_window(136, 596, window=gender_cb)

        # keyID
        keyID_txt=tk.Entry(root,textvariable=self.var_keyID,width=3,bd=0,font=("Montserrat",11, "bold"))
        canvas1.create_window(196, 89, window=keyID_txt)

        # Search combobox
        self.var_search=StringVar()
        search_cb=ttk.Combobox(root,textvariable=self.var_search,width=14,font=("Montserrat",11, "bold"),state="readonly")
        search_cb.config(background="black")
        search_cb["values"]=(" Search by"," Last Name"," First Name"," Employee ID")
        search_cb.current(0)
        canvas1.create_window(359, 123, window=search_cb)

        # Search entry
        self.var_search_entry=StringVar()
        Search_txt=tk.Entry(root,textvariable=self.var_search_entry,width=10,bd=0,font=("Montserrat",11, "bold"))
        canvas1.create_window(565, 123, window=Search_txt)

    # BUTTONS
        # save
        img_save=Image.open(r"buttons\save.png")
        img_save=img_save.resize((150,75))

        root.img_save=ImageTk.PhotoImage(img_save)
        button_save=Button(root,image=root.img_save,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white",command=self.add)
        button_save.place(x=270,y=550,width=150,height=75)

        # update
        img_update=Image.open(r"buttons\update.png")
        img_update=img_update.resize((150,75))

        root.img_update=ImageTk.PhotoImage(img_update)
        button_update=Button(root,image=root.img_update,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white", command=self.update_data)
        button_update.place(x=420,y=550,width=150,height=75)

        # delete
        img_delete=Image.open(r"buttons\delete.png")
        img_delete=img_delete.resize((165,75))

        root.img_delete=ImageTk.PhotoImage(img_delete)
        button_delete=Button(root,image=root.img_delete,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white", command=self.delete)
        button_delete.place(x=570,y=550,width=160,height=75)

        # clear
        img_clear=Image.open(r"buttons\clear.png")
        img_clear=img_clear.resize((150,75))

        root.img_clear=ImageTk.PhotoImage(img_clear)
        button_clear=Button(root,image=root.img_clear,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white", command=self.clear)
        button_clear.place(x=730,y=550,width=150,height=75)

        # search
        img_search=Image.open(r"buttons\search.png")
        img_search=img_search.resize((100,50))

        root.img_search=ImageTk.PhotoImage(img_search)
        button_search=Button(root,image=root.img_search,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white", command=self.search)
        button_search.place(x=650,y=106,width=100,height=40)

        # reset
        img_reset=Image.open(r"buttons\reset.png")
        img_reset=img_reset.resize((100,50))

        root.img_reset=ImageTk.PhotoImage(img_reset)
        button_reset=Button(root,image=root.img_reset,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white", command=self.show_data)
        button_reset.place(x=750,y=106,width=100,height=40)

        # take_photo
        img_take_photo=Image.open(r"buttons\take_photo.png")
        img_take_photo=img_take_photo.resize((150,75))

        root.img_take_photo=ImageTk.PhotoImage(img_take_photo)
        button_take_photo=Button(root,image=root.img_take_photo,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white",command=self.display)
        button_take_photo.place(x=870,y=550,width=150,height=75)

        # exit
        img5_inactive=Image.open(r"buttons\exit_data_inactive.png")
        img5_inactive=img5_inactive.resize((70,70))

        img5_active=Image.open(r"buttons\exit_data_active.png")
        img5_active=img5_active.resize((80,80))

        root.img5_inactive=ImageTk.PhotoImage(img5_inactive)
        root.img5_active=ImageTk.PhotoImage(img5_active)

        def on_enter_exit(event):
                    button_exit.config(image=root.img5_active)
        def on_inactive_exit(event):
                    button_exit.config(image=root.img5_inactive)
        def pressed_exit(event):
                    button_exit.config(image=root.img5_inactive)
        def unpressed_exit(event):
                    button_exit.config(image=root.img5_active)
        button_exit=Button(root,image=root.img5_inactive,border=0,borderwidth=0,width=80,highlightthickness=0,height=80,bd=0,relief="sunken",activebackground="white",command=self.Close)
        button_exit.bind("<Enter>",on_enter_exit)
        button_exit.bind("<Leave>",on_inactive_exit)
        button_exit.bind("<Button-1>",pressed_exit)
        button_exit.bind("<ButtonRelease-1>",unpressed_exit)
        button_exit.place(x=1160,y=560,width=60,height=60)

        # photos
        img_photos_inactive=Image.open(r"buttons\photos_inactive.png")
        img_photos_inactive=img_photos_inactive.resize((70,70))

        img_photos_active=Image.open(r"buttons\photos_active.png")
        img_photos_active=img_photos_active.resize((80,80))

        root.img_photos_inactive=ImageTk.PhotoImage(img_photos_inactive)
        root.img_photos_active=ImageTk.PhotoImage(img_photos_active)

        def on_enter_photos(event):
                    button_photos.config(image=root.img_photos_active)
        def on_inactive_photos(event):
                    button_photos.config(image=root.img_photos_inactive)
        def pressed_photos(event):
                    button_photos.config(image=root.img_photos_inactive)
        def unpressed_photos(event):
                    button_photos.config(image=root.img_photos_active)
        button_photos=Button(root,image=root.img_photos_inactive,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white", command=self.open_photos)
        button_photos.bind("<Enter>",on_enter_photos)
        button_photos.bind("<Leave>",on_inactive_photos)
        button_photos.bind("<Button-1>",pressed_photos)
        button_photos.bind("<ButtonRelease-1>",unpressed_photos)
        button_photos.place(x=1100,y=560,width=60,height=60)

        # train
        img_train_inactive=Image.open(r"buttons\train_inactive.png")
        img_train_inactive=img_train_inactive.resize((70,70))

        img_train_active=Image.open(r"buttons\train_active.png")
        img_train_active=img_train_active.resize((80,80))

        root.img_train_inactive=ImageTk.PhotoImage(img_train_inactive)
        root.img_train_active=ImageTk.PhotoImage(img_train_active)

        def on_enter_train(event):
                    button_train.config(image=root.img_train_active)
        def on_inactive_train(event):
                    button_train.config(image=root.img_train_inactive)
        def pressed_train(event):
                    button_train.config(image=root.img_train_inactive)
        def unpressed_train(event):
                    button_train.config(image=root.img_train_active)
        button_train=Button(root,image=root.img_train_inactive,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white", command=self.train_classifier)
        button_train.bind("<Enter>",on_enter_train)
        button_train.bind("<Leave>",on_inactive_train)
        button_train.bind("<Button-1>",pressed_train)
        button_train.bind("<ButtonRelease-1>",unpressed_train)
        button_train.place(x=1040,y=560,width=60,height=60)

        # home

        img_home_inactive=Image.open(r"buttons\home_inactive.png")
        img_home_inactive=img_home_inactive.resize((70,70))

        img_home_active=Image.open(r"buttons\home_active.png")
        img_home_active=img_home_active.resize((80,80))

        root.img_home_inactive=ImageTk.PhotoImage(img_home_inactive)
        root.img_home_active=ImageTk.PhotoImage(img_home_active)

        def on_enter_home(event):
                    button_home.config(image=root.img_home_active)
        def on_inactive_home(event):
                    button_home.config(image=root.img_home_inactive)
        def pressed_home(event):
                    button_home.config(image=root.img_home_inactive)
        def unpressed_home(event):
                    button_home.config(image=root.img_home_active)
        button_home=Button(root,image=root.img_home_inactive,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white", command=self.home)
        button_home.bind("<Enter>",on_enter_home)
        button_home.bind("<Leave>",on_inactive_home)
        button_home.bind("<Button-1>",pressed_home)
        button_home.bind("<ButtonRelease-1>",unpressed_home)
        button_home.place(x=980,y=560,width=60,height=60)
        

    # DATABASE TABLE

        frame_DB=LabelFrame(root,bd=0,bg="white",relief=RIDGE,font=("Franklin Gothic Demi",12))
        frame_DB.place(x=293,y=184,width=910,height=335)

        hor_scroll=ttk.Scrollbar(frame_DB,orient=HORIZONTAL)
        ver_scroll=ttk.Scrollbar(frame_DB,orient=VERTICAL)

        self.student_table=ttk.Treeview(frame_DB,columns=("ID","Last Name","First Name","Middle Initial",
                                                          "Gender","E-mail","Phone No.", "Address","Photo",
                                                          "Employee ID"),xscrollcommand=hor_scroll.set, 
                                                          yscrollcommand=ver_scroll.set)

        hor_scroll.config(command=self.student_table.xview)
        ver_scroll.config(command=self.student_table.yview)

        hor_scroll.pack(side=BOTTOM,fill=X)
        ver_scroll.pack(side=RIGHT,fill=Y)
        hor_scroll.config(command=self.student_table.xview)
        ver_scroll.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Last Name",text="Last Name")
        self.student_table.heading("First Name",text="First Name")
        self.student_table.heading("Middle Initial",text="Middle Initial")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("E-mail",text="E-mail")
        self.student_table.heading("Phone No.",text="Phone No.")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Photo",text="Photo")
        self.student_table.heading("Employee ID",text="Employee ID")
        self.student_table["show"]="headings"

        self.student_table.column("ID",anchor=CENTER,width=10)
        self.student_table.column("Last Name",anchor=CENTER,width=120)
        self.student_table.column("First Name",anchor=CENTER,width=120)
        self.student_table.column("Middle Initial",anchor=CENTER,width=120)
        self.student_table.column("Gender",anchor=CENTER,width=80)
        self.student_table.column("E-mail",anchor=CENTER,width=190)
        self.student_table.column("Phone No.",anchor=CENTER,width=90)
        self.student_table.column("Address",anchor=CENTER,width=170)
        self.student_table.column("Photo",anchor=CENTER,width=150)
        self.student_table.column("Employee ID",anchor=CENTER,width=160)

        # adjustable table

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.show_data()

    def home(self):
        self.root.destroy()

    def open_photos(self):
        self.new_window=Toplevel(self.root)
        window_width = 500
        window_height = 580
        screen_width = self.new_window.winfo_screenwidth()
        screen_height = self.new_window.winfo_screenheight()
        x_coor = (screen_width/2)-(window_width/2)
        y_coor = (screen_height/2)-(window_height/2)
        self.new_window.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.new_window.wm_attributes("-transparentcolor","red")
        self.new_window.title("Attentiface V 1.0")
        self.new_window.iconbitmap(r'logos\attentiface_icon_v2.ico')

        images_list = []
        images_vars = []

        def load_images():
            dir_path = "photo_data"
            images_files = os.listdir(dir_path)
            images_files=images_files[::100]
            for r in range(0, len(images_files)):
                images_list.append([
                    ImageTk.PhotoImage(
                        Image.open(dir_path + '/' + images_files[r]).resize((50,50), Image.Resampling.LANCZOS)),
                    ImageTk.PhotoImage(
                        Image.open(dir_path + '/' + images_files[r]).resize((500, 500), Image.Resampling.LANCZOS))
                    
                    ])
                images_vars.append(f'img_{r}')

            for n in range(len(images_vars)):
                globals()[images_vars[n]] = tk.Button(slider, image=images_list[n][0], bd=0, command=lambda n=n: display_image(n))
                globals()[images_vars[n]].pack(side=tk.LEFT)

        def display_image(index):
            image_display_lbl.config(image=images_list[index][1])

        image_display_lbl = tk.Label(self.new_window)
        image_display_lbl.pack(side=tk.TOP, fill=tk.X)

        canvas = tk.Canvas(self.new_window, height=60, width=500, background="white", highlightthickness=0)
        canvas.pack(side=tk.BOTTOM, fill=tk.X)

        x_scroll = ttk.Scrollbar(self.new_window, orient='horizontal')
        x_scroll.pack(side='bottom', fill='x')
        x_scroll.config(command=canvas.xview)

        canvas.config(xscrollcommand=x_scroll.set)
        canvas.bind('<Configure>', lambda e: canvas.bbox('all'))

        slider = tk.Frame(canvas, background="red")
        canvas.create_window((0,0), window=slider, anchor=tk.NW)

        load_images()
        display_image(0)

        self.new_window.mainloop()

    def Close(self):
        sys.exit()

    def train_classifier(self):
        validation = messagebox.askyesno("Attentiface V 1.0",
                                         "Are you sure you want to register the data?",
                                         parent=self.root)
        if validation > 0:
            self.new_win=Toplevel(self.root)
            window_width = 750
            window_height = 345
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            x_coor = (screen_width/2)-(window_width/2)
            y_coor = (screen_height/2)-(window_height/2)
            self.new_win.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
            self.new_win.overrideredirect(1)
            self.new_win.wm_attributes("-transparentcolor", "red")

            image_list = []

            def extract_image_from_gif(path):
                global gif_duration

                image = Image.open(path)

                for r in count(1):
                    try:
                        image_list.append(image.copy())
                        image.seek(r)
                    except Exception as e:
                        print(e)
                        break
                print(len(image_list))
                gif_duration = int(image.info['duration'])


            def play_gif():
                global x, cur_img, stop
                try:
                    x +=1
                    cur_img = ImageTk.PhotoImage(image_list[x])
                    gif_lb.config(image=cur_img)
                    self.new_win.after(gif_duration-26, play_gif)
                except Exception as e:
                    print(e)
                    x = 0
                    self.new_win.after(gif_duration, play_gif)
                if stop==1:
                    stop=0
                    self.new_win.protocol("WM_DELETE_WINDOW", loadReg(self.new_win))
            def yes():
                global stop
                photo_data_dir=("photo_data")
                path=[os.path.join(photo_data_dir,file)for file in os.listdir(photo_data_dir)]

                faces=[]
                ids=[]

                for image in path:
                    img=Image.open(image).convert('L') # convert to a grayscale image
                    img_numpy=np.array(img,'uint8')
                    id=int(os.path.split(image)[1].split('.')[1])

                    faces.append(img_numpy)
                    ids.append(id)
                ids=np.array(ids) # convert into an array

                # TRAIN THE DATA using LBPH

                LBPH_clf=cv2.face.LBPHFaceRecognizer_create()
                LBPH_clf.train(faces,ids)
                LBPH_clf.write("recognizer.xml")
                stop=1   

            gif_lb = tk.Label(self.new_win,bg="red",border=0)
            gif_lb.pack()

            extract_image_from_gif('loading_register.gif')

            t1 = threading.Thread(target=play_gif)
            t1.start()
            t2 = threading.Thread(target=yes)
            t2.start()

        else:
            if not validation:
                return
            
    # Add function
    
    def add(self):
        if self.var_Name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Attentiface V 1.0",
                                 "Please fill-in all the required fields",
                                 parent=self.root)
        else:
            try:
                i=0
                conn = sqlite3.connect("face_recognition_software_system")
                cursor = conn.cursor()
                val = (
                    self.var_Name.get(),
                    self.var_firstname.get(),
                    self.var_middleI.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_photo.get(),
                    self.var_ID.get())
                sql_insert=f""" INSERT INTO student_details(Last_Name,
                            First_Name,
                            Middle_Initial, 
                            Gender, 
                            E_mail, 
                            Phone_No, 
                            Address, 
                            Photo,
                            Employee_ID) VALUES
                            ("{val[0]}","{val[1]}","{val[2]}","{val[3]}","{val[4]}","{val[5]}","{val[6]}",
                            "{val[7]}","{val[8]}") """
                cursor.execute(sql_insert)

                conn.commit()
                self.show_data()
                messagebox.showinfo("Attentiface V 1.0",
                                    "Input successful",
                                    parent=self.root)
            except Exception as es:
                messagebox.showerror("Attentiface V 1.0",
                                     f"Error: {str(es)}",parent=self.root)

            conn = sqlite3.connect("face_recognition_software_system")
            cursor = conn.cursor()
            cursor.execute(" SELECT * from student_details ")
            data=cursor.fetchall()
            lr=int(len(data))
            index_value=data[lr-1]
            self.var_keyID.set("")
            self.var_keyID.set(index_value[0])


            conn.commit()
            self.show_data()
            conn.close()

    # SHOW DATA TO BOX
    def show_data(self):
        conn = sqlite3.connect("databases/face_recognition_software_system")
        cursor = conn.cursor()
        cursor.execute("SELECT * from student_details")
        data=cursor.fetchall()
        
        self.var_search.set(" Search by")
        self.var_search_entry.set("")

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        else:
            self.student_table.delete(*self.student_table.get_children())
        conn.close

    # get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_ID.set(data[9]),
        self.var_Name.set(data[1]),
        self.var_firstname.set(data[2]),
        self.var_middleI.set(data[3]),
        self.var_gender.set(data[4]),
        self.var_email.set(data[5]),
        self.var_phone.set(data[6]),
        self.var_address.set(data[7]),
        self.var_photo.set(data[8]),
        self.var_keyID.set(data[0])

    # Update function
    def update_data(self):
        if self.var_Name.get()=="" or self.var_ID.get()=="":
            messagebox.showerror("Attentiface V 1.0",
                                 "Please fill-in all the required fields",
                                 parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Attentiface V 1.0", 
                                           "Are you sure you want to update this entry?",
                                           parent=self.root)
                if Update>0:
                    conn = sqlite3.connect("face_recognition_software_system")
                    cursor = conn.cursor()
                    sql = "INSERT INTO student_details (Last_Name, First_Name, Middle_Initial, Gender, E_mail, Phone_No, Address, Photo, Employee_ID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"    
                    val = (self.var_Name.get(),
                        self.var_firstname.get(),
                        self.var_middleI.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_photo.get(),
                        self.var_ID.get(),
                        self.var_keyID.get())
                    sql_update=f""" UPDATE student_details SET Last_Name="{val[0]}", First_Name="{val[1]}", Middle_Initial="{val[2]}", Gender="{val[3]}", E_mail="{val[4]}", Phone_No="{val[5]}", Address="{val[6]}", Photo="{val[7]}", Employee_ID="{val[8]}" WHERE ID={val[9]} """
                    cursor.execute(sql_update)
                else:
                    if not Update:
                        return
                messagebox.showinfo("Attentiface V 1.0",
                                    "Data updated successfully",
                                    parent=self.root)
                conn.commit()
                self.show_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Attentiface V 1.0",
                                     f"Error: {str(es)}",parent=self.root)
    # Delete function
    def delete(self):
        if self.var_ID.get()=="":
            messagebox.showerror("Attentiface V 1.0",
                                 "Select an entry to delete",
                                 parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Attentiface V 1.0",
                                           "Are you sure you want to delete this data?",
                                           parent=self.root)
                if delete>0:
                    conn = sqlite3.connect("face_recognition_software_system")
                    cursor = conn.cursor()

                    val=self.var_keyID.get()
                    # delete photos---------------
                    for row in cursor.execute(f"SELECT Employee_ID FROM student_details WHERE ID={val}"):
                            path = "photo_data/"
                            files = glob.glob(path + f"*{row[0]}*.jpg")
                            for file in files:
                                os.remove(file)

                    cursor.execute("SELECT COUNT(*) FROM student_details")
                    count = cursor.fetchone()[0]
                    if count == 1:
                        cursor.execute("DELETE FROM student_details")
                        cursor.execute("DELETE FROM sqlite_sequence where name='student_details'")
                    else:
                        sql=""" DELETE FROM student_details where ID={} """.format(val)
                        cursor.execute(sql)
                else:
                    if not delete:
                        return
                conn.commit()
                messagebox.showinfo("Attentiface V 1.0","Data deleted successfully", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Attentiface V 1.0",f"Error: {str(es)}",parent=self.root)
        self.show_data()

    # Clear function
    def clear(self):
        self.var_ID.set(""),
        self.var_Name.set(""),
        self.var_gender.set(" Select Gender"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_photo.set(""),
        self.var_firstname.set(""),
        self.var_middleI.set(""),
        self.var_keyID.set("")        
    
    def display(self):
        self.new_window=Toplevel(self.root)
        self.new_window.geometry('400x320')
        self.new_window.iconbitmap(r'logos\attentiface_icon.ico')
        self.new_window.title("Attentiface V 1.0")
        self.new_window.configure(background='white')
        self.new_window.configure(bd=0)
        # Create a frame
        app = Frame(self.new_window, bg="white")
        app.grid()

        # train
        img_train1=Image.open(r"icons\start.png")
        img_train1=img_train1.resize((120,60))

        self.new_window.img_train1=ImageTk.PhotoImage(img_train1)
        button_train=Button(self.new_window,image=self.new_window.img_train1,bg="white",
                            borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,
                            relief="raised",activebackground="white",command=self.take_photo_data)
        button_train.place(x=145,y=257,width=120,height=60)

        # Create a label in the frame
        lmain = Label(app)
        lmain.grid()

        # Capture from camera
        cap = cv2.VideoCapture(0)

        # function for video streaming
        def video_stream():
            _, frame = cap.read()
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            cv2image = cv2.resize(cv2image, (400,250))
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            lmain.imgtk = imgtk
            lmain.configure(image=imgtk)
            lmain.after(1, video_stream) 

        video_stream()
        self.new_window.mainloop()

    # TAKE PHOTO DATA
    def take_photo_data(self):
        if self.var_Name.get()=="" or self.var_ID.get()=="" or self.var_keyID=="":
            messagebox.showerror("Attentiface V 1.0",
                                 "Please fill-in the fields first",
                                 parent=self.root)
        else:
            try:
                take_pic=messagebox.askyesno("Attentiface V 1.0", 
                                             "Are you sure you want to take a photo?",
                                             parent=self.root)
                if take_pic>0:
                    self.new_window.destroy()
                    conn = sqlite3.connect("face_recognition_software_system")
                    cursor = conn.cursor()
                    cursor.execute(""" SELECT * from student_details """)
                    result=cursor.fetchall()
                    
                    keyID=self.var_keyID.get()
                    ID=self.var_ID.get()
                    #--------------------------------------------
                    def twentyfour_to_twelve(time):
                        # Split the time into hours and minutes
                        hours, minutes, seconds = time.split(":")
                        hours = int(hours)
                        minutes = int(minutes)

                        # Determine AM or PM
                        am_pm = "AM"
                        if hours >= 12:
                            hours -= 12
                            am_pm = "PM"

                        # Format the result as a string
                        return f"{hours:02d}:{minutes:02d} {am_pm}"
                    #---------------------------------------------
                    now = datetime.now()
                    current_time = str(twentyfour_to_twelve(str(now.time())))
                    current_date = str(now.date())

                    val = (self.var_Name.get(),
                        self.var_firstname.get(),
                        self.var_middleI.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        f"{current_date}, {current_time}",
                        self.var_ID.get())
                    sql_update=f""" UPDATE student_details SET Last_Name="{val[0]}", First_Name="{val[1]}", Middle_Initial="{val[2]}", Gender="{val[3]}", E_mail="{val[4]}", Phone_No="{val[5]}", Address="{val[6]}", Photo="{val[7]}", Employee_ID="{val[8]}" WHERE ID={keyID} """
                    cursor.execute(sql_update)
                    conn.commit()
                    self.show_data()
                    self.clear()
                    conn.close()

                    # LOAD MODEL

                    classifer_model=cv2.CascadeClassifier(r"detection_model\haarcascade_frontalface_default.xml")

                    def crop_face(img):
                        gray_convert=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=classifer_model.detectMultiScale(gray_convert,1.3,5) # scaling factor of 1.3, minimun neighbour of 5

                        for (x,y,w,h) in faces:
                            crop_face=img[y:y+h,x:x+w]
                            return crop_face
                  
                    cap=cv2.VideoCapture(0)
                    img_id=0

                    while True:
                        ret,frame=cap.read()
                        if crop_face(frame)is not None:
                            img_id+=1
                            face=cv2.resize(crop_face(frame),(250,250))
                            face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                            if img_id > 10:
                                data_path=f"photo_data/{ID}."+str(keyID)+"."+str(int(img_id-10))+".jpg"
                                cv2.imwrite(data_path,face)
                                cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_DUPLEX,2,(255,255,255),2)
                                cv2.imshow("Face Capture",face)

                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Attentiface V 1.0",
                                        "All photo samples taken successfully",
                                        parent=self.root)
                else:
                    if not take_pic:
                        return
            except Exception as es:
                messagebox.showerror("Attentiface V 1.0",
                                     f"Error: {str(es)}",
                                     parent=self.root)
    
    # Search function
    def search(self):
        if self.var_search.get()=="" or self.var_search_entry.get()=="":
            messagebox.showerror("Attentiface V 1.0",
                                 "Please fill in the search details")
        else:
            try:
               conn = sqlite3.connect("face_recognition_software_system")
               cursor = conn.cursor()
               if self.var_search.get()==" Employee ID":
                    word = "Employee_ID"
               elif self.var_search.get()==" Last Name":
                    word = "Last_Name"
               elif self.var_search.get()==" First Name":
                    word = "First_Name"
               sql_search= f""" SELECT * from student_details WHERE {word} LIKE '%{str(self.var_search_entry.get())}%'"""
               cursor.execute(sql_search) 
               data=cursor.fetchall()
               
               if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
               conn.close()
            except Exception as es:
                messagebox.showerror("Attentiface V 1.0",
                                     f"Error: {str(es)}",
                                     parent=self.root)

if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()