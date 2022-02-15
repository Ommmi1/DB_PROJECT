from tkinter import *
import tkinter.messagebox
import cx_Oracle
import time

root = Tk()
root.geometry("900x500")
root.title("Attendance System")

# create/connect the database
conn = cx_Oracle.connect('hr/hr@//localhost:1521/pdborcl')

# create cursor
c = conn.cursor()


employee_login_frame = None
employee_password_entry = None
employee_username_entry = None

shift_name_entry = None
shift_id_entry = None
depart_loc_entry = None
department_name_entry = None
department_no_entry = None
employee_eshift_entry = None
employee_edept_entry = None
employee_hdate_entry = None
employee_age_entry = None
employee_comm_entry = None
employee_sal_entry = None
employee_phone_entry = None
employee_name_entry = None
employee_no_entry = None


def authorize(event):
    return


def employee_exit():
    main_window()


def daily_record():
    global daily_record_frame
    daily_record_frame = Frame(
        employee_login_frame, width=900, height=500, bg='#EBF2F8')
    daily_record_frame.place(x=0, y=0)
    daily_record_frame.tkraise()

    header_label = Label(employee_login_frame, text="DATE\tSTATUS", font=(
        'Berlin Sans FB', 30), bg='#EBF2F8')
    header_label.place(x=0, y=0)

    record_label = Label(employee_login_frame, text=daily,
                         font=('Berlin Sans FB', 16), bg='#EBF2F8')
    record_label.place(x=0, y=70)

    back_button = Button(employee_login_frame, image=img20,
                         bd=0, bg='#EBF2F8', command=employee_login)
    back_button.place(x=820, y=420)


def employee_attendence():
    conn = cx_Oracle.connect('hr/hr@//localhost:1521/pdborcl')

    # create cursor
    c = conn.cursor()

    # insert into table
    # c.execute("SELECT *,oid FROM attendance")
    c.execute("SELECT  ATTENdate,status FROM attendance WHERE employee_id = :2", [
              employee_password_entry.get(), ])

    daily_list = c.fetchall()
    print(daily_list)

    global daily
    daily = ''

    for data in range(len(daily_list)):
        for i in range(2):
            daily += str(daily_list[data][i]) + "\t\t"
        daily += "\n"

    print(daily)

    daily_record()

    # commit changes
    conn.commit()

    # close connection
    conn.close()


