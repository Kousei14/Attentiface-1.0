from tkinter import *

import os
import numpy as np
import cv2
import threading

from utils.utilities import animation_utils as animu
from done import Done

class Train:
    def __init__(self, root, second_root = None):
        self.root = root
        self.second_root = second_root
        self.animu = animu(self.root)
        
        # Configuration
        window_width = 750
        window_height = 345
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width / 2) - (window_width / 2)
        y_coor = (screen_height / 2) - (window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor", "red")
        self.root.overrideredirect(1)
        self.root.iconbitmap(r'logos\attentiface_icon_v2.ico')    
        
        t1 = threading.Thread(
            target = self.animu.load_screen("loading_animations/loading_register.gif", self.stop)
            )
        t1.start()

        t2 = threading.Thread(
            target = self.train
            )
        t2.start()   

    def train(self):
        photo_data_dir = ("photo_data")
        path = [os.path.join(photo_data_dir, file) for file in os.listdir(photo_data_dir)]

        faces = [np.array(Image.open(image).convert('L'), 'uint8') for image in path]  
        ids = np.array([int(os.path.split(image)[1].split('.')[1]) for image in path]) 

        LBPH_clf = cv2.face.LBPHFaceRecognizer_create()
        LBPH_clf.train(faces, ids)
        LBPH_clf.write("models/model_classifier.xml")

        self.animu.stop_animation = True
    
    def stop(self):
        self.root.destroy()
        self.new_window = self.second_root
        self.done_screen = Done(self.new_window, "icons\data_registered.png")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()