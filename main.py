import tkinter as tk
from tkinter import *
from itertools import count
from PIL import Image, ImageTk
from menu import mainscreen

class Splash_screen:
    def __init__(self,root):
        self.root = root
        window_width = 480
        window_height = 242
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width/2)-(window_width/2)
        y_coor = (screen_height/2)-(window_height/2)
        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.overrideredirect(1)
        self.root.wm_attributes("-transparentcolor", "red")

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
            global x, cur_img
            try:
                x +=1
                cur_img = ImageTk.PhotoImage(image_list[x])
                gif_lb.config(image=cur_img)
                self.root.after(gif_duration-35, play_gif)
            except Exception as e:
                print(e)
                x = 0
                root.after(gif_duration, play_gif)

        def main_window():
            self.root.destroy()
            self.win = Tk()
            self.main_S = mainscreen(self.win)
            self.win.mainloop()

        gif_lb = tk.Label(self.root,bg="red",border=0)
        gif_lb.pack()

        extract_image_from_gif(r'loading_animations\splash_screen_loading_final.gif')
        play_gif()

        self.root.after(3000, main_window)

if __name__ == "__main__":
    root = tk.Tk()
    obj = Splash_screen(root)
    root.mainloop()