def employee_login():
    global employee_login_frame
    employee_login_frame = Frame(
        employee_admin_frame, width=900, height=500, bg='#EBF2F8')
    employee_login_frame.place(x=0, y=0)
    employee_login_frame.tkraise()

    employee_icon = Label(employee_login_frame,
                          image=img15, bd=0, bg='#EBF2F8')
    employee_icon.place(x=370, y=10)

    username_label = Label(employee_login_frame, text='Employee Name', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    username_label.place(x=365, y=200)
    global employee_username_entry
    employee_username_entry = Entry(employee_login_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                    highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_username_entry.place(x=350, y=240)
    password_label = Label(employee_login_frame, text='Employee Id', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    password_label.place(x=405, y=280)
    global employee_password_entry
    employee_password_entry = Entry(employee_login_frame, bg='white', show='*', relief='sunken',
                                    highlightcolor='#D2E0F1', highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_password_entry.place(x=350, y=320)
    employee_password_entry.bind('<Return>', authorize)
    login_button = Button(employee_login_frame, image=img24,
                          bd=0, bg='#EBF2F8', command=employee_attendence)
    login_button.bind('<Button-1>', authorize)
    login_button.place(x=457, y=380)
    cancel_button = Button(employee_login_frame, image=img34,
                           bd=0, bg='#EBF2F8', command=employee_exit)
    cancel_button.place(x=800, y=400)


admin_username_entry = None
admin_password_entry = None
admin_login_frame = None
# --------------------------------XXXX---------------------------XXXX-----------------------------------------
# --------------------------------------DELETING SHIFT DB-------------------------------------------------------


def delete_shift():
    # create/connect the database
    conn = cx_Oracle.connect('hr/hr@//localhost:1521/pdborcl')

    # create cursor
    c = conn.cursor()
    global shift_id_entry
    # delete employee record
    # c.execute("DELETE FROM DEPARTMENT")
    c.execute("DELETE FROM EMPLOYEES_SHIFT WHERE Shift_id = :1",
              [shift_id_entry.get(), ])

    # commit changes
    conn.commit()

    # close connection
    conn.close()

# --------------------------------XXXX---------------------------XXXX-----------------------------------------
# --------------------------------------UPDATING SHIFT DB-------------------------------------------------------


def upadte_shift():
    conn = cx_Oracle.connect('hr/hr@//localhost:1521/pdborcl')
    c = conn.cursor()

    c.execute("UPDATE EMPLOYEES_SHIFT SET Shift_name=shift_name_entry.get() WHERE Shift_id = :1",
              [shift_id_entry.get()])

    conn.commit()
    conn.close()

# --------------------------------XXXX---------------------------XXXX-----------------------------------------
# --------------------------------------ADDING SHIFT DB-------------------------------------------------------


def add_shift():
    # create/connect the database
    conn = cx_Oracle.connect('hr/hr@//localhost:1521/pdborcl')

    # create cursor
    c = conn.cursor()

    c.execute("INSERT INTO EMPLOYEES_SHIFT VALUES (:Shift_id, :Shift_name)", [
        shift_id_entry.get(), shift_name_entry.get()])

    shift_id_entry.delete(0, END)
    shift_name_entry.delete(0, END)

    
    conn.commit()
    conn.close()


# --------------------------------XXXX---------------------------XXXX-----------------------------------------
# --------------------------------------ADDING DEPARTMENT DB-------------------------------------------------------


def add_department():
    # create/connect the database
    conn = cx_Oracle.connect('hr/hr@//localhost:1521/pdborcl')
    # create cursor
    c = conn.cursor()

    c.execute("INSERT INTO DEPARTMENT VALUES (:Dept_no, :Dept_name, :Dept_location)", [
        department_no_entry.get(), department_name_entry.get(), depart_loc_entry.get()])

    department_no_entry.delete(0, END)
    department_name_entry.delete(0, END)
    depart_loc_entry.delete(0, END)

    
    conn.commit()
    conn.close()


# --------------------------------XXXX---------------------------XXXX-----------------------------------------
# --------------------------------------DELETE DEPARTMENT DB-------------------------------------------------------
department_no_entry = None


def delete_department():
    # create/connect the database
    conn = cx_Oracle.connect('hr/hr@//localhost:1521/pdborcl')

    # create cursor
    c = conn.cursor()
    global department_no_entry
    # delete employee record
    # c.execute("DELETE FROM DEPARTMENT")
    c.execute("DELETE FROM DEPARTMENT WHERE Dept_no = :1",
              [department_no_entry.get(), ])

    # commit changes
    conn.commit()

    # close connection
    conn.close()
# --------------------------------XXXX---------------------------XXXX-----------------------------------------
# --------------------------------------UPDATE DEPARTMENT DB-------------------------------------------------------


def update_department():
    conn = cx_Oracle.connect('hr/hr@//localhost:1521/pdborcl')
    c = conn.cursor()

    c.execute("UPDATE DEPARTMENT SET Dept_name=department_name_entry.get(), Dept_location=depart_loc_entry.get() WHERE Dept_no = :1",
              [department_no_entry.get()])

    conn.commit()
    conn.close()


# --------------------------------XXXX---------------------------XXXX-----------------------------------------
# --------------------------------------ADDING EMPLOYEE DB-------------------------------------------------------


def add_employee():
    # create/connect the database
    conn = cx_Oracle.connect('hr/hr@//localhost:1521/pdborcl')

    # create cursor
    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO EMPLOYEES VALUES (:Emp_no, :Emp_name, :Emp_phone, :Emp_salary, :Emp_Comm, :Emp_age, :Hiredate, :Emp_dept_no, :Emp_shift_id)", [
              employee_no_entry.get(), employee_name_entry.get(), employee_phone_entry.get(), employee_sal_entry.get(), employee_comm_entry.get(), employee_age_entry.get(), employee_hdate_entry.get(), employee_edept_entry.get(), employee_eshift_entry.get()])

    # clear text boxes
    employee_no_entry.delete(0, END)
    employee_name_entry.delete(0, END)
    employee_phone_entry.delete(0, END)
    employee_sal_entry.delete(0, END)
    employee_comm_entry.delete(0, END)
    employee_age_entry.delete(0, END)
    employee_hdate_entry.delete(0, END)
    employee_edept_entry.delete(0, END)
    employee_eshift_entry.delete(0, END)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


employee = None

# -------------------------XXXX---------------------------XXXX-------------------------------------------------
# ------------------------------SHOW EMPLOYEE-----------------------------------------------------------------


def show_employee():
    # create/connect the database
    conn = cx_Oracle.connect('hr/hr@//localhost:1521/pdborcl')

    # create cursor
    c = conn.cursor()

    c.execute("SELECT * FROM EMPLOYEES")

    employee_list = c.fetchall()
    print(employee_list)

    global employee
    employee = ''

    for data in range(len(employee_list)):
        for i in range(4):
            employee += str(employee_list[data][i]) + "\t\t"
        employee += "\n"

    print(employee)

    employee_record()

    # commit changes
    conn.commit()

    # close connection
    conn.close()


# ------------------------------------XXXX-------------------------------------XXXX------------------------------------------------------------------
# ----------------------------------------------DELETE EMPLOYE DB-----------------------------------------------------------------------------------
employee_no_entry = None


def delete_employee():
    # create/connect the database
    conn = cx_Oracle.connect('hr/hr@//localhost:1521/pdborcl')

    # create cursor
    c = conn.cursor()
    global employee_no_entry
    # delete employee record
    # c.execute("DELETE FROM attendance")
    c.execute("DELETE FROM EMPLOYEES WHERE Emp_no = :1",
              [employee_no_entry.get(), ])

    # commit changes
    conn.commit()

    # close connection
    conn.close()


def employee_record():
    global employee_record_frame
    employee_record_frame = Frame(
        employee_detail_frame, width=900, height=500, bg='#EBF2F8')
    employee_record_frame.place(x=0, y=0)
    employee_record_frame.tkraise()

    header_label = Label(employee_record_frame, text="EMP_ID\tNAME\tPHONE\tSALARY", font=(
        'Berlin Sans FB', 30), bg='#EBF2F8')
    header_label.place(x=0, y=0)

    record_label = Label(employee_record_frame, text=employee,
                         font=('Berlin Sans FB', 16), bg='#EBF2F8')
    record_label.place(x=0, y=70)

    back_button = Button(employee_record_frame, image=img34,
                         bd=0, bg='#EBF2F8', command=employee_detail)
    back_button.place(x=820, y=420)

# ---------------------------XXXX---------------------------XXXX----------------------------------------------------
# -----------------------------------SHIFT WINDOW----------------------------------------------------------


def shift_detail():
    global shift_detail_frame
    shift_detail_frame = Frame(
        admin_login_frame, width=900, height=500, bg='#EBF2F8')
    shift_detail_frame.place(x=0, y=0)
    shift_detail_frame.tkraise()

    main_shift_lable = Label(shift_detail_frame, text='SHIFTS', font=(
        'Berlin Sans FB', 32), bg='#EBF2F8')
    main_shift_lable.place(x=200, y=50)

    shift_id_lable = Label(shift_detail_frame, text='Shift Id:', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    shift_id_lable.place(x=140, y=150)
    global shift_id_entry
    shift_id_entry = Entry(shift_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                           highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    shift_id_entry.place(x=350, y=150)

    sname_label = Label(shift_detail_frame, text='Shift Name:',
                        font=('Berlin Sans FB', 16), bg='#EBF2F8')
    sname_label.place(x=140, y=190)
    global shift_name_entry
    shift_name_entry = Entry(shift_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                             highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    shift_name_entry.place(x=350, y=190)

    # --------------------------Button-----------------------------------------

    add_depart_button = Button(shift_detail_frame, image=img31,
                               bd=0, bg='#EBF2F8', command=add_shift)
    add_depart_button.place(x=600, y=300)

    upd_depart_button = Button(shift_detail_frame, image=img32,
                               bd=0, bg='#EBF2F8', command=upadte_shift)
    upd_depart_button.place(x=450, y=300)

    del_depart_button = Button(shift_detail_frame, image=img33,
                               bd=0, bg='#EBF2F8', command=delete_shift)
    del_depart_button.place(x=300, y=300)

    back_depart_button = Button(shift_detail_frame, image=img34,
                                bd=0, bg='#EBF2F8', command=admin_portal)
    back_depart_button.place(x=150, y=300)


# ---------------------------XXXX---------------------------XXXX----------------------------------------------------
# -----------------------------------DEPARTMENT WINDOW----------------------------------------------------------
def department_detail():
    global department_detail_frame
    department_detail_frame = Frame(
        admin_login_frame, width=900, height=500, bg='#EBF2F8')
    department_detail_frame.place(x=0, y=0)
    department_detail_frame.tkraise()

    maindepart_lable = Label(department_detail_frame, text='DEPARTMENTS', font=(
        'Berlin Sans FB', 32), bg='#EBF2F8')
    maindepart_lable.place(x=200, y=50)

    dept_no_lable = Label(department_detail_frame, text='Dept_no:', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    dept_no_lable.place(x=140, y=150)
    global department_no_entry
    department_no_entry = Entry(department_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    department_no_entry.place(x=350, y=150)

    dname_label = Label(department_detail_frame, text='Department Name:',
                        font=('Berlin Sans FB', 16), bg='#EBF2F8')
    dname_label.place(x=140, y=190)
    global department_name_entry
    department_name_entry = Entry(department_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                  highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    department_name_entry.place(x=350, y=190)

    depart_loc_label = Label(department_detail_frame, text='Location:',
                             font=('Berlin Sans FB', 16), bg='#EBF2F8')
    depart_loc_label.place(x=140, y=240)
    global depart_loc_entry
    depart_loc_entry = Entry(department_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                             highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    depart_loc_entry.place(x=350, y=240)

    # --------------------------Button---------------------

    add_depart_button = Button(department_detail_frame, image=img31,
                               bd=0, bg='#EBF2F8', command=add_department)
    add_depart_button.place(x=600, y=300)

    upd_depart_button = Button(department_detail_frame, image=img32,
                               bd=0, bg='#EBF2F8', command=update_department)
    upd_depart_button.place(x=450, y=300)

    del_depart_button = Button(department_detail_frame, image=img33,
                               bd=0, bg='#EBF2F8', command=delete_department)
    del_depart_button.place(x=300, y=300)

    back_depart_button = Button(department_detail_frame, image=img34,
                                bd=0, bg='#EBF2F8', command=admin_portal)
    back_depart_button.place(x=150, y=300)


# ---------------------------XXXX---------------------------XXXX----------------------------------------------------
# -----------------------------------EMPLOYEE ADDING WINDOW----------------------------------------------------------


def employee_detail():
    global employee_detail_frame
    employee_detail_frame = Frame(
        admin_login_frame, width=900, height=500, bg='#EBF2F8')
    employee_detail_frame.place(x=0, y=0)
    employee_detail_frame.tkraise()

    Emp_no_lable = Label(employee_detail_frame, text='Emp No:', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    Emp_no_lable.place(x=80, y=100)
    global employee_no_entry
    employee_no_entry = Entry(employee_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                              highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_no_entry.place(x=210, y=100)

    name_label = Label(employee_detail_frame, text='Emp Name:',
                       font=('Berlin Sans FB', 16), bg='#EBF2F8')
    name_label.place(x=80, y=150)
    global employee_name_entry
    employee_name_entry = Entry(employee_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_name_entry.place(x=210, y=150)

    phone_label = Label(employee_detail_frame, text='Phone:',
                        font=('Berlin Sans FB', 16), bg='#EBF2F8')
    phone_label.place(x=80, y=200)
    global employee_phone_entry
    employee_phone_entry = Entry(employee_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                 highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_phone_entry.place(x=210, y=200)

    salary_label = Label(employee_detail_frame, text='Salary:',
                         font=('Berlin Sans FB', 16), bg='#EBF2F8')
    salary_label.place(x=80, y=250)
    global employee_sal_entry
    employee_sal_entry = Entry(employee_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                               highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_sal_entry.place(x=210, y=250)

    comm_label = Label(employee_detail_frame, text='Comm:',
                       font=('Berlin Sans FB', 16), bg='#EBF2F8')
    comm_label.place(x=80, y=300)
    global employee_comm_entry
    employee_comm_entry = Entry(employee_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_comm_entry.place(x=210, y=300)

    age_label = Label(employee_detail_frame, text='Age:',
                      font=('Berlin Sans FB', 16), bg='#EBF2F8')
    age_label.place(x=450, y=100)
    global employee_age_entry
    employee_age_entry = Entry(employee_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                               highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_age_entry.place(x=560, y=100)

    hiredate_label = Label(employee_detail_frame, text='Hiredate:',
                           font=('Berlin Sans FB', 16), bg='#EBF2F8')
    hiredate_label.place(x=450, y=150)
    global employee_hdate_entry
    employee_hdate_entry = Entry(employee_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                 highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_hdate_entry.place(x=560, y=150)

    edept_label = Label(employee_detail_frame, text='Dept No:',
                        font=('Berlin Sans FB', 16), bg='#EBF2F8')
    edept_label.place(x=450, y=200)
    global employee_edept_entry
    employee_edept_entry = Entry(employee_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                 highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_edept_entry.place(x=560, y=200)

    eshift_label = Label(employee_detail_frame, text='Shift Id:',
                         font=('Berlin Sans FB', 16), bg='#EBF2F8')
    eshift_label.place(x=450, y=250)
    global employee_eshift_entry
    employee_eshift_entry = Entry(employee_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                  highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_eshift_entry.place(x=560, y=250)

    # --------------------------Buttons-----------------------

    add_button = Button(employee_detail_frame, image=img31,
                        bd=0, bg='#EBF2F8', command=add_employee)
    add_button.place(x=600, y=350)

    show_button = Button(employee_detail_frame, image=img35,
                         bd=0, bg='#EBF2F8', command=show_employee)
    show_button.place(x=450, y=350)

    delete_button = Button(employee_detail_frame, image=img33,
                           bd=0, bg='#EBF2F8', command=delete_employee)
    delete_button.place(x=300, y=350)

    back_button = Button(employee_detail_frame, image=img34,
                         bd=0, bg='#EBF2F8', command=admin_portal)
    back_button.place(x=150, y=350)

# -----------------------------------------XXXX---------------------------------XXXX-------------------------------------------------------------
# -------------------------------------------ADD ATTENDACNE DB--------------------------------------------------------------------------------------


def add_attendance():

    # create/connect the database
    conn = cx_Oracle.connect('hr/hr@//localhost:1521/pdborcl')

    # create cursor
    c = conn.cursor()

    # insert into table
    c.execute("INSERT INTO EMPLOYEES_ATTENDANCE VALUES (:Working_date, :Emp_no, :Attendance_status)", [
              employee_date_entry.get(), employee_no_entry.get(), employee_status_entry.get()])

    # clear text boxes
    employee_no_entry.delete(0, END)
    employee_status_entry.delete(0, END)

    # commit changes
    conn.commit()

    # close connection
    conn.close()


def attendance_record():
    global attendance_record_frame
    attendance_record_frame = Frame(
        open_attendance_frame, width=900, height=500, bg='#EBF2F8')
    attendance_record_frame.place(x=0, y=0)
    attendance_record_frame.tkraise()

    header_label = Label(attendance_record_frame, text="employee_id\tSTATUS", font=(
        'Berlin Sans FB', 30), bg='#EBF2F8')
    header_label.place(x=0, y=0)

    record_label = Label(attendance_record_frame, text=attendance, font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    record_label.place(x=0, y=70)

    back_button = Button(attendance_record_frame, image=img34,
                         bd=0, bg='#EBF2F8', command=open_attendance)
    back_button.place(x=820, y=420)


def show_attendance():

    # create/connect the database
    conn = cx_Oracle.connect('hr/hr@//localhost:1521/pdborcl')

    # create cursor
    c = conn.cursor()

    # insert into table
    # c.execute("SELECT *,oid FROM attendance")
    c.execute("SELECT  Emp_no,Attendance_status FROM EMPLOYEES_ATTENDANCE WHERE Working_date = :DATA", [
              employee_date_entry.get(), ])

    attendance_list = c.fetchall()
    print(attendance_list)

    global attendance
    attendance = ''

    for data in range(len(attendance_list)):
        for i in range(2):
            attendance += str(attendance_list[data][i]) + "\t\t"
        attendance += "\n"

    print(attendance)

    attendance_record()

    # commit changes
    conn.commit()

    # close connection
    conn.close()


def open_attendance():
    global open_attendance_frame
    open_attendance_frame = Frame(
        admin_login_frame, width=900, height=500, bg='#EBF2F8')
    open_attendance_frame.place(x=0, y=0)
    open_attendance_frame.tkraise()

    date_label = Label(open_attendance_frame, text='DATE(DD/MM/YYYY):',
                       font=('Berlin Sans FB', 16), bg='#EBF2F8')
    date_label.place(x=200, y=50)
    global employee_date_entry
    employee_date_entry = Entry(open_attendance_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_date_entry.place(x=400, y=50)

    update_button = Button(open_attendance_frame, image=img28,
                           bd=0, bg='#EBF2F8', command=show_attendance)
    update_button.place(x=300, y=100)

    back_button = Button(open_attendance_frame, image=img34,
                         bd=0, bg='#EBF2F8', command=admin_portal)
    back_button.place(x=800, y=400)


def attendance_detail():
    global attendance_detail_frame
    attendance_detail_frame = Frame(
        admin_login_frame, width=900, height=500, bg='#EBF2F8')
    attendance_detail_frame.place(x=0, y=0)
    attendance_detail_frame.tkraise()

    date_label = Label(attendance_detail_frame, text='Employee No:',
                       font=('Berlin Sans FB', 16), bg='#EBF2F8')
    date_label.place(x=200, y=50)
    global employee_date_entry
    employee_date_entry = Entry(attendance_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_date_entry.place(x=400, y=50)

    employee_id_label = Label(attendance_detail_frame, text='DATE(DD/MM/YYYY):', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    employee_id_label.place(x=200, y=150)
    global employee_no_entry
    employee_no_entry = Entry(attendance_detail_frame, bg='white', relief='sunken',
                              highlightcolor='#D2E0F1', highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_no_entry.place(x=400, y=150)

    status_label = Label(attendance_detail_frame, text='STATUS:', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    status_label.place(x=200, y=250)
    global employee_status_entry
    employee_status_entry = Entry(attendance_detail_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                  highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    employee_status_entry.place(x=400, y=250)

    # --------------------Butoon--------------------------------------------

    update_button = Button(attendance_detail_frame, image=img32,
                           bd=0, bg='#EBF2F8', command=add_attendance)
    update_button.place(x=350, y=350)

    back_button = Button(attendance_detail_frame, image=img34,
                         bd=0, bg='#EBF2F8', command=admin_portal)
    back_button.place(x=800, y=400)

# -----------------------XXXX--------------------------XXXX-------------------------------------------------------------------
# ---------------------------------------ADMIN-------------------------------------------------------------------------------


def admin_portal():
    global admin_dashboard_frame
    admin_dashboard_frame = Frame(
        admin_login_frame, width=900, height=500, bg='#EBF2F8')
    admin_dashboard_frame.place(x=0, y=0)
    admin_dashboard_frame.tkraise()
    '''
    class_button = Button(admin_dashboard_frame,image=img17, bd=0,bg="#EBF2F8")
    class_button.place(x=150, y=100)
    class_label=Label(admin_dashboard_frame,text='New_Class',font=('Berlin Sans FB',16),bg='#EBF2F8')
    class_label.place(x=175,y=250)
    '''
    employee_button = Button(
        admin_dashboard_frame, image=img15, bd=0, bg="#EBF2F8", command=employee_detail)
    employee_button.place(x=380, y=20)
    employee_label = Label(admin_dashboard_frame, text='ADD EMPLOYEE', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    employee_label.place(x=385, y=170)

    attendence_button = Button(
        admin_dashboard_frame, image=img6, bd=0, bg="#EBF2F8", command=attendance_detail)
    attendence_button.place(x=30, y=70)
    attendence_label = Label(admin_dashboard_frame, text='MARK ATTENDANCE', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    attendence_label.place(x=60, y=170)

    record_button = Button(admin_dashboard_frame, image=img7,
                           bd=0, bg="#EBF2F8", command=open_attendance)
    record_button.place(x=550, y=70)
    record_label = Label(admin_dashboard_frame, text='VIEW RECORD', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    record_label.place(x=625, y=170)

    back_button = Button(admin_dashboard_frame, image=img34,
                         bd=0, bg='#EBF2F8', command=admin_login)
    back_button.place(x=800, y=400)

    add_depart_button = Button(admin_dashboard_frame, image=img29,
                               bd=0, bg="#EBF2F8", command=department_detail)
    add_depart_button.place(x=80, y=260)
    add_depart_label = Label(admin_dashboard_frame, text='ADD DEPARTMENT', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    add_depart_label.place(x=60, y=415)

    add_shifts_button = Button(admin_dashboard_frame, image=img30,
                               bd=0, bg="#EBF2F8", command=shift_detail)
    add_shifts_button.place(x=400, y=260)
    add_shifts_label = Label(admin_dashboard_frame, text='ADD SHIFT', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    add_shifts_label.place(x=410, y=410)


# ------------------------------XXXX-----------------------------------XXXX-------------------------------------------
# ---------------------------------------ADMID VERIFICATION------------------------------------------------------------


def admin_authorize(event):
    if admin_username_entry.get() == 'ADNAN' and admin_password_entry.get() == 'ADMIN1':
        admin_portal()
    elif admin_username_entry.get() == 'OMER' and admin_password_entry.get() == 'ADMIN2':
        admin_portal()
    elif admin_username_entry.get() == 'TAHA' and admin_password_entry.get() == 'ADMIN3':
        admin_portal()
    # elif admin_username_entry.get() == '' and admin_password_entry.get() == '':
    #     admin_portal()
    else:
        tkinter.messagebox.showinfo(
            "INVALID", "WRONG USERENAME OR PASSWORD")
        admin_username_entry.delete("0", "end")
        admin_password_entry.delete("0", "end")


def admin_exit():
    main_window()

# ---------------------------XXXX-----------------------XXXX-----------------------------------------------------------
# -----------------------------------ADMIN WINDOW----------------------------------------------------------------------


def admin_login():
    global admin_login_frame
    admin_login_frame = Frame(employee_admin_frame,
                              width=900, height=500, bg='#EBF2F8')
    admin_login_frame.place(x=0, y=0)
    admin_login_frame.tkraise()
    admin_icon = Label(admin_login_frame, image=img13, bd=0, bg='#EBF2F8')
    admin_icon.place(x=370, y=10)
    username_label = Label(admin_login_frame, text='Username', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    username_label.place(x=405, y=200)
    global admin_username_entry
    admin_username_entry = Entry(admin_login_frame, bg='white', relief='sunken', highlightcolor='#D2E0F1',
                                 highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    admin_username_entry.place(x=350, y=240)
    password_label = Label(admin_login_frame, text='Password', font=(
        'Berlin Sans FB', 16), bg='#EBF2F8')
    password_label.place(x=405, y=280)
    global admin_password_entry
    admin_password_entry = Entry(admin_login_frame, bg='white', show='*', relief='sunken',
                                 highlightcolor='#D2E0F1', highlightthickness=1, highlightbackground='#D8D6D7', font=('Tw Cen MT', 14))
    admin_password_entry.place(x=350, y=320)
    admin_password_entry.bind('<Return>', admin_authorize)
    login_button = Button(admin_login_frame, image=img24, bd=0, bg='#EBF2F8')
    login_button.bind('<Button-1>', admin_authorize)
    login_button.place(x=397, y=380)
    cancel_button = Button(admin_login_frame, image=img34,
                           bd=0, bg='#EBF2F8', command=admin_exit)
    cancel_button.place(x=800, y=400)


employee_admin_frame = None

# -------------------------XXXX----------------------XXXX---------------------------------------------------------------
# -----------------------------------MAIN WINDOW------------------------------------------------------------------------


def main_window():
    global employee_admin_frame
    employee_admin_frame = Frame(root, width=900, height=500, bg="#FFFFFF")
    employee_admin_frame.place(x=0, y=0)
    main_logo_image = Label(employee_admin_frame,
                            image=img23, bg='#FFFFFF')
    main_logo_image.place(x=200, y=50)

    UITU_label = Label(employee_admin_frame, text='UIT UNIVERSITY', font=(
        'Berlin Sans FB', 32), fg='#2E86C1', bg="#FFFFFF")
    UITU_label.place(x=435, y=100)
    present_label = Label(employee_admin_frame, text='PREPARED BY', font=(
        'Berlin Sans FB', 16), fg='#8E44AD', bg="#FFFFFF")
    present_label.place(x=530, y=150)
    present_label = Label(employee_admin_frame, text='19B STUDENTS', font=(
        'Berlin Sans FB', 16), fg='#8E44AD', bg="#FFFFFF")
    present_label.place(x=530, y=180)

    # ----------------Button-----------------------------------------------------------
    black_button_employee = Button(
        employee_admin_frame, image=img11, bd=0, command=employee_login, bg="#FFFFFF")
    black_button_employee.place(x=150, y=300)
    back_label = Label(employee_admin_frame, text='EMPLOYEES DETAILS', font=(
        'Berlin Sans FB', 18), fg='#2E86C1', bg="#FFFFFF")
    back_label.place(x=110, y=450)

    admin_button = Button(
        employee_admin_frame, image=img12, bd=0, command=admin_login, bg="#FFFFFF")
    admin_button.place(x=500, y=300)
    admin_label = Label(employee_admin_frame, text='ADMIN LOGIN', font=(
        'Berlin Sans FB', 18), fg='#2E86C1', bg="#FFFFFF")
    admin_label.place(x=495, y=450)

# -----------------------------XXXX-----------------------------XXXX--------------------------------------------------
# -------------------------------------------ALL IMAGES---------------------------------------------------------------


img6 = PhotoImage(file='attendance-logo.png')
img7 = PhotoImage(file='view-records-logo.png')
img11 = PhotoImage(file='student-login.png')
img12 = PhotoImage(file='admin-login.png')
img20 = PhotoImage(file='back-button.png')
img23 = PhotoImage(file='aaa.png')
img24 = PhotoImage(file='login-button.png')
img13 = PhotoImage(file='admin-icon1.png')
img15 = PhotoImage(file='student-icon.png')
img17 = PhotoImage(file='take-attendance.png')
img28 = PhotoImage(file='ok.png')
img29 = PhotoImage(file='depart.png')
img30 = PhotoImage(file='shifts.png')
img31 = PhotoImage(file='pp.png')
img32 = PhotoImage(file='uu.png')
img33 = PhotoImage(file='dd.png')
img34 = PhotoImage(file='bb.png')
img35 = PhotoImage(file='ll.png')
# commit changes
conn.commit()

# close connection
conn.close()

main_window()

root.mainloop()
