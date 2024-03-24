from tkinter import *   # used for making GUI applications
from tkinter import ttk
# used for importing the images and modifying the images
from PIL import Image, ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Help System")

        title_lbl = Label(self.root, text="HELP ", font=(
            "times new roman", 35, "bold"), bg="white", fg="blue")
        # for placing the text
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(
            r"college_images\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top = img_top.resize((1530, 720), PIL.Image.LANCZOS)
        self.img_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.img_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

        dev_label = Label(f_lbl, text="Email:kushalsinha851@gmail.com",
                          font=("times new roman", 19, "bold"), fg="blue", bg="white")

        dev_label.place(x=550, y=200)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()  # the code  is used for creating a window
