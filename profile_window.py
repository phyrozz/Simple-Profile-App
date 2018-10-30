from tkinter import *
import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

p_window = Tk()
p_window.resizable(0, 0)
p_window.title("User Profile")
p_window.iconbitmap("icon.ico")
p_window.withdraw()

w = 800
h = 600

ws = p_window.winfo_screenwidth()
hs = p_window.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

p_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

p_frame_1 = Frame(p_window)
p_frame_1.pack()
space_frame_1 = Frame(p_window, height=50)
space_frame_1.pack()
table_frame = Frame(p_window, width=200)
table_frame.pack()
space_frame_2 = Frame(p_window, height=50)
space_frame_2.pack()
p_frame_2 = Frame(p_window)
p_frame_2.pack()

welcome = Label(p_frame_1, text="Welcome", font="Ubuntu 30", height=2)
welcome.pack()

thumb = Canvas(p_frame_1, width=112, height=112)

user_icon_file = PhotoImage(file="user_icon.png")
user_icon = thumb.create_image(58, 58, image=user_icon_file)
thumb.pack()

conn.text_factory = str

print_fullname = Label(p_frame_1, font="Ubuntu 20", pady=5)
print_email = Label(p_frame_1, font="ubuntu 12")

table_firstname_left = Label(table_frame, font="Ubuntu 12 bold")
table_lastname_left = Label(table_frame, font="Ubuntu 12 bold")
table_email_left = Label(table_frame, font="Ubuntu 12 bold")
table_username_left = Label(table_frame, font="Ubuntu 12 bold")
table_gender_left = Label(table_frame, font="Ubuntu 12 bold")

table_firstname = Label(table_frame, font="Ubuntu 12")
table_lastname = Label(table_frame, font="Ubuntu 12")
table_email = Label(table_frame, font="Ubuntu 12")
table_username = Label(table_frame, font="Ubuntu 12")
table_gender = Label(table_frame, font="Ubuntu 12")

def refresh_profile():
    print_fullname.config(text="")
    print_fullname.pack()
    print_email.config(text="")
    print_email.pack()

    table_firstname_left.config(text="")
    table_firstname_left.grid(row=0, sticky=E)
    table_lastname_left.config(text="")
    table_lastname_left.grid(row=1, sticky=E)
    table_email_left.config(text="")
    table_email_left.grid(row=2, sticky=E)
    table_username_left.config(text="")
    table_username_left.grid(row=3, sticky=E)
    table_gender_left.config(text="")
    table_gender_left.grid(row=4, sticky=E)

    table_firstname.config(text="")
    table_firstname.grid(row=0, column=1, sticky=W)
    table_lastname.config(text="")
    table_lastname.grid(row=1, column=1, sticky=W)
    table_email.config(text="")
    table_email.grid(row=2, column=1, sticky=W)
    table_username.config(text="")
    table_username.grid(row=3, column=1, sticky=W)
    table_gender.config(text="")
    table_gender.grid(row=4, column=1, sticky=W)

def fetch_info():
    fetch = c.execute("SELECT * FROM accountInfo WHERE active='1'").fetchall()
    print_fullname.config(text=fetch[0][0] + " " + fetch[0][1])
    print_fullname.pack()

    print_email.config(text=fetch[0][2])
    print_email.pack()

    table_firstname_left.config(text="First Name: ")
    table_firstname_left.grid(row=0, sticky=E)
    table_lastname_left.config(text="Last Name: ")
    table_lastname_left.grid(row=1, sticky=E)
    table_email_left.config(text="Email Address: ")
    table_email_left.grid(row=2, sticky=E)
    table_username_left.config(text="Username: ")
    table_username_left.grid(row=3, sticky=E)
    table_gender_left.config(text="Gender: ")
    table_gender_left.grid(row=4, sticky=E)

    table_firstname.config(text=fetch[0][0])
    table_firstname.grid(row=0, column=1, sticky=W)
    table_lastname.config(text=fetch[0][1])
    table_lastname.grid(row=1, column=1, sticky=W)
    table_email.config(text=fetch[0][2])
    table_email.grid(row=2, column=1, sticky=W)
    table_username.config(text=fetch[0][3])
    table_username.grid(row=3, column=1, sticky=W)
    table_gender.config(text=fetch[0][5])
    table_gender.grid(row=4, column=1, sticky=W)

conn.commit()