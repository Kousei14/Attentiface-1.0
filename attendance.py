from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import sqlite3
from time import strftime
from queries import DB_Credentials
import csv
from tkinter import filedialog
from tkinter import messagebox
from datetime import datetime
from splash_email import loadEmail
from itertools import count
import yagmail
import pandas as pd
import re
import matplotlib.pyplot as plt
import os
import six
from datetime import datetime, timedelta
import numpy as np
import threading


stop=0

class Attendance_screen:
    def __init__(self, root):
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
        self.root.iconbitmap('attentiface_icon.ico')

        self.var_search_entry = StringVar()

        def move_app(self,e):
            root.geometry(f'+{e.x_root}+{e.y_root}')

        self.bg_mainscreen = PhotoImage(file="bg_attendance.png")
        canvas = tk.Canvas(root, width=1280, height=720, background="red",highlightthickness=0)
        canvas.pack()
        canvas.create_image(0,0, image=self.bg_mainscreen ,anchor="nw")
        
        bg_label = tk.Label(self.root, border=0, bg="red",image=self.bg_mainscreen)
        bg_label.pack(fill=BOTH, expand=True)

        bg_label.bind("<B1-Motion>", move_app)
    
    #Database TABLE in the app

        frame_DB=LabelFrame(root,bd=0,bg="white",relief=RIDGE,font=("Franklin Gothic Demi",12))
        frame_DB.place(x=67,y=137,width=1168,height=383)

        hor_scroll=ttk.Scrollbar(frame_DB,orient=HORIZONTAL)
        ver_scroll=ttk.Scrollbar(frame_DB,orient=VERTICAL)

        self.student_table=ttk.Treeview(frame_DB,columns=("ID", "Employee ID","Last Name","First Name","Middle Initial","Time In", "Time Out", "Date"),xscrollcommand=hor_scroll.set, yscrollcommand=ver_scroll.set)

        hor_scroll.config(command=self.student_table.xview)
        ver_scroll.config(command=self.student_table.yview)

        hor_scroll.pack(side=BOTTOM,fill=X)
        ver_scroll.pack(side=RIGHT,fill=Y)
        hor_scroll.config(command=self.student_table.xview)
        ver_scroll.config(command=self.student_table.yview)

        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Employee ID",text="Employee ID")
        self.student_table.heading("Last Name",text="Last Name")
        self.student_table.heading("First Name",text="First Name")
        self.student_table.heading("Middle Initial",text="Middle Initial")
        self.student_table.heading("Time In",text="Time In")
        self.student_table.heading("Time Out",text="Time Out")
        self.student_table.heading("Date",text="Date")
        
        self.student_table["show"]="headings"

        self.student_table.column("ID",anchor=CENTER,width=10)
        self.student_table.column("Employee ID",anchor=CENTER,width=160)
        self.student_table.column("Last Name",anchor=CENTER,width=120)
        self.student_table.column("First Name",anchor=CENTER,width=120)
        self.student_table.column("Middle Initial",anchor=CENTER,width=120)
        self.student_table.column("Time In",anchor=CENTER,width=140)
        self.student_table.column("Time Out",anchor=CENTER,width=140)
        self.student_table.column("Date",anchor=CENTER,width=90)

        #adjustable table

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>")

    #button exit
                
        img5_inactive=Image.open(r"pictures\exit_data_inactive.png")
        img5_inactive=img5_inactive.resize((70,70))

        img5_active=Image.open(r"pictures\exit_data_active.png")
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
        button_exit=Button(root,image=root.img5_inactive,border=0,borderwidth=0,width=80,highlightthickness=0,height=80,bd=0,relief="sunken",activebackground="white",command=self.close)
        button_exit.bind("<Enter>",on_enter_exit)
        button_exit.bind("<Leave>",on_inactive_exit)
        button_exit.bind("<Button-1>",pressed_exit)
        button_exit.bind("<ButtonRelease-1>",unpressed_exit)
        button_exit.place(x=1160,y=555,width=70,height=70)
    
    #button home
                
        img6_inactive=Image.open(r"pictures\home_inactive.png")
        img6_inactive=img6_inactive.resize((70,70))

        img6_active=Image.open(r"pictures\home_active.png")
        img6_active=img6_active.resize((80,80))

        root.img6_inactive=ImageTk.PhotoImage(img6_inactive)
        root.img6_active=ImageTk.PhotoImage(img6_active)

        def on_enter_home(event):
                    button_home.config(image=root.img6_active)
        def on_inactive_home(event):
                    button_home.config(image=root.img6_inactive)
        def pressed_home(event):
                    button_home.config(image=root.img6_inactive)
        def unpressed_home(event):
                    button_home.config(image=root.img6_active)
        button_home=Button(root,image=root.img6_inactive,border=0,borderwidth=0,width=80,highlightthickness=0,height=80,bd=0,relief="sunken",activebackground="white",command=self.home)
        button_home.bind("<Enter>",on_enter_home)
        button_home.bind("<Leave>",on_inactive_home)
        button_home.bind("<Button-1>",pressed_home)
        button_home.bind("<ButtonRelease-1>",unpressed_home)
        button_home.place(x=1100,y=555,width=70,height=70)
    
    #search
        img_search=Image.open(r"pictures\search.png")
        img_search=img_search.resize((100,50))

        root.img_search=ImageTk.PhotoImage(img_search)
        button_search=Button(root,image=root.img_search,textvariable=self.var_search_entry,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white",command=self.search)
        button_search.place(x=256,y=567,width=100,height=50)

        #Search entry
        self.var_search_entry=StringVar()
        Search_txt=tk.Entry(root,textvariable=self.var_search_entry,width=14,bd=0,font=("Montserrat",12, "bold"))
        canvas.create_window(164, 597, window=Search_txt)

    #reset
        img_reset=Image.open(r"pictures\reset.png")
        img_reset=img_reset.resize((100,50))

        root.img_reset=ImageTk.PhotoImage(img_reset)
        button_reset=Button(root,image=root.img_reset,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white",command=self.show_data)
        button_reset.place(x=358,y=567,width=100,height=50)
    
    #export
        img_export=Image.open(r"pictures\export.png")
        img_export=img_export.resize((160,80))

        root.img_export=ImageTk.PhotoImage(img_export)
        button_export=Button(root,image=root.img_export,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white",command=self.export_csv)
        button_export.place(x=660,y=550,width=160,height=80)

    #send email
        img_email=Image.open(r"pictures\send_email.png")
        img_email=img_email.resize((160,80))

        root.img_email=ImageTk.PhotoImage(img_email)
        button_email=Button(root,image=root.img_email,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white",command=self.send_mail)
        button_email.place(x=820,y=550,width=160,height=80)

    #change email
        img_change_email=Image.open(r"pictures\change_email.png")
        img_change_email=img_change_email.resize((160,80))

        root.img_change_email=ImageTk.PhotoImage(img_change_email)
        button_change_email=Button(root,image=root.img_change_email,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white", command=self.cMail)
        button_change_email.place(x=980,y=550,width=130,height=80)

    #Start Entry
        self.var_start_entry=StringVar()
        start_txt=tk.Entry(root,textvariable=self.var_start_entry,width=7,bd=0,font=("Montserrat",10, "bold"))
        canvas.create_window(682, 101, window=start_txt)

    #End Entry
        self.var_end_entry=StringVar()
        end_txt=tk.Entry(root,textvariable=self.var_end_entry,width=7,bd=0,font=("Montserrat",10, "bold"))
        canvas.create_window(863, 101, window=end_txt)

    #Break Entry
        self.var_break_entry=StringVar()
        break_txt=tk.Entry(root,textvariable=self.var_break_entry,width=7,bd=0,font=("Montserrat",10, "bold"))
        canvas.create_window(1058, 101, window=break_txt)

    #Save time
        img_save=Image.open(r"pictures\save1.png")
        img_save=img_save.resize((70,35))

        root.img_save=ImageTk.PhotoImage(img_save)
        button_saveimg_save=Button(root,image=root.img_save,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white",command=self.saveTime)
        button_saveimg_save.place(x=1108,y=86,width=70,height=30)

    #Delete all
        img_delete_all=Image.open(r"pictures\delete_all.png")
        img_delete_all=img_delete_all.resize((70,35))

        root.img_delete_all=ImageTk.PhotoImage(img_delete_all)
        button_delete_all=Button(root,image=root.img_delete_all,bg="white",borderwidth=0,width=200,highlightthickness=0,height=200,bd=0,relief="raised",activebackground="white",command=self.delAll)
        button_delete_all.place(x=1180,y=86,width=70,height=30)

    #clock
        def time():
            string = strftime('%I:%M %p')
            clock.config(text=f"{string}")
            clock.after(1000, time)
        clock = tk.Label(root,font = ('Montserrat', 21, 'bold'),
             background = 'white',
             foreground = 'black',
             bd=0,
             activebackground="white")
        clock.place(x=500,y=584)
        time()
    #------------------------------------------------
        self.show_data()

    def home(self):
        self.root.destroy()

    def close(self):
        self.root.destroy()

    def show_data(self):
        conn = sqlite3.connect("Attendance_Database")
        cursor = conn.cursor()
        cursor.execute("SELECT * from Attendance")
        data=cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        else:
            self.student_table.delete(*self.student_table.get_children())
              
        conn.close

    def search(self):
        if self.var_search_entry.get()=="":
            messagebox.showerror("Attentiface V 1.0","Please fill in the surname", parent=self.root)
        else:
            try:
               conn = sqlite3.connect("Attendance_Database")
               cursor = conn.cursor()
               word="Last_Name"
               sql_search= f""" SELECT * from Attendance WHERE {word} LIKE '%{str(self.var_search_entry.get())}%'"""
               cursor.execute(sql_search) 
               data=cursor.fetchall()
               
               if len(data)!=0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("",END,values=i)
                    conn.commit()
               conn.close()
            except Exception as es:
                messagebox.showerror("Attentiface V 1.0",f"Error: {str(es)}",parent=self.root)

    def cMail(self):
        self.new_window=Toplevel(self.root)
        self.DBCredentials_screen=DB_Credentials(self.new_window)

    def send_mail(self):
        validation = messagebox.askyesno("Attentiface V 1.0", "Are you sure you want to send e-mails now?",parent=self.root)
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
                    print("tapos")
                    stop=0
                    self.new_win.protocol("WM_DELETE_WINDOW", loadEmail(self.new_win))

            def sendGmail():
                conn = sqlite3.connect("Credentials_Database")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM credentials")
                row=cursor.fetchall()
                
                if len(row)==0:
                    messagebox.showerror("Attentiface V 1.0","You haven't provided an e-mail account yet!")
                    return
                else:
                    for i in row:
                        try:
                            yag = yagmail.SMTP(str(i[1]), str(i[2]))

                            conn1 = sqlite3.connect("face_recognition_software_system")
                            cursor1 = conn1.cursor()
                            cursor1.execute('SELECT E_mail, Employee_ID FROM student_details')
                            emails = cursor1.fetchall()

                            for email in emails:
                                yag.send(
                                    to = str(email[0]),
                                    subject = "Employee Summary Information",
                                    contents = f"Greetings {email[1]}, Here is your summary information",
                                    attachments = f"Summary_Information\Employee {email[1]}.png"
                            )
                            conn.commit()
                        except Exception as es:
                            messagebox.showerror("Attentiface V 1.0",f"Error: {str(es)}")
            def calculate():
                global stop
                conn1 = sqlite3.connect("face_recognition_software_system")
                cursor1 = conn1.cursor()
                cursor1.execute('SELECT ID, E_mail, Employee_ID FROM student_details')
                idd = cursor1.fetchall()

                conn1.close()

                for employee in idd:
                    conn = sqlite3.connect("Attendance_Database")
                    cursor = conn.cursor()
                    cursor.execute(f'SELECT date, Time_In, Time_Out, idd FROM Attendance WHERE idd={employee[0]}')
                    result = cursor.fetchall()

                    conn2 = sqlite3.connect("Credentials_Database")
                    cursor2 = conn2.cursor()
                    cursor2.execute(f'SELECT Start_time, End_time, Break_time FROM Time_limit WHERE ID={int(1)}')
                    time_limits = cursor2.fetchall()

                    if len(result)>0:
                        df = pd.DataFrame(columns=['Date', 'Time In', 'Time Out', "Break Time (Start)", "Break Time (End)" , 'Total Time', 'Overtime'])
                        count=0
                        for row in result:
                            s1 = row[1]
                            s2 = row[2]
                            FMT = '%H:%M:%S'

                            tdeltaSTART = datetime.strptime(time_limits[0][0], FMT)
                            tdeltaEND = datetime.strptime(time_limits[0][1], FMT)
                            tdeltas1 =  datetime.strptime(s1, FMT)
                            tdeltas2 = datetime.strptime(s2, FMT)

                            tdelta = min(tdeltas2,tdeltaEND) - max(tdeltas1,tdeltaSTART)

                            if max(tdeltas1,tdeltaSTART) > min(tdeltas2,tdeltaEND):
                                tdelta="00:00:00"

                            summary_list = list(row)
                            
                            summary_list.insert(3, str(tdelta))

                            #Break Time
                            
                            tdeltaBREAK = time_limits[0][2]
                            match = re.match(r"(\d+)\s*(min(?:ute)?s?)", tdeltaBREAK, re.IGNORECASE)
                            if match:
                                duration = int(match.group(1))
                            else:
                                start = tdeltaBREAK[:tdeltaBREAK.index("-")].strip()
                                end = tdeltaBREAK[tdeltaBREAK.index("-")+1:].strip()

                                start_time = datetime.strptime(start, "%I:%M %p").time()
                                end_time = datetime.strptime(end, "%I:%M %p").time()

                                summary_list.insert(3, str(start_time))
                                summary_list.insert(4, str(end_time))

                            #Overtime

                            time_interval = "0 hours 30 minutes"
                            time_parts = time_interval.split()

                            time_dict = {}
                            for i in range(0, len(time_parts), 2):
                                if time_parts[i+1] in ['hours', 'hour']:
                                    time_dict['hours'] = int(time_parts[i])
                                elif time_parts[i+1] in ['minutes', 'minute']:
                                    time_dict['minutes'] = int(time_parts[i])
                                elif time_parts[i+1] in ['seconds', 'second']:
                                    time_dict['seconds'] = int(time_parts[i])
                            time_maxEnd = timedelta(**time_dict)

                            if tdeltas2 > tdeltaEND:
                                Nortime = tdeltas2 - tdeltaEND
                                if (Nortime >= time_maxEnd) and (max(tdeltas1,tdeltaSTART) < min(tdeltas2,tdeltaEND)):
                                    summary_list.insert(6, str(Nortime))
                                else:
                                    summary_list.insert(6, '00:00:00')
                            else:
                                summary_list.insert(6, '00:00:00')
                            df.loc[count] = summary_list[0:7]
                
                            count=count+1

                        def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
                                            header_color='#000000', row_colors=['#f1f1f2', 'w'], edge_color='w',
                                            bbox=[0, 0, 1, 1], header_columns=0,
                                            ax=None, **kwargs):
                            if ax is None:
                                size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
                                fig, ax = plt.subplots(figsize=size)
                                ax.axis('off')

                            mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
                            mpl_table.auto_set_font_size(False)
                            mpl_table.set_fontsize(font_size)

                            for k, cell in  six.iteritems(mpl_table._cells):
                                cell.set_edgecolor(edge_color)
                                if k[0] == 0 or k[1] < header_columns:
                                    cell.set_text_props(weight='bold', color='w')
                                    cell.set_facecolor(header_color)
                                else:
                                    cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
                                    
                            directory = "Summary_Information"
                            filename = f"Employee {employee[2]}.png"
                            filepath = os.path.join(directory, filename)
                            plt.savefig(filepath)

                            return ax

            
                        render_mpl_table(df, header_columns=0, col_width=3.0)
                    sendGmail()
                    stop=1
            gif_lb = tk.Label(self.new_win,bg="red",border=0)
            gif_lb.pack()
            
            extract_image_from_gif('loading_email.gif')

            t1 = threading.Thread(target=play_gif)
            t1.start()
            t2 = threading.Thread(target=calculate)
            t2.start()
            
        else:
            if not validation:
                return
            
    def export_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension='.csv',
                                        filetypes=[("CSV Files", "*.csv")],parent=self.root)
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Employee ID","Last Name","First Name","Middle Initial","Time In", "Time Out", "Date"])
            for row_id in self.student_table.get_children():
                row = self.student_table.item(row_id)['values']
                writer.writerow(row)
        messagebox.showinfo("Attentiface V 1.0","Successfully exported file",parent=self.root)

    def saveTime(self):
        if self.var_start_entry.get()=="" or self.var_end_entry.get()=="":
            messagebox.showerror("Attentiface V 1.0","Please fill-in all the required fields",parent=self.root)
        else:
            try:
                connection = sqlite3.connect('Credentials_Database')
                cursor = connection.cursor()

                # convert to 24 hour time with seconds default to 0
                time_list24=[]
                time_list12=[str(self.var_start_entry.get()),self.var_end_entry.get()]
                for tm in time_list12:
                    time_24 = datetime.strptime(tm, "%I:%M %p").strftime("%H:%M:%S")
                    if ':00' not in time_24:
                        time_24 = time_24 + ':00'
                    time_list24.append(time_24)

                #UPDATE DATA
                ID=1
                sql_update=f""" UPDATE Time_limit SET Start_time="{time_list24[0]}", End_time="{time_list24[1]}", Break_time="{self.var_break_entry.get()}" WHERE ID={ID} """
                cursor.execute(sql_update)
                
                for row in cursor.execute("SELECT * FROM Time_limit"):
                    print(row)
                messagebox.showinfo("Attentiface V 1.0","Successfully updated Start, End, and Break time")
            except Exception as es:
                messagebox.showerror("Attentiface V 1.0",f"Error: {str(es)}",parent=self.root)
        connection.commit()
        connection.close()
        
    def delAll(self):
        validation = messagebox.askyesno("Attentiface V 1.0", "Are you sure you want to delete all attendance records? Please make sure you have a copy before deleting",parent=self.root)
        if validation > 0:
            conn = sqlite3.connect("Attendance_Database")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Attendance")
            cursor.execute("DELETE FROM sqlite_sequence where name='Attendance'")
            conn.commit()
            messagebox.showinfo("Attentiface V 1.0", "Successfully deleted all data",parent=self.root)
        else:
            if not validation:
                return
        self.show_data()

if __name__ == "__main__":
    root=Tk()
    obj=Attendance_screen(root)
    root.mainloop()