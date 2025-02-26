from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import csv
import sqlite3
from time import strftime
from datetime import datetime

from utils.utilities import image_utils as imgu, datetime_utils as dtu
from host import Host
from summary import Summary
from queries import Queries

stop = 0

class Attendance:
    def __init__(self, root):
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
        self.root.wm_attributes("-transparentcolor", "red")
        self.root.overrideredirect(1)
        self.root.iconbitmap(r'logos\attentiface_icon_v2.ico')

        # Background
        self.bg = PhotoImage(
             file = r"backgrounds/bg_attendance.png")
        canvas = tk.Canvas(
             root, 
             width = 1280, 
             height = 720, 
             background = "red",
             highlightthickness = 0)
        canvas.pack()
        canvas.create_image(
             0,0, 
             image = self.bg,
             anchor = "nw")
        
        # Background Label
        bg_label = tk.Label(
             self.root, 
             border = 0, 
             bg = "red",
             image = self.bg)
        bg_label.pack(
             fill = BOTH, 
             expand = True)

        # Move app
        def move_app(self, e):
            root.geometry(f'+{e.x_root}+{e.y_root}')

        bg_label.bind("<B1-Motion>", move_app)
    
        # Table
        frame_DB = LabelFrame(
            root,
            bd = 0,
            bg = "white",
            relief = RIDGE,
            font = ("Franklin Gothic Demi", 12)
        )
        frame_DB.place(
            x = 67,
            y = 137,
            width = 1168,
            height = 383
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
            columns = ("ID", "Employee ID", "Last Name", "First Name", 
                       "Middle Initial", "Time In", "Time Out", "Date"),
            xscrollcommand = hor_scroll.set,
            yscrollcommand = ver_scroll.set
        )

        hor_scroll.config(
            command = self.table.xview
        )
        ver_scroll.config(
            command = self.table.yview
        )

        hor_scroll.pack(
            side = BOTTOM,
            fill = X
        )
        ver_scroll.pack(
            side = RIGHT,
            fill = Y
        )

        self.table.heading("ID", text = "ID")
        self.table.heading("Employee ID", text = "Employee ID")
        self.table.heading("Last Name", text = "Last Name")
        self.table.heading("First Name", text = "First Name")
        self.table.heading("Middle Initial", text = "Middle Initial")
        self.table.heading("Time In", text = "Time In")
        self.table.heading("Time Out", text = "Time Out")
        self.table.heading("Date", text = "Date")

        self.table["show"] = "headings"

        self.table.column("ID", anchor = CENTER, width = 10)
        self.table.column("Employee ID", anchor = CENTER, width = 160)
        self.table.column("Last Name", anchor = CENTER, width = 120)
        self.table.column("First Name", anchor = CENTER, width = 120)
        self.table.column("Middle Initial", anchor = CENTER, width = 120)
        self.table.column("Time In", anchor = CENTER, width = 140)
        self.table.column("Time Out", anchor = CENTER, width = 140)
        self.table.column("Date", anchor = CENTER, width = 90)

        self.table.pack(
            fill = BOTH,
            expand = 1
        )
        self.table.bind("<ButtonRelease>")
        self.show_data()

        # V1 Buttons
        # --- Exit
        self.imgu.setup_button(
            root = root,
            img_path_inactive = r"buttons\exit_data_inactive.png",
            img_path_active = r"buttons\exit_data_active.png",
            button_x = 1160,
            button_y = 555,
            button_width = 70,
            button_height = 70,
            img_width = 70,
            img_height = 70,
            command = self.close
        )

        # --- Home
        self.imgu.setup_button(
            root = root,
            img_path_inactive = r"buttons\home_inactive.png",
            img_path_active = r"buttons\home_active.png",
            button_x = 1100,
            button_y = 555,
            button_width = 70,
            button_height = 70,
            img_width = 70,
            img_height = 70,
            command = self.home
        )

        # V2 Buttons
        # --- Search
        self.imgu.setup_button_v2(
            root = root,
            img_path = r"buttons\search.png",
            x = 256,
            y = 567,
            width = 100,
            height = 50,
            command = self.search,
            bg = "white",
            borderwidth = 0,
            highlightthickness = 0,
            bd = 0,
            relief = "raised",
            activebackground = "white"
        )

        self.imgu.setup_button_v2(
            root,
            img_path = r"buttons\reset.png",
            x = 358,
            y = 567,
            width = 100,
            height = 50,
            command = self.show_data,
            bg = "white",
            borderwidth = 0,
            highlightthickness = 0,
            bd = 0,
            relief = "raised",
            activebackground = "white"
        )

        # --- Export
        self.imgu.setup_button_v2(
            root,
            img_path = r"buttons\export.png",
            x = 660,
            y = 550,
            width = 160,
            height = 80,
            command = self.export_to_csv,
            bg = "white",
            borderwidth = 0,
            highlightthickness = 0,
            bd = 0,
            relief = "raised",
            activebackground = "white"
        )

        # --- Send email
        self.imgu.setup_button_v2(
            root,
            img_path = r"buttons\send_email.png",
            x = 820,
            y = 550,
            width = 160,
            height = 80,
            command = self.send_attendance_summary,
            bg = "white",
            borderwidth = 0,
            highlightthickness = 0,
            bd = 0,
            relief = "raised",
            activebackground = "white"
        )

        # V3 Buttons
        # --- Change host credentials
        self.imgu.setup_button_v3(
            root = root,
            img_path = r"buttons\change_email.png",
            x = 980,
            y = 550,
            img_width = 160,
            img_height = 80,
            button_width = 130,
            button_height = 80,
            command = self.add_update_host_credentials,
            bg = "white",
            borderwidth = 0,
            highlightthickness = 0,
            bd = 0,
            relief = "raised",
            activebackground = "white"
        )

        # --- Save time
        self.imgu.setup_button_v3(
            root = root,
            img_path = r"buttons\save_v2.png",
            x = 1108,
            y = 86,
            img_width = 70,
            img_height = 35,
            button_width = 70,
            button_height = 30,
            command = self.update_timebounds,
            bg = "white",
            borderwidth = 0,
            highlightthickness = 0,
            bd = 0,
            relief = "raised",
            activebackground = "white"
        )

        # --- Delete all attendance data
        self.imgu.setup_button_v3(
            root = root,
            img_path = r"buttons\delete_all.png",
            x = 1180,
            y = 86,
            img_width = 70,
            img_height = 35,
            button_width = 70,
            button_height = 30,
            command = self.delete_all_records,
            bg = "white",
            borderwidth = 0,
            highlightthickness = 0,
            bd = 0,
            relief = "raised",
            activebackground = "white"
        )

        # Text box
        # --- Search
        self.var_search_entry = StringVar()
        self.imgu.setup_textbox(
            root = root,
            canvas = canvas,
            variable = self.var_search_entry,
            x = 164,
            y = 597,
            width = 14,
            bd = 0
        )

        # --- Start time
        self.var_start_entry = StringVar()
        self.imgu.setup_textbox(
            root = root,
            canvas = canvas,
            variable = self.var_start_entry,
            x = 682,
            y = 101,
            width = 7,
            bd = 0
        )

        # --- End time
        self.var_end_entry = StringVar()
        self.imgu.setup_textbox(
            root = root,
            canvas = canvas,
            variable = self.var_end_entry,
            x = 863,
            y = 101,
            width = 7,
            bd = 0
        )

        # --- Break time
        self.var_break_entry = StringVar()
        self.imgu.setup_textbox(
            root = root,
            canvas = canvas,
            variable = self.var_break_entry,
            x = 1058,
            y = 101,
            width = 7,
            bd = 0
        )

        # Supplemental
        # --- Clock widget
        self.clock_widget = tk.Label(
            root,
            font = ('Montserrat', 21, 'bold'),
            background = 'white',
            foreground = 'black',
            bd = 0,
            activebackground = "white")
        self.clock_widget.place(
            x = 500,
            y = 584)
        
        self.clock()
        self.show_data()
    
    # Main Functions
    def home(self):
        self.root.destroy()

    def close(self):
        self.root.destroy()

    # CRUD Functions
    # --- Search
    def search(self):
        if self.var_search_entry.get() == "":
            messagebox.showerror("Attentiface V 1.0",
                                 "Please fill in the surname", 
                                 parent = self.root)
        else:
            database = r"databases\Attentiface.db"
            table = "Attendance"
            data = self.q.search(database,
                          table,
                          search_key = "last_name",
                          search_string = self.var_search_entry.get(),
                          root = root)
            
            if len(data) != 0:
                self.table.delete(*self.table.get_children())
                for i in data:
                    self.table.insert("",
                                    END,
                                    values = i)
                    
    # Supplemental Functions
    # --- Populate table with data
    def show_data(self):
        database = r"databases\Attentiface.db"
        table = "Attendance"
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

    # --- Creates a clock widget
    def clock(self):
        string = strftime('%I:%M %p')
        self.clock_widget.config(text = f"{string}")
        self.clock_widget.after(1000, self.clock)

    # --- Add or update a host credentials for sending attendance summary to gmails
    def add_update_host_credentials(self):
        self.new_window = Toplevel(self.root)
        self.host_screen = Host(self.new_window)

    # --- Send attendnace summary to email
    def send_attendance_summary(self):
        send_email_mode = messagebox.askyesno("Attentiface V 1.0", 
                                              "Are you sure you want to send summaries now?",
                                              parent = self.root)
        if send_email_mode > 0:
            self.new_window = Toplevel(self.root)
            self.second_window = Toplevel(self.root)
            self.summary_screen = Summary(self.new_window, self.second_window)
        else:
            if not send_email_mode:
                return
            
    # --- Export attendance data to csv
    def export_to_csv(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension = '.csv',
            filetypes = [("CSV Files", "*.csv")], parent = self.root)
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", 
                             "Employee ID",
                             "Last Name",
                             "First Name",
                             "Middle Initial",
                             "Time In", 
                             "Time Out", 
                             "Date"])
            for row_id in self.table.get_children():
                row = self.table.item(row_id)['values']
                writer.writerow(row)
        messagebox.showinfo("Attentiface V 1.0",
                            "Successfully exported file",
                            parent = self.root)

    # --- save start_time, end_time and break_time
    def update_timebounds(self):
        if self.var_start_entry.get() == "" or self.var_end_entry.get() == "":
            messagebox.showerror("Attentiface V 1.0",
                                 "Please fill-in all the required fields",
                                 parent = self.root)
        else:
            # Convert to 24 hour time with seconds default to 0
            time_bounds = self.dtu.twelve_to_twentyfour(
                time_list = [str(self.var_start_entry.get()),
                                str(self.var_end_entry.get())]
            )

            database = r"databases\Attentiface.db"
            table = "Schedule"
            self.q.update(
                database,
                table,
                columns = ["start_time", "end_time", "break_time"],
                values = [time_bounds[0], time_bounds[1], self.var_break_entry.get()],
                on_key = 1,
                root = self.root
            )
    
    # --- delete all attendance records
    def delete_all_records(self):
        delete_mode = messagebox.askyesno("Attentiface V 1.0", 
                                          "Are you sure you want to delete all attendance records? Please make sure you have a copy before deleting",
                                          parent = self.root)
        
        if delete_mode > 0:
            database = r"databases\Attentiface.db"
            table = "Attendance"
            self.q.delete_all(database,
                              table,
                              self.root)
            messagebox.showinfo("Attentiface V 1.0", 
                                "Successfully deleted all data",
                                parent = self.root)
        else:
            if not delete_mode:
                return
            
        self.show_data()

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()