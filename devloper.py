from tkinter import *   # used for making GUI applications
from tkinter import ttk
# used for importing the images and modifying the images
from PIL import Image, ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2


class Devloper:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Devloper System")

        title_lbl = Label(self.root, text="DEVLOPER ", font=(
            "times new roman", 35, "bold"), bg="white", fg="blue")
        # for placing the text
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(
            r"college_images\dev.jpg")
        img_top = img_top.resize((1530, 720), PIL.Image.LANCZOS)
        self.img_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.img_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=500, y=0, width=500, height=680)

        img_top1 = Image.open(
            r"college_images\maa.jpg")
        img_top1 = img_top1.resize((200, 300), PIL.Image.LANCZOS)
        self.img_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.img_top1)
        f_lbl.place(x=300, y=0, width=200, height=300)

        # -----dEVLOPER INFOOS

        dev_label = Label(main_frame, text="Hello My Name Is Kushal",
                          font=("times new roman", 19, "bold"), fg="blue", bg="white")

        dev_label.place(x=0, y=5)

        dev_label = Label(main_frame, text="I am Android Devloper", fg="blue",
                          font=("times new roman", 20, "bold"), bg="white")

        dev_label.place(x=0, y=40)

        img2 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img2 = img2.resize((500, 400), PIL.Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(main_frame, image=self.photoimg2)
        f_lbl.place(x=0, y=210, width=500, height=520)


if __name__ == "__main__":
    root = Tk()
    obj = Devloper(root)
    root.mainloop()  # the code  is used for creating a window
