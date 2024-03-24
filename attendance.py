from tkinter import *   # used for making GUI applications
from tkinter import ttk
# used for importing the images and modifying the images
from PIL import Image, ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np
from time import strftime
from datetime import datetime

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance System")

        # ------Variables-----
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dept = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # first imgdi.jpg
        img1 = Image.open(
            r"college_images\di.jpg")
        img1 = img1.resize((800, 200), PIL.Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # second img
        img2 = Image.open(
            r"college_images\JSS.jpeg")
        img2 = img2.resize((800, 200), PIL.Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=800, y=0, width=800, height=200)

        img3 = Image.open(
            r"college_images\mm.jpg")
        img3 = img3.resize((1530, 790), PIL.Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=790)

        # for setting the font
        title_lbl = Label(self.root, text="ATTENDANCE MANAGEMENT SYSTEM ", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkgreen")
        # for placing the text
        title_lbl.place(x=0, y=200, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=50, width=1490, height=520)

        Left_frame = LabelFrame(main_frame, bd=5, bg="white", relief=RIDGE, text="Student Attendance Details", font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=680)

        img_left = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\JSS.jpeg")
        img_left = img_left.resize((700, 200), PIL.Image.LANCZOS)
        self.img_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.img_left)
        f_lbl.place(x=5, y=0, width=680, height=130)

        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=720, height=300)

        # labels and entries----

        # attendance id
        attendanceId_label = Label(left_inside_frame,  text="AttendanceID:",
                                   font=("times new roman", 12, "bold"), bg="white")

        attendanceId_label.grid(row=0, column=0, padx=0, sticky=W)

        attendanceID_entry = ttk.Entry(
            left_inside_frame, textvariable=self.var_atten_id, width=20,   font=("times new roman", 12, "bold"))
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Name
        studentName_label = Label(
            left_inside_frame, text="Name:",  font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=1, column=0, padx=0, sticky=W)

        studentName_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_name,  width=20, font=(
            "times new roman", 12, "bold"))
        studentName_entry.grid(row=1, column=1, padx=10, pady=20,  sticky=W)

        # ROLL
        roll_label = Label(
            left_inside_frame, text="Roll:", font=("times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=30, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_roll,   width=20, font=(
            "times new roman", 12, "bold"))
        roll_entry.grid(row=0, column=3, padx=10,  sticky=W)

        # Department
        department_label = Label(
            left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        department_label.grid(row=1, column=2, padx=30, sticky=W)

        department_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_dept, width=20, font=(
            "times new roman", 12, "bold"))
        department_entry.grid(row=1, column=3, padx=10, pady=20,  sticky=W)

        # Time

        time_label = Label(
            left_inside_frame,  text="Time:", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=0, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_time,  width=20, font=(
            "times new roman", 12, "bold"))
        time_entry.grid(row=2, column=1, padx=10,  sticky=W)

        # Date
        date_label = Label(
            left_inside_frame,  text="Date:", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=30, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_date,  width=20, font=(
            "times new roman", 12, "bold"))
        date_entry.grid(row=2, column=3, padx=10,  sticky=W)

        # Attendance Status

        attendance_label = Label(
            left_inside_frame,  text="Attendance Status:", font=("times new roman", 12, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx=0, sticky=W)

        div_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance, font=(
            "times new roman", 12, "bold"), state="readonly", width=18)
        div_combo["values"] = ("Status",
                               "P", "A")
        div_combo.current(0)  # for showing current value
        div_combo.grid(row=3, column=1, padx=10, pady=20, sticky=W)

        btn_frame = Frame(left_inside_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=0, y=250, width=710, height=40)

        save_btn = Button(btn_frame, command=self.importCSV,  width=19, text="Import csv", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        # update
        update_btn = Button(btn_frame, command=self.exportCSV,  width=19, text="Export csv", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        # delete

        delete_btn = Button(btn_frame,  width=19, text="Update", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        # reset

        reset_btn = Button(btn_frame, command=self.reset_data, width=19, text="Reset", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        Right_frame = LabelFrame(main_frame, bd=5, bg="white", relief=RIDGE, text="Attendance Details", font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=760, y=10, width=700, height=580)

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=670, height=475)

        # scrollBar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=(
            "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        # for removing the extra space
        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width=100, anchor="center")
        self.AttendanceReportTable.heading("roll", anchor="center")
        self.AttendanceReportTable.heading("name", anchor="center")
        self.AttendanceReportTable.heading("department", anchor="center")
        self.AttendanceReportTable.heading("time", anchor="center")
        self.AttendanceReportTable.heading("date", anchor="center")
        self.AttendanceReportTable.heading("attendance", anchor="center")

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # ------FETCH DATA--------

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCSV(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
            parent=self.root
        )
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)
    # ----Exporting data-----

    def exportCSV(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No Data", "No Data Found to Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Open CSV",
                filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                parent=self.root
            )
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data EXPORT", "Your Data Exported to"+os.path.basename(fln)+"successfully")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):

        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dept.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dept.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()  # the code  is used for creating a window
