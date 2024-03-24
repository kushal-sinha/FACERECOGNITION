from tkinter import *   # used for making GUI applications
from tkinter import ttk
# used for importing the images and modifying the images
from PIL import Image, ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        # -----------variables-----------------
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # first img
        img1 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\JSS.jpeg")
        img1 = img1.resize((500, 200), PIL.Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=200, y=0, width=500, height=130)

        # second img
        img2 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\face_detector1.jpg")
        img2 = img2.resize((500, 200), PIL.Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=700, y=0, width=500, height=130)

        # third img
        img3 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\Stanford.jpg")
        img3 = img3.resize((500, 200), PIL.Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl = Label(self.root, image=self.photoimg3)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # bg image

        img3 = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\mm.jpg")
        img3 = img3.resize((1530, 790), PIL.Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1530, height=790)

        # for setting the font
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM ", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkgreen")
        # for placing the text
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, width=1500, height=700)

        # for making left and right frame

        Left_frame = LabelFrame(main_frame, bd=5, bg="white", relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=700, height=680)

        img_left = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\JSS.jpeg")
        img_left = img_left.resize((700, 200), PIL.Image.LANCZOS)
        self.img_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.img_left)
        f_lbl.place(x=5, y=0, width=680, height=130)

        Current_course_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Current Course Information", font=(
            "times new roman", 12, "bold"))
        Current_course_frame.place(x=10, y=135, width=670, height=150)

        # Department

        dept_label = Label(Current_course_frame, text="Department",
                           font=("times new roman", 12, "bold"), bg="white")

        dept_label.grid(row=0, column=0, padx=0, pady=10)

        # comboBox basically acts as a scrollview

        dept_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_dept, font=(
            "times new roman", 12, "bold"), state="readonly", width=20)
        dept_combo["values"] = ("Select Department",
                                "CSE", "IT", "CIVIL", "MECHANICAL")
        dept_combo.current(0)  # for showing current value
        dept_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(Current_course_frame, text="Course",
                             font=("times new roman", 12, "bold"), bg="white")

        course_label.grid(row=0, column=2, padx=50, sticky=W)

        # comboBox basically acts as a scrollview

        course_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 12, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course",
                                  "BE", "MBA", "BE LATERAL", "M.Tech")
        course_combo.current(0)  # for showing current value
        course_combo.grid(row=0, column=3, padx=0, pady=10, sticky=W)

        # Year

        year_label = Label(Current_course_frame, text="Year",
                           font=("times new roman", 12, "bold"), bg="white")

        year_label.grid(row=1, column=0, padx=0, sticky=W)

        # comboBox basically acts as a scrollview

        year_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 12, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year",
                                "2020-21", "2021-22", "2022-23", "2023-24")
        year_combo.current(0)  # for showing current value
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(Current_course_frame, text="Semester",
                               font=("times new roman", 12, "bold"), bg="white")

        semester_label.grid(row=1, column=2, padx=50, sticky=W)

        # comboBox basically acts as a scrollview

        semester_combo = ttk.Combobox(Current_course_frame, textvariable=self.var_semester, font=(
            "times new roman", 12, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester",
                                    "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8")
        semester_combo.current(0)  # for showing current value
        semester_combo.grid(row=1, column=3, padx=0, pady=10, sticky=W)

        # class student information
        Class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=(
            "times new roman", 12, "bold"))
        Class_Student_frame.place(x=10, y=300, width=670, height=340)

        # studentID

        studentId_label = Label(Class_Student_frame, text="StudentID:",
                                font=("times new roman", 12, "bold"), bg="white")

        studentId_label.grid(row=0, column=0, padx=0, sticky=W)

        studentID_entry = ttk.Entry(
            Class_Student_frame, textvariable=self.var_std_id, width=20,   font=("times new roman", 12, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # studentName
        studentName_label = Label(
            Class_Student_frame, text="StudentName:", font=("times new roman", 12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=30, sticky=W)

        studentName_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_std_name, width=20, font=(
            "times new roman", 12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10,  sticky=W)

        # class divison
        class_div_label = Label(
            Class_Student_frame, text="Class Divison:", font=("times new roman", 12, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=0, pady=15, sticky=W)

       # class_div_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_div, width=20, font=(
        #   "times new roman", 12, "bold"))
       # class_div_entry.grid(row=1, column=1, padx=10, pady=15,  sticky=W)

        div_combo = ttk.Combobox(Class_Student_frame, textvariable=self.var_div, font=(
            "times new roman", 12, "bold"), state="readonly", width=18)
        div_combo["values"] = ("A",
                               "B", "C")
        div_combo.current(0)  # for showing current value
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll No
        student_rollNo_label = Label(
            Class_Student_frame, text="Roll NO:", font=("times new roman", 12, "bold"), bg="white")
        student_rollNo_label.grid(row=1, column=2, padx=30, pady=15, sticky=W)

        student_rollNo_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_roll, width=20, font=(
            "times new roman", 12, "bold"))
        student_rollNo_entry.grid(row=1, column=3, padx=10, pady=15,  sticky=W)

        # Gender
        gender_label = Label(
            Class_Student_frame, text="Gender:", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=0, pady=5, sticky=W)

        # gender_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_gender, width=20, font=(
        #    "times new roman", 12, "bold"))
        # gender_entry.grid(row=2, column=1, padx=10, pady=5,  sticky=W)

        gender_combo = ttk.Combobox(Class_Student_frame, textvariable=self.var_gender, font=(
            "times new roman", 12, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("male",
                                  "Female", "Other")
        gender_combo.current(0)  # for showing current value
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # DOB
        student_DOB_label = Label(
            Class_Student_frame, text="DOB:", font=("times new roman", 12, "bold"), bg="white")
        student_DOB_label.grid(row=2, column=2, padx=30, pady=5, sticky=W)

        student_DOB_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_dob, width=20, font=(
            "times new roman", 12, "bold"))
        student_DOB_entry.grid(row=2, column=3, padx=10, pady=5,  sticky=W)

        # Email
        Email_label = Label(
            Class_Student_frame, text="Email:", font=("times new roman", 12, "bold"), bg="white")
        Email_label.grid(row=3, column=0, padx=0, pady=15, sticky=W)

        Email_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 12, "bold"))
        Email_entry.grid(row=3, column=1, padx=10, pady=15,  sticky=W)

        # phone number
        student_PhoneNo_label = Label(
            Class_Student_frame, text="PhoneNo:", font=("times new roman", 12, "bold"), bg="white")
        student_PhoneNo_label.grid(row=3, column=2, padx=30, pady=5, sticky=W)

        student_PhoneNo_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_phone, width=20, font=(
            "times new roman", 12, "bold"))
        student_PhoneNo_entry.grid(row=3, column=3, padx=10, pady=5,  sticky=W)

        # Address
        address_label = Label(
            Class_Student_frame, text="Address:", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=0, pady=15, sticky=W)

        address_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_address, width=20, font=(
            "times new roman", 12, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=15,  sticky=W)

        # Teacher Name
        teacher_label = Label(
            Class_Student_frame, text="TeacherName:", font=("times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=30, pady=5, sticky=W)

        teacher_entry = ttk.Entry(Class_Student_frame, textvariable=self.var_teacher, width=20, font=(
            "times new roman", 12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5,  sticky=W)

        # radiobutton
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(
            Class_Student_frame, variable=self.var_radio1, text="Take a Photo Sample", value="Yes")
        radiobtn1.grid(row=6, column=0)

        self.var_radio2 = StringVar()
        radiobtn2 = ttk.Radiobutton(
            Class_Student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=6, column=1)

        # button frame
        btn_frame = Frame(Class_Student_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame.place(x=0, y=250, width=650, height=40)

        save_btn = Button(btn_frame, command=self.add_data, width=17, text="Save", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        # update
        update_btn = Button(btn_frame, command=self.update_data, width=17, text="Update", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        # delete

        delete_btn = Button(btn_frame, command=self.delete_data, width=17, text="Delete", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        # reset

        reset_btn = Button(btn_frame, command=self.reset_data, width=17, text="Reset", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)

        btn_frame1 = Frame(Class_Student_frame, bd=2, bg="white", relief=RIDGE)
        btn_frame1.place(x=0, y=280, width=650, height=30)

        # takehphotoSample

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, width=35, text="Take Photo Sample", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=1, column=0)

        # updatePhotoSample

        update_photo_btn = Button(btn_frame1, width=35, text="Update Photo Sample", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=1, column=1)

        # rightme
        Right_frame = LabelFrame(main_frame, bd=5, bg="white", relief=RIDGE, text="Student Details", font=(
            "times new roman", 12, "bold"))
        Right_frame.place(x=760, y=10, width=700, height=680)

        img_right = Image.open(
            r"C:\Users\DELL\Desktop\FACE RECOGNITION\college_images\jssateb.png")
        img_right = img_right.resize((700, 200), PIL.Image.LANCZOS)
        self.img_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image=self.img_right)
        f_lbl.place(x=5, y=0, width=680, height=130)

        # =======SEARCH SYSTEM=======

        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=(
            "times new roman", 12, "bold"))
        Search_frame.place(x=10, y=135, width=670, height=70)

        search_label = Label(
            Search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=0, pady=5, sticky=W)

        search_combo = ttk.Combobox(Search_frame, font=(
            "times new roman", 12, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Select",
                                  "Roll_No", "Phone_No")
        search_combo.current(0)  # for showing current value
        search_combo.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        search_entry = ttk.Entry(Search_frame, width=15, font=(
            "times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=15,  sticky=W)

        search_btn = Button(Search_frame, width=12, text="Search", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(Search_frame, width=12, text="Show All", font=(
            "times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        # ---------TABLE FRAME---------

        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=670, height=450)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender",
                                                               "dob", "email",  "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="RollNo")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotSampleStatus")
        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=120)
        self.student_table.column("email", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    # ----------Function declaration------------

    def add_data(self):
        if self.var_dept.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Mapapa7890", database="face_recogniser")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dept.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_std_id.get(), self.var_std_name.get(), self.var_div.get(), self.var_roll.get(
                    ), self.var_gender.get(), self.var_dob.get(), self.var_email.get(), self.var_phone.get(), self.var_address.get(), self.var_teacher.get(), self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "SUCCESS", "STUDENT DETAILS HAS BEEN ADDED SUCCESSFULLY", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to  :{str(es)}", parent=self.root)

    # ------------fetch data-------------
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Mapapa7890", database="face_recogniser")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
                conn.commit()
        conn.close()
    # -----get cursor-----------------

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dept.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    # -----uPDATE fUNCTION--------
    # -----UPDATE FUNCTION--------
    def update_data(self):
        if self.var_dept.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "All fields are required", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do You want to Update this student details", parent=self.root)
                if Update:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Mapapa7890", database="face_recogniser")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photo=%s where Student_Id=%s",
                        (
                            self.var_dept.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        )
                    )
                    messagebox.showinfo(
                        "Success", "Student detail updated successfully", parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to: {str(es)}", parent=self.root)

    # ---------Delete function-----
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror(
                "Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to delete this student", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Mapapa7890", database="face_recogniser")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_Id =%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted student", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to: {str(es)}", parent=self.root)

    # -----reset function---------
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # ---------Genererae DataSet--------

    # ... (previous code)

# ---------Genererae DataSet--------
    def generate_dataset(self):
        try:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Mapapa7890", database="face_recogniser")
            my_cursor = conn.cursor()
            my_cursor.execute("Select * from student")
            myresult = my_cursor.fetchall()
            id = 0
            for x in myresult:
                id += 1
            my_cursor.execute(
                "update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photo=%s where Student_Id=%s",
                (
                    self.var_dept.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get() == id+1
                )
            )
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            # ----load predefined data on face frontals from opencv----

            face_classifier = cv2.CascadeClassifier(
                "haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)

                if len(faces) == 0:
                    return None

                x, y, w, h = faces[0]
                face_cropped = img[y:y+h, x:x+w]
                return face_cropped

            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                cropped_face = face_cropped(my_frame)
                if cropped_face is not None:
                    img_id += 1
                else:
                    continue

                face = cv2.resize(cropped_face, (450, 450))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_name_path = "data/user." + \
                    str(id)+"."+str(img_id)+".jpg"
                cv2.imwrite(file_name_path, face)
                cv2.putText(face, str(img_id), (50, 50),
                            cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                cv2.imshow("Cropped Face", face)

                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo(
                "RESULT", "Generating data sets completed!!!!")
        except Exception as es:
            messagebox.showerror(
                "Error", f"Due to: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()  # the code  is used for creating a window
