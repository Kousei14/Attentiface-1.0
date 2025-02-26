from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import sys
from datetime import datetime

from utils.utilities import image_utils as imgu, datetime_utils as dtu
from utils.camera import Camera
from photos import Photos
from train import Train
from queries import Queries

class Register:
    def __init__(self,root):
        self.root = root
        self.imgu = imgu()
        self.dtu = dtu()
        self.q = Queries()

        # Configurations
        window_width = 1280
        window_height = 720
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width / 2) - (window_width / 2)
        y_coor = (screen_height / 2) - (window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor","red")
        self.root.overrideredirect(1)
        self.root.iconbitmap(r'logos\attentiface_icon_v2.ico')

        self.bg_mainscreen = PhotoImage(
            file = r"backgrounds\bg_register.png"
        )

        # Background
        canvas = tk.Canvas(
            root, 
            width = 1280, 
            height = 720, 
            background = "red", 
            highlightthickness = 0
        )
        canvas.pack()
        canvas.create_image(
            0, 
            0, 
            image = self.bg_mainscreen, 
            anchor = "nw"
        )

        # Background Label
        bg_label = tk.Label(
            self.root, 
            border = 0, 
            bg = "red", 
            image = self.bg_mainscreen
        )
        bg_label.pack(
            fill = BOTH, 
            expand = True
        )

        self.var_keyID = StringVar() # ID
        self.var_ID = StringVar() # Employee ID
        self.var_lastName = StringVar() # Last Name
        self.var_firstname = StringVar() # First Name
        self.var_middleI = StringVar()  # Middle Initial
        self.var_gender = StringVar() # Gender
        self.var_email = StringVar() # Email
        self.var_phone = StringVar() # Phone No.
        self.var_address = StringVar() # Address
        self.var_photo = StringVar() # Photo

        # Entry Pane
        # --- Employee ID
        self.imgu.setup_textbox(
            self.root,
            canvas = canvas,
            variable = self.var_ID,
            x = 136,
            y = 125,
            width = 15  # Override default width
        )

        # --- Last Name
        self.imgu.setup_textbox(
            self.root,
            canvas = canvas,
            variable = self.var_lastName,
            x = 136,
            y = 191,
            width = 15  # Override default width
        )

        # --- First Name
        self.imgu.setup_textbox(
            self.root,
            canvas = canvas,
            variable = self.var_firstname,
            x = 136,
            y = 257,
            width = 15  # Override default width
        )

        # --- Middle Initial
        self.imgu.setup_textbox(
            self.root,
            canvas = canvas,
            variable = self.var_middleI,
            x = 136,
            y = 324,
            width = 15  # Override default width
        )

        # --- E-mail
        self.imgu.setup_textbox(
            self.root,
            canvas = canvas,
            variable = self.var_email,
            x = 136,
            y = 392,
            width = 15  # Override default width
        )

        # --- Contact Number
        self.imgu.setup_textbox(
            self.root,
            canvas = canvas,
            variable = self.var_phone,
            x = 136,
            y = 458,
            width = 15  # Override default width
        )

        # --- Address
        self.imgu.setup_textbox(
            self.root,
            canvas = canvas,
            variable = self.var_address,
            x = 136,
            y = 525,
            width = 15  # Override default width
        )

        # --- Gender
        self.imgu.setup_combobox(
            self.root,
            canvas = canvas,
            variable = self.var_gender,
            values = (" Select Gender", " Male", " Female"),
            x = 136,
            y = 596
        )

        # --- Key ID
        self.imgu.setup_textbox(
            self.root,
            canvas = canvas,
            variable = self.var_keyID,
            x = 196,
            y = 89,
            width = 3  # Override default width
        )

        # Search Pane
        # --- Search combobox
        self.var_search = StringVar()
        self.imgu.setup_combobox(
            self.root,
            canvas = canvas,
            variable = self.var_search,
            x = 359,
            y = 123,
            width = 14,  # Override default width
            values = (" Search by", " Last Name", " First Name", " Employee ID"),  # Override default values
            config = {"background": "black"}  # Additional configurations
        )

        # --- Search textbox
        self.var_search_entry = StringVar()
        self.imgu.setup_textbox(
            self.root,
            canvas = canvas,
            variable = self.var_search_entry,
            x = 565,
            y = 123,
            width = 10,  # Override default width
            bd = 0       # Override default bd
        )

        # V2 Buttons
        # --- Save
        self.imgu.setup_button_v2(
            root = self.root,
            img_path = r"buttons\save.png",
            x = 270,
            y = 550,
            width = 150,
            height = 75,
            command = self.insert
        )

        # --- Update
        self.imgu.setup_button_v2(
            root = self.root,
            img_path = r"buttons\update.png",
            x = 420,
            y = 550,
            width = 150,
            height = 75,
            command = self.update_data
        )

        # --- Delete
        self.imgu.setup_button_v2(
            root = self.root,
            img_path = r"buttons\delete.png",
            x = 570,
            y = 550,
            width = 160,
            height = 75,
            command = self.delete
        )

        # --- Clear
        self.imgu.setup_button_v2(
            root = self.root,
            img_path = r"buttons\clear.png",
            x = 730,
            y = 550,
            width = 150,
            height = 75,
            command = self.clear
        )

        # V3 Buttons
        # --- Search
        self.imgu.setup_button_v3(
            root = self.root,
            img_path = r"buttons\search.png",
            x = 650,
            y = 106,
            img_width = 100,
            img_height = 50,
            button_width = 100,
            button_height = 40,
            command = self.search
        )

        # --- Reset
        self.imgu.setup_button_v3(
            root = self.root,
            img_path = r"buttons\reset.png",
            x = 750,
            y = 106,
            img_width = 100,
            img_height = 50,
            button_width = 100,
            button_height = 40,
            command = self.show_data
        )

        # V4 Buttons
        # --- Open Camera
        self.imgu.setup_button_v4(
            root = root,
            image_path_inactive = r"buttons/open_camera.png",
            image_path_active = r"buttons/open_camera.png",
            x = 870,
            y = 550,
            width = 150,
            height = 75,
            command = self.open_camera
        )

        # --- Exit 
        self.imgu.setup_button_v4(
            root = self.root,
            image_path_inactive = r"buttons/exit_data_inactive.png",
            image_path_active = r"buttons/exit_data_active.png",
            x = 1160,
            y = 560,
            width = 70,
            height = 70,
            command = self.close
        )

        # --- Photo Grid
        self.imgu.setup_button_v4(
            root = self.root,
            image_path_inactive = r"buttons/photos_inactive.png",
            image_path_active = r"buttons/photos_active.png",
            x = 1100,
            y = 560,
            width = 70,
            height = 70,
            command = self.photos
        )

        # --- Train
        self.imgu.setup_button_v4(
            root = self.root,
            image_path_inactive = r"buttons/train_inactive.png",
            image_path_active = r"buttons/train_active.png",
            x = 1040,
            y = 560,
            width = 70,
            height = 70,
            command = self.train
        )

        # --- Home
        self.imgu.setup_button_v4(
            root = self.root,
            image_path_inactive = r"buttons/home_inactive.png",
            image_path_active = r"buttons/home_active.png",
            x = 980,
            y = 560,
            width = 70,
            height = 70,
            command = self.home
        )
        

        # Table
        frame_DB = LabelFrame(
            root,
            bd = 0,
            bg = "white",
            relief = RIDGE,
            font = ("Franklin Gothic Demi", 12)
        )
        frame_DB.place(
            x = 293,
            y = 184,
            width = 910,
            height = 335
        )

        hor_scroll = ttk.Scrollbar(
            frame_DB,
            orient = HORIZONTAL
        )
        ver_scroll = ttk.Scrollbar(
            frame_DB,
            orient = VERTICAL
        )

        self.table = ttk.Treeview(
            frame_DB,
            columns = (
                "ID", "Last Name", "First Name", "Middle Initial",
                "Gender", "E-mail", "Phone No.", "Address", "Photo",
                "Employee ID"
            ),
            xscrollcommand = hor_scroll.set,
            yscrollcommand = ver_scroll.set
        )

        hor_scroll.config(command = self.table.xview)
        ver_scroll.config(command = self.table.yview)

        hor_scroll.pack(
            side = BOTTOM,
            fill = X
        )
        ver_scroll.pack(
            side = RIGHT,
            fill = Y
        )

        self.table.heading("ID", text = "ID")
        self.table.heading("Last Name", text = "Last Name")
        self.table.heading("First Name", text = "First Name")
        self.table.heading("Middle Initial", text = "Middle Initial")
        self.table.heading("Gender", text = "Gender")
        self.table.heading("E-mail", text = "E-mail")
        self.table.heading("Phone No.", text = "Phone No.")
        self.table.heading("Address", text = "Address")
        self.table.heading("Photo", text = "Photo")
        self.table.heading("Employee ID", text = "Employee ID")
        self.table["show"] = "headings"

        self.table.column("ID", anchor = CENTER, width = 10)
        self.table.column("Last Name", anchor = CENTER, width = 120)
        self.table.column("First Name", anchor = CENTER, width = 120)
        self.table.column("Middle Initial", anchor = CENTER, width = 120)
        self.table.column("Gender", anchor = CENTER, width = 80)
        self.table.column("E-mail", anchor = CENTER, width = 190)
        self.table.column("Phone No.", anchor = CENTER, width = 90)
        self.table.column("Address", anchor = CENTER, width = 170)
        self.table.column("Photo", anchor = CENTER, width = 150)
        self.table.column("Employee ID", anchor = CENTER, width = 160)

        self.table.pack(
            fill = BOTH,
            expand = 1
        )
        self.table.bind("<ButtonRelease>", self.get_cursor)
        self.show_data()

    # Main Functions
    def home(self):
        self.root.destroy()

    def photos(self):
        self.new_window = Toplevel(self.root)
        self.photos_screen = Photos(self.new_window)

    def close(self):
        sys.exit()

    def train(self):
        train_mode = messagebox.askyesno("Attentiface V 1.0",
                                         "Are you sure you want to register the data?",
                                         parent = self.root)
        if train_mode > 0:
            self.new_window = Toplevel(self.root)
            self.second_new_window = Toplevel(self.root)
            self.train_screen = Train(self.new_window, self.second_new_window)
        else:
            if not train_mode:
                return
    
    # CRUD Functions
    # --- Insert
    def insert(self):
        if self.var_lastName.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Attentiface V 1.0",
                                 "Please fill-in all the required fields",
                                 parent = self.root)
        else:
            columns = [
                "last_name",
                "first_name",
                "middle_initial",
                "gender",
                "email",
                "phone_number",
                "address",
                "photo_last_taken",
                "employee_id"
            ]
            values = (
                self.var_lastName.get(),
                self.var_firstname.get(),
                self.var_middleI.get(),
                self.var_gender.get(),
                self.var_email.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_photo.get(),
                self.var_ID.get())
            
            database = r"databases\Attentiface.db"
            table = "Employee"
            self.q.insert(database,
                          table,
                          columns,
                          values,
                          self.root)

            data = self.q.read(database,
                               table)
            lr = int(len(data)) + 1
            self.var_keyID.set(lr)

            self.show_data()

    # --- Update
    def update_data(self):
        if self.var_lastName.get() == "" or self.var_ID.get() == "":
            messagebox.showerror("Attentiface V 1.0",
                                 "Please fill-in all the required fields",
                                 parent = self.root)
        else:
            update_mode = messagebox.askyesno("Attentiface V 1.0", 
                                              "Are you sure you want to update this entry?",
                                              parent = self.root)
            if update_mode > 0:
                columns = [
                    "last_name",
                    "first_name",
                    "middle_initial",
                    "gender",
                    "email",
                    "phone_number",
                    "address",
                    "photo_last_taken",
                    "employee_id"
                ]
                values = (
                    self.var_lastName.get(),
                    self.var_firstname.get(),
                    self.var_middleI.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_photo.get(),
                    self.var_ID.get())
                
                database = r"databases\Attentiface.db"
                table = "Employee"
                self.q.update(database,
                              table,
                              columns,
                              values,
                              on_key = self.var_keyID.get(),
                              root = self.root)
            else:
                if not update_mode:
                    return
                
            self.show_data()

    # --- Delete
    def delete(self):
        if self.var_ID.get() == "":
            messagebox.showerror("Attentiface V 1.0",
                                 "Select an entry to delete",
                                 parent = self.root)
        else:
            delete_mode = messagebox.askyesno("Attentiface V 1.0",
                                              "Are you sure you want to delete this data?",
                                              parent = self.root)
            if delete_mode > 0:
                database = r"databases\Attentiface.db"
                table = "Employee"
                self.q.delete(database,
                              table,
                              on_key = self.var_keyID.get(),
                              root = self.root)
            else:
                if not delete_mode:
                    return
                
            self.show_data()

    # --- Clear
    def clear(self):
        self.var_ID.set(""),
        self.var_lastName.set(""),
        self.var_gender.set(" Select Gender"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_photo.set(""),
        self.var_firstname.set(""),
        self.var_middleI.set(""),
        self.var_keyID.set("") 

    # --- Search
    def search(self):
        if self.var_search.get() == "" or self.var_search_entry.get() == "":
            messagebox.showerror("Attentiface V 1.0",
                                 "Please fill in the search details")
        else:
            database = r"databases\Attentiface.db"
            table = "Employee"
            data = self.q.search(database,
                          table,
                          search_key = self.var_search.get(),
                          search_string = self.var_search_entry.get(),
                          root = root)
            
            if len(data) != 0:
                self.table.delete(*self.table.get_children())
                for i in data:
                    self.table.insert("",
                                    END,
                                    values = i)

    # Supplement Functions
    # --- Populate table with data
    def show_data(self):
        database = r"databases\Attentiface.db"
        table = "Employee"
        data = self.q.read(database,
                    table)

        if len(data) != 0:
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert("",
                                  END,
                                  values = i)
        else:
            self.table.delete(*self.table.get_children())

        self.var_search.set(" Search by")
        self.var_search_entry.set("")

    # --- Populate entry boxes and combo boxes with selected data
    def get_cursor(self, event = ""):
        cursor_focus = self.table.focus()
        content = self.table.item(cursor_focus)
        data = content["values"]
        
        if data is not None:
            self.var_ID.set(data[9]),
            self.var_lastName.set(data[1]),
            self.var_firstname.set(data[2]),
            self.var_middleI.set(data[3]),
            self.var_gender.set(data[4]),
            self.var_email.set(data[5]),
            self.var_phone.set(data[6]),
            self.var_address.set(data[7]),
            self.var_photo.set(data[8]),
            self.var_keyID.set(data[0])
        else:
            pass     
    
    # Camera Functions
    # --- Open camera
    def open_camera(self):
        self.new_window = Toplevel(self.root)
        self.camera_screen = Camera(self.new_window)

    # --- Take photos
    def take_photos(self):
        if self.var_lastName.get() == "" or self.var_ID.get() == "" or self.var_keyID == "":
            messagebox.showerror("Attentiface V 1.0",
                                 "Please select a record first",
                                 parent = self.root)
        else:
            try:
                take_pic = messagebox.askyesno("Attentiface V 1.0", 
                                               "Are you sure you want to take a photo?",
                                               parent = self.root)
                if take_pic > 0:
                    self.new_window.destroy()

                    # 1. update entry's phot_last_taken
                    now = datetime.now()
                    current_time = self.dtu.twentyfour_to_twelve(now.time())
                    current_date = str(now.date())

                    columns = [
                        "last_name",
                        "first_name",
                        "middle_initial",
                        "gender",
                        "email",
                        "phone_number",
                        "address",
                        "photo_last_taken",
                        "employee_id"
                    ]
                    values = (
                        self.var_lastName.get(),
                        self.var_firstname.get(),
                        self.var_middleI.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        f"{current_date}, {current_time}",
                        self.var_ID.get())
                    
                    database = r"databases\Attentiface.db"
                    table = "Employee"
                    self.q.update(database,
                                    table,
                                    columns,
                                    values,
                                    on_key = self.var_keyID.get(),
                                    root = self.root)

                    # 2. collect face photos
                    self.new_window = Toplevel(self.root)
                    self.camera = Camera(self.new_window)
                    self.camera.take_photos(self.var_ID.get(),
                                            self.var_keyID.get(),
                                            self.root)
                else:
                    if not take_pic:
                        return
            except Exception as es:
                messagebox.showerror("Attentiface V 1.0",
                                     f"Error: {str(es)}",
                                     parent = self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()