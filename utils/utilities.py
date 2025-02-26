from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from itertools import count
from datetime import datetime

class image_utils:
    def __init__(self):
            pass
    
    # .resize()/.place() different dimensions, active/inactive same dimensions, 2 events
    def setup_button(
            self,
            root,
            img_path_inactive,
            img_path_active,
            button_x,
            button_y,
            button_width,
            button_height,
            img_width,
            img_height,
            command
        ):
            img_inactive = Image.open(img_path_inactive).resize((img_width, img_height))
            img_active = Image.open(img_path_active).resize((img_width, img_height))

            img_inactive = ImageTk.PhotoImage(img_inactive)
            img_active = ImageTk.PhotoImage(img_active)

            button = Button(
                root,
                image = img_inactive,
                bg = "black",
                borderwidth = 0,
                highlightthickness = 0,
                bd = 0,
                relief = "raised",
                activebackground = "black",
                command = command
            )
            button.image_inactive = img_inactive
            button.image_active = img_active

            def on_enter(event):
                button.config(image = button.image_active)

            def on_leave(event):
                button.config(image = button.image_inactive)

            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)
            button.place(
                x = button_x,
                y = button_y,
                width = button_width,
                height = button_height
            )

            return button
    
    # .resize()/.place same dimensions, no active/inactive, lumulubog
    def setup_button_v2(
            self,
            root,
            img_path,
            x,
            y,
            width,
            height,
            command,
            bg = "white",
            borderwidth = 0,
            highlightthickness = 0,
            bd = 0,
            relief = "raised",
            activebackground = "white"
        ):
        img = Image.open(img_path).resize((width, height))
        img = ImageTk.PhotoImage(img)

        button = Button(
            root,
            image = img,
            bg = bg,
            borderwidth = borderwidth,
            highlightthickness = highlightthickness,
            bd = bd,
            relief = relief,
            activebackground = activebackground,
            command = command
        )
        button.image = img  # Keep a reference to avoid garbage collection
        button.place(
            x = x,
            y = y,
            width = width,
            height = height
        )

        return button
    
    # .resize()/.place() different dimensions, no active/inactive, lumulubog
    def setup_button_v3(
            self,
            root,
            img_path,
            x,
            y,
            img_width,
            img_height,
            button_width,
            button_height,
            command,
            bg = "white",
            borderwidth = 0,
            highlightthickness = 0,
            bd = 0,
            relief = "raised",
            activebackground = "white"
        ):
        img = Image.open(img_path).resize((img_width, img_height))
        img = ImageTk.PhotoImage(img)

        button = Button(
            root,
            image = img,
            bg = bg,
            borderwidth = borderwidth,
            highlightthickness = highlightthickness,
            bd = bd,
            relief = relief,
            activebackground = activebackground,
            command = command
        )
        button.image = img  # Keep a reference to avoid garbage collection
        button.place(
            x = x,
            y = y,
            width = button_width,
            height = button_height
        )

        return button
    
    # .resize()/.place different dimensions, active/inactive different dimensions, 4 events
    def setup_button_v4(
        self,
        root,
        image_path_inactive,
        image_path_active,
        x,
        y,
        width,
        height,
        command
    ):
        # Load and resize images
        img_inactive = Image.open(image_path_inactive)
        img_inactive = img_inactive.resize((width, height))
        img_active = Image.open(image_path_active)
        img_active = img_active.resize((width + 10, height + 10))  # Slightly larger for active state

        # Create PhotoImage objects
        img_inactive = ImageTk.PhotoImage(img_inactive)
        img_active = ImageTk.PhotoImage(img_active)

        # Define event handlers
        def on_enter(event):
            button.config(image=img_active)

        def on_leave(event):
            button.config(image=img_inactive)

        def on_press(event):
            button.config(image=img_inactive)

        def on_release(event):
            button.config(image=img_active)

        # Create and place the button
        button = Button(
            root,
            image = img_inactive,
            bg = "white",
            borderwidth = 0,
            highlightthickness = 0,
            bd = 0,
            relief = "raised",
            activebackground = "white",
            command = command
        )
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        button.bind("<Button-1>", on_press)
        button.bind("<ButtonRelease-1>", on_release)
        button.place(x=x, y=y, width=width, height=height)

    def setup_textbox(
                self,
                root, 
                canvas, 
                variable, 
                x, 
                y,
                width: int = 20,
                bd: int = 0):
            
            textbox = tk.Entry(
                root, 
                textvariable = variable, 
                width = width, 
                bd = bd, 
                font = ("Montserrat", 10, "bold")
            )
            canvas.create_window(
                x, 
                y, 
                window = textbox
            )
    
    def setup_combobox(
            self,
            root, 
            canvas, 
            variable, 
            x, 
            y,
            values,
            width: int = 14,  # Default width
            font: tuple = ("Montserrat", 11, "bold"),  # Default font
            state: str = "readonly" ,
            config = None # Default state
        ):
        combobox = ttk.Combobox(
            root, 
            textvariable = variable, 
            width = width, 
            font = font, 
            state = state
        )
        combobox["values"] = values
        combobox.current(0)
        if config:
             combobox.config(**config)
        canvas.create_window(
            x, 
            y, 
            window=combobox
        )

class animation_utils:
    def __init__(self, root):
        self.root = root
        self.image_list = []
        self.stop_animation = False

    def load_screen(self, path, function):
        self.extract_frames_from_gif(r'{}'.format(path))

        self.gif_lb = tk.Label(
             self.root,
             bg = "red",
             border = 0
        )
        self.gif_lb.pack()

        self.play_gif()
        self.root.after(3000, function)

    def extract_frames_from_gif(self, path):
        self.image_list = []
        self.gif_duration = 0
        image = Image.open(path)

        for r in count(1):
            try:
                self.image_list.append(image.copy())
                image.seek(r)
            except Exception as e:
                print(e)
                break
        print(f"{len(self.image_list)} frames")
        self.gif_duration = int(image.info['duration'])

    def play_gif(self):
        self.x = 0
        self.cur_img = None

        def update_gif():
            if not self.stop_animation:
                try:
                    self.cur_img = ImageTk.PhotoImage(self.image_list[self.x])
                    self.gif_lb.config(image=self.cur_img)
                    self.x = (self.x + 1) % len(self.image_list)  # Reset self.x to 0 when it reaches the end
                    self.root.after(self.gif_duration, update_gif)
                except Exception as e:
                    print(e)
                    self.x = 0
                    self.root.after(self.gif_duration - 35, update_gif)

        update_gif()

class datetime_utils:
    def __init__(self):
        pass

    def twentyfour_to_twelve(self, time):
        time = str(time)

        # Split the time into hours, minutes, seconds
        hours, minutes, seconds = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

        # Determine AM or PM
        am_pm = "AM"
        if hours >= 12:
            hours -= 12
            am_pm = "PM"

        return f"{hours:02d}:{minutes:02d} {am_pm}"
    
    def twelve_to_twentyfour(self, time_list: list):
        time_list_24 = []
        for tm in time_list:
            time_24 = datetime.strptime(tm, "%I:%M %p").strftime("%H:%M:%S")
            if ':00' not in time_24:
                time_24 = time_24 + ':00'
            time_list_24.append(time_24)
        
        return time_list_24

