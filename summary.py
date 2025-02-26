from tkinter import *
from tkinter import messagebox

from time import strftime
from datetime import datetime, timedelta
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import os
import six
import threading
import yagmail

from utils.utilities import animation_utils as animu
from done import Done
from queries import Queries

class Summary:
    def __init__(self, root, second_root = None):
        self.root = root
        self.second_root = second_root
        self.animu = animu(self.root)
        self.q = Queries()

        # Configurations
        window_width = 350
        window_height = 350
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x_coor = (screen_width / 2) - (window_width / 2)
        y_coor = (screen_height / 2) - (window_height / 2)
        self.root.geometry(f'{window_width}x{window_height}+{int(x_coor)}+{int(y_coor)}')
        self.root.wm_attributes("-transparentcolor","red")
        self.root.overrideredirect(1)

        t1 = threading.Thread(
            target = self.animu.load_screen("loading_animations/loading_email.gif", self.stop)
            )
        t1.start()

        t2 = threading.Thread(
            target = self.send_summary_to_gmail
            )
        t2.start()   

    def send_summary_to_gmail(self):

        self.calculate_time_summary()

        database = r"databases\Attentiface.db"
        table = "Credentials"
        credentials_data = self.q.read(
            database,
            table)
        
        if len(credentials_data) == 0:
            messagebox.showerror("Attentiface V 1.0",
                                 "No host email indicated")
            return
        
        else:
            
            database = r"databases\Attentiface.db"
            table = "Employee"
            employee_data = self.q.read(
                database,
                table
            )
            for record in credentials_data:
                try:
                    yag = yagmail.SMTP(str(record[1]), str(record[2]))

                    for record in employee_data:
                        yag.send(
                            to = str(record[0]),
                            subject = "Employee Summary Information",
                            contents = f"Greetings {record[1]}, Here is your attendance summary",
                            attachments = f"Summary_Information/Employee {record[1]}.png"
                    )
                except Exception as es:
                    messagebox.showerror("Attentiface V 1.0",
                                         f"Error: {str(es)}")
                    
        self.animu.stop_animation = True

    def calculate_time_summary(self):

        database = r"database\Attentiface.db"
        table = "Employee"
        columns = ["ID", "email", "employee_id"]
        employee_data = self.q.read_v2(database,
                       table,
                       columns = columns)

        for employee in employee_data:

            table = "Attendance"
            columns = ["date", "time_in", "time_out", "secondary_id"]
            attendance_data = self.q.read_v2(database,
                                    table,
                                    columns = columns
                                    )
            table = "Schedule"
            columns = ["start_time", "end_time", "break_time"]
            time_bounds = self.q.read_v2(database,
                                         table,
                                         columns = columns,
                                         row_specific = True,
                                         column_key = "ID",
                                         id = 1
                                         )
            
            if len(attendance_data) > 0:
                df = pd.DataFrame(
                    columns = ["Date", "Time In", "Time Out", "Break Time (Start)", 
                               "Break Time (End)" , "Total Time", "Overtime"])
                
                count = 0
                for record in attendance_data:
                    time_in = record[1]
                    time_out = record[2]
                    FMT = '%H:%M:%S'

                    tdeltaSTART = datetime.strptime(time_bounds[0][0], FMT)
                    tdeltaEND = datetime.strptime(time_bounds[0][1], FMT)
                    tdeltaTIMEIN =  datetime.strptime(time_in, FMT)
                    tdeltaTIMEOUT = datetime.strptime(time_out, FMT)

                    tdelta = min(tdeltaTIMEOUT, tdeltaEND) - max(tdeltaTIMEIN, tdeltaSTART)

                    if max(tdeltaTIMEIN, tdeltaSTART) > min(tdeltaTIMEOUT, tdeltaEND):
                        tdelta = "00:00:00"

                    summary_list = list(record)
                    summary_list.insert(3, str(tdelta))

                    # --- Break Time
                    
                    tdeltaBREAK = time_bounds[0][2]
                    match = re.match(r"(\d+)\s*(min(?:ute)?s?)", tdeltaBREAK, re.IGNORECASE)
                    if match:
                        duration = int(match.group(1))
                    else:
                        start = tdeltaBREAK[:tdeltaBREAK.index("-")].strip()
                        end = tdeltaBREAK[tdeltaBREAK.index("-") + 1 : ].strip()

                        start_time = datetime.strptime(start, "%I:%M %p").time()
                        end_time = datetime.strptime(end, "%I:%M %p").time()

                        summary_list.insert(3, str(start_time))
                        summary_list.insert(4, str(end_time))

                    # --- Overtime

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

                    if tdeltaTIMEOUT > tdeltaEND:
                        Nortime = tdeltaTIMEIN - tdeltaEND
                        if (Nortime >= time_maxEnd) and (max(tdeltaTIMEIN, tdeltaSTART) < min(tdeltaTIMEOUT, tdeltaEND)):
                            summary_list.insert(6, str(Nortime))
                        else:
                            summary_list.insert(6, '00:00:00')
                    else:
                        summary_list.insert(6, '00:00:00')
                    df.loc[count] = summary_list[0:7]
        
                    count = count + 1

            self.render_mpl_table(data = df,
                                  employee = employee,
                                  header_columns = 0, 
                                  col_width = 3.0)

    def render_mpl_table(self, 
                         data,
                         employee,
                         col_width = 3.0, 
                         row_height = 0.625, 
                         font_size = 14,
                         header_color = '#000000', 
                         row_colors = ['#f1f1f2', 'w'], 
                         edge_color = 'w',
                         bbox = [0, 0, 1, 1], 
                         header_columns = 0,
                         ax = None, 
                         **kwargs):
        
        if ax is None:
            size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
            fig, ax = plt.subplots(figsize=size)
            ax.axis('off')

        mpl_table = ax.table(
            cellText = data.values, 
            bbox = bbox, 
            colLabels = data.columns, 
            **kwargs)
        mpl_table.auto_set_font_size(False)
        mpl_table.set_fontsize(font_size)

        for k, cell in  six.iteritems(mpl_table._cells):
            cell.set_edgecolor(edge_color)
            if k[0] == 0 or k[1] < header_columns:
                cell.set_text_props(
                    weight ='bold', 
                    color = 'w')
                cell.set_facecolor(header_color)
            else:
                cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
                
        directory = "Summary_Information"
        filename = f"Employee {employee[2]}.png"
        filepath = os.path.join(directory, filename)
        plt.savefig(filepath)

        return ax

    def stop(self):
        self.root.destroy()
        self.new_window = self.second_root
        self.done_screen = Done(self.new_window, "icons\emails_sent.png")

if __name__ == "__main__":
    root = Tk()
    obj = Summary(root)
    root.mainloop()
