from tkinter import *
from tkinter import messagebox
import sqlite3
import profile_window

conn = sqlite3.connect('database.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS accountInfo(first TEXT, last TEXT, email TEXT, username TEXT, password TEXT, gender TEXT, active TEXT)")

# Call the create_table function on line 13 if database.db file doesn't exist


m_window = Toplevel()
m_window.resizable(0, 0)
m_window.title("Login")
m_window.iconbitmap("icon.ico")
sign_up = Toplevel()
sign_up.resizable(0, 0)
sign_up.title("Create an account")
sign_up.iconbitmap("icon.ico")
sign_up.withdraw()

w = 450
h = 220

ws = m_window.winfo_screenwidth()
hs = m_window.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

m_window.geometry('%dx%d+%d+%d' % (w, h, x, y))

frame_1 = Frame(sign_up, padx=60)
frame_1.pack()
button_frame = Frame(sign_up, pady=15)
button_frame.pack()

label_1 = Label(frame_1, text="Create an account")
label_1.config(font=("Ubuntu 24"))
label_1.grid(row=0, columnspan=2)

create_first_name_label = Label(frame_1, text="First name: ", font=("Ubuntu 10"))
create_first_name = Entry(frame_1, font=("Ubuntu 10"), width=30)

create_last_name_label = Label(frame_1, text="Last name: ", font=("Ubuntu 10"))
create_last_name = Entry(frame_1, font=("Ubuntu 10"), width=30)

create_email_label = Label(frame_1, text="E-mail address: ", font=("Ubuntu 10"))
create_email = Entry(frame_1, font=("Ubuntu 10"), width=30)

create_user_label = Label(frame_1, text="Username: ")
create_user_label.config(font=("Ubuntu 10"))
create_user_entry = Entry(frame_1)
create_user_entry.config(font=("Ubuntu 10"), width=30)

create_pass_label = Label(frame_1, text="Password: ")
create_pass_label.config(font=("Ubuntu 10"))
create_pass_entry = Entry(frame_1)
create_pass_entry.config(font=("Ubuntu 10"), width=30, show="*")

confirm_pass_label = Label(frame_1, text="Confirm password: ")
confirm_pass_label.config(font=("Ubuntu 10"))
confirm_pass_entry = Entry(frame_1)
confirm_pass_entry.config(font=("Ubuntu 10"), width=30, show="*")

gender_select_label = Label(frame_1, text="Gender: ", font="Ubuntu 10")
gender_val = StringVar(frame_1)
gender_val.set("Male")
gender_select = OptionMenu(frame_1, gender_val, "Male", "Female", "Others")

create_first_name_label.grid(row=1, sticky=E)
create_last_name_label.grid(row=2, sticky=E)
create_email_label.grid(row=3, sticky=E)
create_user_label.grid(row=4, sticky=E)
create_pass_label.grid(row=5, sticky=E)
confirm_pass_label.grid(row=6, sticky=E)
create_first_name.grid(row=1, column=1)
create_last_name.grid(row=2, column=1)
create_email.grid(row=3, column=1)
create_user_entry.grid(row=4, column=1)
create_pass_entry.grid(row=5, column=1)
confirm_pass_entry.grid(row=6, column=1)
gender_select_label.grid(row=7, sticky=E)
gender_select.grid(row=7, column=1, sticky=W)

label_frame = Frame(m_window)
label_frame.pack(padx=150)
m_frame = Frame(m_window)
m_frame.pack()
frame_2 = Frame(m_window)
frame_2.pack()

m_label = Label(label_frame, text="Welcome")
m_label.config(font=("Ubuntu 24"))
m_label.grid(columnspan=2)

user_label = Label(m_frame, text="Username: ")
user_label.config(font=("Ubuntu 10"))
pass_label = Label(m_frame, text="Password: ")
pass_label.config(font=("Ubuntu 10"))

user_entry = Entry(m_frame)
user_entry.config(font="Ubuntu 10", width=30)
pass_entry = Entry(m_frame, show="*")
pass_entry.config(font="Ubuntu 10", width=30)

user_label.grid(row=0, sticky=E)
pass_label.grid(row=1, sticky=E)
user_entry.grid(row=0, column=1)
pass_entry.grid(row=1, column=1)

var = IntVar()

def visible_pass():
    if var.get() == 1:
        pass_entry.config(show="")
    elif var.get() == 0:
        pass_entry.config(show="*")

show_pass = Checkbutton(m_frame, text="Show password", onvalue=1, offvalue=0, variable=var, command=visible_pass)
show_pass.config(font=("Ubuntu 10"))
show_pass.grid(row=2, columnspan=2)

def finish_acc():
    first = create_first_name.get()
    last = create_last_name.get()
    email = create_email.get()
    username = create_user_entry.get()
    password = create_pass_entry.get()
    gender = gender_val.get()

    if password != confirm_pass_entry.get():
        messagebox.showerror("Error", "The passwords you've entered doesn't match! Please try again.")
    elif first == "" or last == "" or email == "" or username == "" or password == "":
        messagebox.showerror("Error", "Looks like you've left something blank. Please try again.")
    elif len(password) < 8:
        messagebox.showerror("Too short", "Your password is short. Make sure that your password is at least 8 characters long.")
    else:
        c.execute("INSERT INTO accountInfo(first, last, email, username, password, gender) VALUES(?, ?, ?, ?, ?, ?)",
                    (first, last, email, username, password, str(gender)))
        conn.commit()

        messagebox.showinfo("Success", "Account successfully created!")
        create_first_name.delete(0, END)
        create_last_name.delete(0, END)
        create_email.delete(0, END)
        create_user_entry.delete(0, END)
        create_pass_entry.delete(0, END)
        confirm_pass_entry.delete(0, END)
        sign_up.withdraw()

finish_reg = Button(button_frame, text="Create", command=finish_acc)
finish_reg.config(font=("Ubuntu 10"), width=10)
finish_reg.pack()

def on_closing():
    if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
        c.execute("UPDATE accountInfo SET active='0' WHERE username=? AND password=?", (user_entry.get(), pass_entry.get()))
        conn.commit()
        m_window.destroy()
        profile_window.p_window.quit()
        sign_up.quit()

def signup_closing():
    if messagebox.askokcancel("Confirm", "Are you sure you want to return to the login window?"):
        sign_up.withdraw()
        create_first_name.delete(0, END)
        create_last_name.delete(0, END)
        create_email.delete(0, END)
        create_user_entry.delete(0, END)
        create_pass_entry.delete(0, END)
        confirm_pass_entry.delete(0, END)
        gender_val.set("Male")

def verify_acc_login():
    fetch_user = str(user_entry.get())
    fetch_pass = str(pass_entry.get())

    c.execute("SELECT * FROM accountInfo WHERE username=? AND password=?", (fetch_user, fetch_pass))
    fetch_account = c.fetchall()

    if fetch_account:
        c.execute("UPDATE accountInfo SET active='1' WHERE username=? AND password=?", (fetch_user, fetch_pass))
        conn.commit()
        profile_window.fetch_info()
        m_window.withdraw()
        profile_window.p_window.deiconify()
    elif fetch_user == "" and fetch_pass == "":
        messagebox.showerror("Error", "Looks like you've left the username and the password blank. Please try again.")
    elif fetch_user == "":
        messagebox.showerror("Error", "Looks like you've left the username blank. Please try again.")
    elif fetch_pass == "":
        messagebox.showerror("Error", "Looks like you've left the password blank. Please try again.")
    else:
        messagebox.showerror("Error", "Looks like you've entered an invalid username or password! Please try again.")
        pass_entry.config(show="*")
        show_pass.deselect()

login = Button(m_frame, text="Login", command=verify_acc_login)
login.config(width=12, height=1, font=("Ubuntu 10"))
login.grid(row=4, columnspan=2, pady=10)

create_acc_label = Label(frame_2, text="Don't have an account?", height=2)
create_acc_label.config(font=("Ubuntu 10"))
create_acc_label.grid(row=0)

create_acc = Button(frame_2, text="Create here", command=sign_up.deiconify)
create_acc.config(font=("Ubuntu 10"))
create_acc.grid(row=0, column=1)

def delete_account():
    if messagebox.askokcancel("Confirm", "Are you sure you want to remove this account?"):
        c.execute("DELETE FROM accountInfo WHERE active='1'")
        conn.commit()
        profile_window.p_window.withdraw()
        m_window.deiconify()

delete_button = Button(profile_window.p_frame_2, text="Delete Account", command=delete_account, height=3, width=40)
delete_button.grid(row=1)

def log_out_session():
    if messagebox.askokcancel("Confirm", "Are you sure you want to log out?"):
        c.execute("UPDATE accountInfo SET active='0' WHERE active='1'")
        conn.commit()
        profile_window.refresh_profile()
        profile_window.p_window.withdraw()
        m_window.deiconify()

log_out = Button(profile_window.p_frame_2, text="Log Out", command=log_out_session, height=3, width=40)
log_out.grid(row=1, column=1)

m_window.protocol("WM_DELETE_WINDOW", on_closing)
sign_up.protocol("WM_DELETE_WINDOW", signup_closing)
profile_window.p_window.protocol("WM_DELETE_WINDOW", on_closing)
m_window.mainloop()