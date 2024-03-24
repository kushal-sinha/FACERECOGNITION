from tkinter import *   # used for making GUI applications
from tkinter import ttk
# used for importing the images and modifying the images
from PIL import Image, ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime
import csv


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl = Label(self.root, text=" FACE RECOGNITION ", font=(
            "times new roman", 35, "bold"), bg="white", fg="green")
        # for placing the text
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # 1st image

        img_top = Image.open(
            r"college_images\face_detector1.jpg")
        img_top = img_top.resize((650, 700), PIL.Image.LANCZOS)
        self.img_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.img_top)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # 2 image

        img_bottom = Image.open(
            r"college_images\fftp.jpg")
        img_bottom = img_bottom.resize((950, 700), PIL.Image.LANCZOS)
        self.img_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.img_bottom)
        f_lbl.place(x=650, y=55, width=950, height=700)

        b1_1 = Button(f_lbl, text="Face  Recognition", command=self.face_recog,  cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkgreen", fg="white")
        b1_1.place(x=370, y=620, width=200, height=40)

    # ---------Attendance Mark------
    def mark_attendance(self, i, r, n, d):
        file_path = "kushal.csv"

        # Check if the student with the given identifier already exists in the file
        if not self.is_student_present(i, file_path):
            with open(file_path, "a", newline="\n") as f:
                writer = csv.writer(f)
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                padded_data = f"{i},{r},{n},{d},{dtString},{d1},Present".center(
                    50)

                f.writelines(padded_data + "\n")

    def is_student_present(self, student_id, file_path):
        with open(file_path, "r") as f:
            # Check if the student with the given identifier already exists in the file
            return any(student_id in line for line in f)

    # --Face Recognition------

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Mapapa7890", database="face_recogniser")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "SELECT CONCAT(Name, ',', Roll, ',', Dep, ',', Student_Id) FROM student WHERE Student_Id =" + str(id))
                result = my_cursor.fetchone()
                data_string = result[0] if result else ''

    # Split the data string into individual components
                if data_string:
                    n, r, d, i = map(str.strip, data_string.split(','))
        # Now n, r, d, i contain the individual components without brackets and commas
        # Use these variables as needed

                # for showing information

                if confidence > 77:
                    cv2.putText(
                        img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)

                    cv2.putText(img, "Unknown Face", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1,
                                  10, (255, 255, 255), "Face", clf)
            return img
        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()  # the code  is used for creating a window
