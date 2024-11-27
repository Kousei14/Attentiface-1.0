from tkinter import*
import cv2 
import os
from datetime import datetime
import mediapipe as mp
import sqlite3

class Out:
    def __init__(self):

        cap=cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FPS, 60)
        cap.set(3, 640)
        cap.set(4, 480)

        imgBackground=cv2.imread("attendance_modes/attentiface_main.png")
        imgBackground_resized=cv2.resize(imgBackground, (1250,704))

        folderModePath="attendance_modes"
        modePathList=os.listdir(folderModePath)
        imgModeList=[]
        for path in modePathList:
            imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
        print(len(imgModeList))
        print(modePathList)


        faceCascade=mp.solutions.face_detection.FaceDetection(0.5)
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"detection_model\recognizer.xml")

        # Convert 24 hour time to 12 hour time
        def twentyfour_to_twelve(time):
            # Split the time into hours and minutes
            hours, minutes, seconds = time.split(":")
            hours = int(hours)
            minutes = int(minutes)

            # Determine AM or PM
            am_pm = "AM"
            if hours >= 12:
                hours -= 12
                am_pm = "PM"

            # Format the result as a string
            return f"{hours:02d}:{minutes:02d} {am_pm}"

        # Get the current date and time
        now = datetime.now()
        curent_date=str(now.date())
        current_time=str(now.time())

        #-------------------------------------------------------

        
        model_spoof = cv2.dnn.readNetFromCaffe('detection_model/deploy.prototxt', 
                                               'detection_model/Widerface-RetinaFace.caffemodel')
            
        #------------------------------------------------------------

        while True:
            ret,img=cap.read()

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
            results = faceCascade.process(gray_image)

            connection1=sqlite3.connect(r"databases/Attendance_Database")
            mycursor1=connection1.cursor()

            if results.detections:
                for id, detection in enumerate(results.detections):
                    bboxC = detection.location_data.relative_bounding_box # normalized values from the class 
                    ih , iw, ic = img.shape
                    bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
                    
                    # draw rectangle
                    x,y,w,h=bbox
                    x1,y1=x+w,y+h
                    cv2.rectangle(img,bbox, (255,255,255),3)
                    cv2.putText(img, f'{int(detection.score[0]*100)}%', (x,y1+26), cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)

                    # predict face
                    gray_image = cv2.cvtColor(gray_image, cv2.COLOR_RGB2GRAY)
                    if len(gray_image[y:y+h,x:x+w]) !=0:
                        if len(gray_image[y:y+h,x:x+w][0]) != 0:
                            id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                            confidence=int((100*(1-predict/300)))

                            connection=sqlite3.connect(r"databases/face_recognition_software_system")
                            mycursor=connection.cursor()

                            mycursor.execute("SELECT Last_Name FROM student_details where ID="+str(id))
                            i=mycursor.fetchone()
                            i="+".join(i)

                            mycursor.execute("SELECT First_Name FROM student_details where ID="+str(id))
                            r=mycursor.fetchone()
                            r="+".join(r)

                            mycursor.execute("SELECT Middle_Initial FROM student_details where ID="+str(id))
                            r1=mycursor.fetchone()
                            r1="+".join(r1)

                            mycursor.execute("SELECT Employee_ID FROM student_details where ID="+str(id))
                            r2=mycursor.fetchone()
                            r2="+".join(r2)

                            if confidence > 77:
                                connection.close
                                #Record attendance IN

                                now=datetime.now()
                                d1=now.strftime("%d/%m/%Y")
                                dtString=now.strftime("%H:%M:%S")

                                mycursor1.execute(f""" SELECT Time_In from Attendance
                                                        WHERE idd= """+str(id))
                                row = mycursor1.fetchall()
                                    
                                if len(row)==0:
                                    imgBackground_resized = cv2.resize(imgModeList[1], (1250,704))
                                    mycursor1.execute(f""" INSERT INTO Attendance(Employee_ID, 
                                        Last_Name, 
                                        First_Name, 
                                        Middle_Initial, 
                                        Time_In, 
                                        date, 
                                        idd) VALUES ("{r2}","{i}","{r}","{r1}","{dtString}","{d1}","{id}")  """)
                                    connection1.commit()
                                else:
                                    mycursor1.execute(f""" UPDATE Attendance
                                                            SET Time_Out = "{dtString}"
                                                            WHERE idd= """+str(id))
                                    connection1.commit()
                                    imgBackground_resized = cv2.resize(imgModeList[2], (1250,704))

                                mycursor1.execute(f""" SELECT * from Attendance
                                                        WHERE idd= """+str(id))
                                row_IN = mycursor1.fetchall()

                                mycursor1.execute(f""" SELECT idd from Attendance
                                                                            """)
                                row_idd = mycursor1.fetchall()
                                
                                if len(row_IN) > 0:
                                    combined_name=f'{i.upper()}, {r[0].upper()}.'
                                    twelve_hour_time = twentyfour_to_twelve(row_IN[0][5])

                                    cv2.putText(imgBackground_resized,str(len(row_idd)),(920,200),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2,cv2.LINE_AA)
                                    cv2.putText(imgBackground_resized, combined_name ,(955,500),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)
                                    cv2.putText(imgBackground_resized,twelve_hour_time,(955,605),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)
                                    cv2.putText(imgBackground_resized,curent_date,(955,85),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)
                                    cv2.putText(imgBackground_resized,str(twentyfour_to_twelve(current_time)),(955,120),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)

                            else:
                                cv2.rectangle(img,bbox, (255,255,255),3)
                                gray_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)
                    

            else:
                mycursor1.execute(f""" SELECT idd from Attendance""")
                row_idd = mycursor1.fetchall()
                imgBackground_resized = cv2.resize(imgModeList[1], (1250,704))
                cv2.putText(imgBackground_resized,str(len(row_idd)),(920,200),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)
                cv2.putText(imgBackground_resized,curent_date,(955,85),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)
                cv2.putText(imgBackground_resized,str(twentyfour_to_twelve(current_time)),(955,120),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,255,255),2)

            imgBackground_resized[147:147+480, 67:67+640] = img
            cv2.imshow('Attentiface V 1.0',imgBackground_resized)

            if cv2.waitKey(1)==13:
                break

        cap.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    root=Tk()
    obj=Out()
    root.mainloop()