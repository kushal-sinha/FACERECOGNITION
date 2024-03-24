from time import strftime
from tkinter import *   # used for making GUI applications
from tkinter import ttk
import tkinter
# used for importing the images and modifying the images
from PIL import Image, ImageTk
import PIL
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from devloper import Devloper
from help import Help


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")
    # used for displying the images
        img = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\JSS.jpeg")
        img = img.resize((500, 200), PIL.Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=200)

        # used for displying the images
        img1 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\NEW.jpeg")
        img1 = img1.resize((500, 200), PIL.Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg)
        f_lbl1.place(x=500, y=0, width=500, height=200)

        # used for displying the images
        img2 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\face_detector1.jpg")
        img2 = img2.resize((700, 200), PIL.Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=1000, y=0, width=500, height=200)

        # bg image

        img3 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\RR.jpg")
        img3 = img3.resize((1530, 790), PIL.Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)

        # for setting the font
        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM ", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        # for placing the text
        title_lbl.place(x=0, y=0, width=1530, height=55)

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

            lbl = Label(title_lbl, font=('times new roman', 14, 'bold'),
                        background='white', foreground='blue')
            lbl.place(x=0, y=100, width=110, height=50)
            time()

        # Student
        img4 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\smartt.jpg")
        img4 = img4.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.student_details, cursor="hand2")
        b1.place(x=100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100, y=300, width=220, height=40)

        # detect button
        img5 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\NEW.jpeg")
        img5 = img5.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,
                    command=self.face_data, cursor="hand2")
        b1.place(x=450, y=100, width=220, height=220)

        b1_1 = Button(bg_img, command=self.face_data, text="Face Detector", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=450, y=300, width=220, height=40)

        # attendance button
        img6 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\AT.jpg")
        img6 = img6.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6,
                    command=self.attendance, cursor="hand2")
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, command=self.attendance, text="Attendance Button", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

     # HelpDesk button
        img7 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\helpp.png")
        img7 = img7.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7,
                    command=self.Help_data, cursor="hand2")
        b1.place(x=1150, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="HELP DESK", command=self.Help_data, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1150, y=300, width=220, height=40)

        # Train Face button
        img8 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\trainp.png")
        img8 = img8.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, command=self.train_data,
                    image=self.photoimg8, cursor="hand2")
        b1.place(x=100, y=450, width=220, height=220)

        b1_1 = Button(bg_img, text="TRAIN", command=self.train_data, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=100, y=650, width=220, height=40)

        # Photos face button
        img9 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\facep.png")
        img9 = img9.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,
                    cursor="hand2", command=self.open_img,)
        b1.place(x=450, y=450, width=220, height=220)

        b1_1 = Button(bg_img, text="PHOTOS", cursor="hand2", command=self.open_img, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=450, y=650, width=220, height=40)

        # devloper button
        img10 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\devloper.png")
        img10 = img10.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, command=self.devloper_data,
                    image=self.photoimg10, cursor="hand2")
        b1.place(x=800, y=450, width=220, height=220)

        b1_1 = Button(bg_img, command=self.devloper_data, text=" DEVLOPER", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=650, width=220, height=40)

        # exit face button
        img11 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\exitt.png")
        img11 = img11.resize((220, 220), PIL.Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11,
                    command=self.iExit, cursor="hand2")
        b1.place(x=1150, y=450, width=220, height=220)

        b1_1 = Button(bg_img, text="EXIT", command=self.iExit, cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1150, y=650, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno(
            "Face Recognition", "Are you sure exit this project", parent=self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return

        # --------Function buttons--------

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def devloper_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Devloper(self.new_window)

    def Help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()  # the code  is used for creating a window
