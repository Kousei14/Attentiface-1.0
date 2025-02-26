from tkinter import*

import cv2
import mediapipe as mp
import os
from datetime import datetime

from utils.utilities import datetime_utils as dtu
from queries import Queries

class Recognize:
    def __init__(self):
        self.dtu = dtu()
        self.q = Queries()

        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FPS, 60)
        cap.set(3, 640)
        cap.set(4, 480)

        main_bg = cv2.imread(
            r"attendance_modes\attentiface_main.png"
            )
        main_bg = cv2.resize(
            main_bg, 
            (1250,704)
            )

        mode_path = "attendance_modes"
        mode_path_list = os.listdir(mode_path)
        img_mode_list = [cv2.imread(os.path.join(mode_path, path)) for path in mode_path_list]

        face_detector = mp.solutions.face_detection.FaceDetection(0.5)
        face_classifier = cv2.face.LBPHFaceRecognizer_create()
        face_classifier.read(
            r"models\recognizer.xml"
            )
        spoof_detector = cv2.dnn.readNetFromCaffe(
            r'models\deploy.prototxt', 
            r'models\Widerface-RetinaFace.caffemodel'
                                               )

        while True:
            ret, img = cap.read()

            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
            results = face_detector.process(gray_image)

            if results.detections:
                for id, detection in enumerate(results.detections):
                    bboxC = detection.location_data.relative_bounding_box
                    ih , iw, ic = img.shape
                    bbox = (int(bboxC.xmin * iw), 
                            int(bboxC.ymin * ih), 
                            int(bboxC.width * iw), 
                            int(bboxC.height * ih))
                    
                    # draw rectangle on detected face
                    x, y, w, h = bbox
                    x1, y1 = x + w, y + h
                    cv2.rectangle(img, bbox, (255, 255, 255), 3)
                    cv2.putText(img, 
                                f'{int(detection.score[0] * 100)}%', (x, y1 + 26), 
                                cv2.FONT_HERSHEY_DUPLEX,
                                0.8,
                                (255, 255, 255),
                                2)

                    # classify detected face
                    gray_image = cv2.cvtColor(gray_image, cv2.COLOR_RGB2GRAY)
                    if len(gray_image[y : y + h, x : x + w]) != 0:

                        if len(gray_image[y : y + h, x : x + w][0]) != 0:

                            id, predict = face_classifier.predict(gray_image[y : y + h, x : x + w])
                            confidence = int((100 * (1 - predict / 300)))

                            database = r"databases\Attentiface.db"
                            table = "Employee"
                            match = self.q.read_v2(database,
                                                   table,
                                                   columns = ["last_name",
                                                              "first_name",
                                                              "middle_initial",
                                                              "employee_id"],
                                                    row_specific = True,
                                                    column_key = "ID",
                                                    id = id)
                            match = match[0]

                            if confidence > 77:

                                database = r"databases\Attentiface.db"
                                table = "Attendance"
                                row = self.q.read_v2(database,
                                                     table,
                                                     columns = ["time_in"],
                                                     row_specific = True,
                                                     column_key = "secondary_id",
                                                     id = id)
                                
                                # if none time_in record yet
                                if len(row) == 0:
                                    main_bg = cv2.resize(img_mode_list[1], (1250,704))

                                    database = r"databases\Attentiface.db"
                                    table = "Attendance"
                                    columns = ["employee_id",
                                               "last_name",
                                               "first_name",
                                               "middle_initial",
                                               "time_in",
                                               "date",
                                               "secondary_id"]
                                    values = [match[3],
                                              match[0],
                                              match[1],
                                              match[2],
                                              datetime.now().strftime("%H:%M:%S"),
                                              datetime.now().strftime("%d/%m/%Y"),
                                              id]

                                    self.q.insert(database,
                                                  table,
                                                  columns = columns,
                                                  values = values)
                                else:
                                    main_bg = cv2.resize(img_mode_list[2], (1250,704))

                                    database = r"databases\Attentiface.db"
                                    table = "Attendance"
                                    self.q.update(database,
                                                  table,
                                                  columns = ["time_out"],
                                                  values = [datetime.now().strftime("%H:%M:%S")],
                                                  on_key = id)
                                
                                if len(row) > 0:
                                    display_name = f'{match[0].upper()}, {match[1][0].upper()}.'
                                    twelve_hour_time = self.dtu.twentyfour_to_twelve(row[0][0])

                                    cv2.putText(img = main_bg,
                                                text = str(len(row)), 
                                                org = (920, 200),
                                                fontFace = cv2.FONT_HERSHEY_DUPLEX,
                                                fontScale = 0.8,
                                                color = (255, 255, 255),
                                                thickness = 2,
                                                lineType = cv2.LINE_AA)
                                    
                                    cv2.putText(main_bg, 
                                                display_name,
                                                (955, 500),
                                                cv2.FONT_HERSHEY_DUPLEX,
                                                0.8,
                                                (255, 255, 255),
                                                2)
                                    
                                    cv2.putText(main_bg,
                                                twelve_hour_time,
                                                (955, 605),
                                                cv2.FONT_HERSHEY_DUPLEX,
                                                0.8,
                                                (255, 255, 255),
                                                2)
                                    
                                    cv2.putText(main_bg,
                                                str(datetime.now().date()),
                                                (955, 85),
                                                cv2.FONT_HERSHEY_DUPLEX,
                                                0.8,
                                                (255, 255, 255),
                                                2)
                                    
                                    cv2.putText(main_bg,
                                                str(self.dtu.twentyfour_to_twelve(str(datetime.now().time()))),
                                                (955, 120),
                                                cv2.FONT_HERSHEY_DUPLEX,
                                                0.8,
                                                (255, 255, 255),
                                                2)

                            else:
                                cv2.rectangle(img, 
                                              bbox, 
                                              (255, 255, 255),
                                              3)
                                gray_image = cv2.cvtColor(gray_image, 
                                                          cv2.COLOR_GRAY2BGR)
                    

            else:
                database = r"databases\Attentiface.db"
                table = "Attendance"
                row = self.q.read_v2(database,
                                     table,
                                     columns = ["secondary_id"])

                main_bg = cv2.resize(img_mode_list[1], (1250, 704))

                cv2.putText(main_bg,
                            str(len(row)),
                            (920, 200),
                            cv2.FONT_HERSHEY_DUPLEX,
                            0.8,
                            (255, 255, 255),
                            2)
                
                cv2.putText(main_bg,
                            str(datetime.now().date()),
                            (955, 85),
                            cv2.FONT_HERSHEY_DUPLEX,
                            0.8,
                            (255, 255, 255),
                            2)
                
                cv2.putText(main_bg,
                            str(self.dtu.twentyfour_to_twelve(datetime.now().time())),
                            (955, 120),
                            cv2.FONT_HERSHEY_DUPLEX,
                            0.8,
                            (255, 255, 255),
                            2)

            main_bg[147 : 147 + 480, 67 : 67 + 640] = img
            cv2.imshow('Attentiface V 1.0', 
                       main_bg)

            if cv2.waitKey(1) == 13:
                break

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = Recognize()
    root.mainloop()