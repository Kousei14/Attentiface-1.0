from tkinter import *
import tkinter as tk
import os
from PIL import Image, ImageTk
import numpy as np
import cv2
from tkinter import messagebox

class msgbox:
    def __init__(self,root):
        self.root = root
        window_width = 364
        window_height = 210
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width/2)-(window_width/2)
        y_coor = (screen_height/2)-(window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor","red")
        self.root.overrideredirect(1)
        self.root.iconbitmap('attentiface_icon.ico')

        self.bg_msgbox = PhotoImage(file="train_msgbox.png")
        bg_label = tk.Label(self.root, border=0, bg="red",image=self.bg_msgbox)
        bg_label.pack(fill=BOTH, expand=True)

        img_yes=Image.open(r"ICONS_2\yes.png")
        img_yes=img_yes.resize((107,40))

        root.img_yes=ImageTk.PhotoImage(img_yes)
        button_yes=Button(root,image=root.img_yes,bg="black",borderwidth=0,width=107,highlightthickness=0,height=40,bd=0,relief="raised",activebackground="black",command=self.loadRegister)
        button_yes.place(x=45,y=135,width=107,height=40)

        img_no=Image.open(r"ICONS_2\no.png")
        img_no=img_no.resize((107,40))

        root.img_no=ImageTk.PhotoImage(img_no)
        button_no=Button(root,image=root.img_no,bg="black",borderwidth=0,width=107,highlightthickness=0,height=40,bd=0,relief="raised",activebackground="black",command=self.no)
        button_no.place(x=180,y=135,width=107,height=40)          

    def yes(self):
        photo_data_dir=("photo_data")
        path=[os.path.join(photo_data_dir,file)for file in os.listdir(photo_data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') #convert to a grayscale image
            img_numpy=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(img_numpy)
            ids.append(id)
        ids=np.array(ids) #convert into an array

        #TRAIN THE DATA using LBPH

        LBPH_clf=cv2.face.LBPHFaceRecognizer_create()
        LBPH_clf.train(faces,ids)
        LBPH_clf.write("model_classifier.xml")
        messagebox.showinfo("Done","Successfully trained the data")

    def no(self):
        self.root.destroy()

if __name__ == "__main__":
    root=Tk()
    obj=msgbox(root)
    root.mainloop()