from tkinter import *
import tkinter as tk
import os
from PIL import Image, ImageTk
from Hakk_registerScreen import Register
from Hakk_chooseAttendance import Choose
from Hakk_attendanceScreen import Attendance_screen
import tkinter.ttk as ttk

class mainscreen:
    def __init__(self, root):

        self.root = root
        window_width = 800
        window_height = 450
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width/2)-(window_width/2)
        y_coor = (screen_height/2)-(window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor","red")
        self.root.overrideredirect(1)

        """ def move_app(e):
            root.geometry(f'+{e.x_root}+{e.y_root}') """

        self.bg_mainscreen = PhotoImage(file=r"backgrounds\bg_mainscreen.png")
        bg_label = tk.Label(self.root, border=0, bg="red",image=self.bg_mainscreen)
        bg_label.pack(fill=BOTH, expand=True)

        """ bg_label.bind("<B1-Motion>", move_app) """

        # logo banner
            
        attentiface_banner=Image.open(r"ICONS\attentiface_banner.png")
        attentiface_banner=attentiface_banner.resize((230,67))

        root.attentiface_banner_img=ImageTk.PhotoImage(attentiface_banner)
        atteentiface_final=Button(root,image=root.attentiface_banner_img,bg="black",borderwidth=0,width=200,
                                  highlightthickness=0,height=200,bd=0,relief="sunken",activebackground="black")
        atteentiface_final.place(x=500,y=190,width=230,height=67)

        # button register

        img1_inactive=Image.open(r"ICONS\register_active.png")
        img1_inactive=img1_inactive.resize((230,67))

        img1_active=Image.open(r"ICONS\register_inactive.png")
        img1_active=img1_active.resize((230,67))

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
        button_student=Button(root,image=root.img1_inactive,bg="black",borderwidth=0,width=200,highlightthickness=0,
                              height=200,bd=0,relief="raised",activebackground="black",command=self.register)
        button_student.bind("<Enter>",on_enter_student)
        button_student.bind("<Leave>",on_inactive_student)
        button_student.bind("<Button-1>",pressed_student)
        button_student.bind("<ButtonRelease-1>",unpressed_student)
        button_student.place(x=80,y=50,width=230,height=67)

        # button face scan
          
        img2_inactive=Image.open(r"ICONS\face_scan_active.png")
        img2_inactive=img2_inactive.resize((230,67))

        img2_active=Image.open(r"ICONS\face_scan_inactive.png")
        img2_active=img2_active.resize((230,67))

        root.img2_inactive=ImageTk.PhotoImage(img2_inactive)
        root.img2_active=ImageTk.PhotoImage(img2_active)

        def on_enter_face_scan(event):
                    button_face_scan.config(image=root.img2_active)
        def on_inactive_face_scan(event):
                    button_face_scan.config(image=root.img2_inactive)
        def pressed_face_scan(event):
                    button_face_scan.config(image=root.img2_inactive)
        def unpressed_face_scan(event):
                    button_face_scan.config(image=root.img2_active)
        button_face_scan=Button(root,image=root.img2_inactive,bg="black",borderwidth=0,width=200,highlightthickness=0,
                                height=200,bd=0,relief="raised",activebackground="black",command=self.Choose_attendance)
        button_face_scan.bind("<Enter>",on_enter_face_scan)
        button_face_scan.bind("<Leave>",on_inactive_face_scan)
        button_face_scan.bind("<Button-1>",pressed_face_scan)
        button_face_scan.bind("<ButtonRelease-1>",unpressed_face_scan)
        button_face_scan.place(x=80,y=119,width=230,height=67)

        # button photos
                
        img3_inactive=Image.open(r"ICONS\photos_active.png")
        img3_inactive=img3_inactive.resize((230,67))

        img3_active=Image.open(r"ICONS\photos_inactive.png")
        img3_active=img3_active.resize((230,67))

        root.img3_inactive=ImageTk.PhotoImage(img3_inactive)
        root.img3_active=ImageTk.PhotoImage(img3_active)

        def on_enter_photos(event):
                    button_photos.config(image=root.img3_active)
        def on_inactive_photos(event):
                    button_photos.config(image=root.img3_inactive)
        def pressed_photos(event):
                    button_photos.config(image=root.img3_inactive)
        def unpressed_photos(event):
                    button_photos.config(image=root.img3_active)
        button_photos=Button(root,image=root.img3_inactive,bg="black",borderwidth=0,width=200,highlightthickness=0,
                             height=200,bd=0,relief="raised",activebackground="black",command=self.open_photos)
        button_photos.bind("<Enter>",on_enter_photos)
        button_photos.bind("<Leave>",on_inactive_photos)
        button_photos.bind("<Button-1>",pressed_photos)
        button_photos.bind("<ButtonRelease-1>",unpressed_photos)
        button_photos.place(x=80,y=188,width=230,height=67)

        # button records
     
        img4_inactive=Image.open(r"ICONS\records_active.png")
        img4_inactive=img4_inactive.resize((230,67))

        img4_active=Image.open(r"ICONS\records_inactive.png")
        img4_active=img4_active.resize((230,67))

        root.img4_inactive=ImageTk.PhotoImage(img4_inactive)
        root.img4_active=ImageTk.PhotoImage(img4_active)

        def on_enter_records(event):
                    button_records.config(image=root.img4_active)
        def on_inactive_records(event):
                    button_records.config(image=root.img4_inactive)
        def pressed_records(event):
                    button_records.config(image=root.img4_inactive)
        def unpressed_records(event):
                    button_records.config(image=root.img4_active)
        button_records=Button(root,image=root.img4_inactive,bg="black",borderwidth=0,width=200,highlightthickness=0,
                              height=200,bd=0,relief="raised",activebackground="black",command=self.Attendance)
        button_records.bind("<Enter>",on_enter_records)
        button_records.bind("<Leave>",on_inactive_records)
        button_records.bind("<Button-1>",pressed_records)
        button_records.bind("<ButtonRelease-1>",unpressed_records)
        button_records.place(x=80,y=257,width=230,height=67)

        # button exit
          
        img5_inactive=Image.open(r"ICONS\exit_active.png")
        img5_inactive=img5_inactive.resize((230,67))

        img5_active=Image.open(r"ICONS\exit_inactive.png")
        img5_active=img5_active.resize((230,67))

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
        button_exit=Button(root,image=root.img5_inactive,bg="black",borderwidth=0,width=200,highlightthickness=0,
                           height=200,bd=0,relief="raised",activebackground="black",command=self.exit)
        button_exit.bind("<Enter>",on_enter_exit)
        button_exit.bind("<Leave>",on_inactive_exit)
        button_exit.bind("<Button-1>",pressed_exit)
        button_exit.bind("<ButtonRelease-1>",unpressed_exit)
        button_exit.place(x=80,y=326,width=230,height=67)

    def register(self):
        self.new_window=Toplevel(self.root)
        self.Register_screen=Register(self.new_window)
    def Choose_attendance(self):
        self.new_window=Toplevel(self.root)
        self.Choose_screen=Choose(self.new_window)
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
        self.new_window.iconbitmap('attentiface_icon_v2.ico')

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
                globals()[images_vars[n]] = tk.Button(slider, image=images_list[n][0], bd=0, 
                                                      command=lambda n=n: display_image(n))
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

    def Attendance(self):
        self.new_window=Toplevel(self.root)
        self.attend_screen=Attendance_screen(self.new_window)
    def exit(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=mainscreen(root)
    root.mainloop()
