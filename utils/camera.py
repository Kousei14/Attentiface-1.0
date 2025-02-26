from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

import cv2

from utils.utilities import image_utils as imgu

class Camera:
    def __init__(self, root):
        self.root = root
        self.imgu = imgu()
        self.cap = cv2.VideoCapture(0)

        # Configurations
        self.root.geometry('400x320')
        self.root.iconbitmap(r'logos\attentiface_icon_v2.ico')
        self.root.title("Attentiface V 1.0")
        self.root.configure(background = 'white')
        self.root.configure(bd = 0)

        # Background
        self.camera = Frame(self.root, 
                            bg = "white")
        self.camera.grid()

        # Label
        self.lmain = Label(self.camera)
        self.lmain.grid()

        # Buttons
        # --- start button
        self.imgu.setup_button_v2(
            root = self.root,
            img_path = r"buttons\start.png",
            x = 145,
            y = 257,
            width = 120,
            height = 60,
            command = self.final_take_photos,
            borderwidth = 0,
            highlightthickness = 0,
            bd = 0,
            relief = "raised",
            activebackground = "white"
        )

        self.stream()

    def stream(self):
        _, frame = self.cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        cv2image = cv2.resize(cv2image, (400,250))
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image = img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image = imgtk)
        self.lmain.after(1, self.stream)

    def take_photos(self, id, key_id, root):
        face_detector_model = cv2.CascadeClassifier(r"detection_model\haarcascade_frontalface_default.xml")
        
        cap = cv2.VideoCapture(0)
        img_id = 0

        while True:
            ret, frame = cap.read()
            if self.crop_photo(frame, face_detector_model) is not None:
                img_id += 1
                face = cv2.resize(
                    self.crop_photo(frame, face_detector_model), 
                    (250,250)
                    )
                face = cv2.cvtColor(
                    face, 
                    cv2.COLOR_BGR2GRAY
                    )
                if img_id > 10:
                    data_path = f"photo_data/{id}."+ str(key_id) + "." + str(int(img_id - 10)) + ".jpg"
                    cv2.imwrite(
                        data_path, 
                        face
                        )
                    cv2.putText(
                        face, 
                        str(img_id),
                        (50,50),
                        cv2.FONT_HERSHEY_DUPLEX,
                        2,
                        (255,255,255),
                        2
                        )
                    cv2.imshow(
                        "Face Capture",
                        face
                        )

            if cv2.waitKey(1) == 13 or int(img_id) == 100:
                break

        cap.release()
        cv2.destroyAllWindows()

        messagebox.showinfo("Attentiface V 1.0",
                            "All photo samples taken successfully",
                            parent = root)
        
    def crop_photo(self, img, face_detector_model):
        gray_convert = cv2.cvtColor(
            img, 
            cv2.COLOR_BGR2GRAY
            )
        faces = face_detector_model.detectMultiScale(gray_convert, 
                                                    scaleFactor = 1.3,
                                                    minNeighbors = 5)
        for (x, y, w, h) in faces:
            crop_face = img[y : y + h, x : x + w]
            return crop_face
        
if __name__ == "__main__":
    root = Tk()
    obj = Camera(root)
    root.mainloop()