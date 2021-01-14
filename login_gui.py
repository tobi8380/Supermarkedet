from tkinter import *
import os

# Designing window for registration

#class login_gui(ttk.Frame):
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    register_screen.configure(bg="yellow")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Indtast oplysninger", bg="yellow").pack()
    Label(register_screen, text="", bg="yellow").pack()
    username_lable = Label(register_screen, text="Brugernavn", bg="yellow")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username, bg="yellow")
    username_entry.pack()
    password_lable = Label(register_screen, text="Adgangskode", bg="yellow")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*', bg="yellow")
    password_entry.pack()
    Label(register_screen, text="", bg="yellow").pack()
    Button(register_screen, text="Registrer bruger", width=15, height=1, bg="yellow", fg="black", command = register_user).pack()


# Designing window for login

def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.configure(bg="yellow")
    Label(login_screen, text="Indtast oplysninger", bg="yellow").pack()
    Label(login_screen, text="", bg="yellow").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Brugernavn", bg="yellow").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify, bg="yellow")
    username_login_entry.pack()
    Label(login_screen, text="", bg="yellow").pack()
    Label(login_screen, text="Kode", bg="yellow").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*', bg="yellow")
    password_login_entry.pack()
    Label(login_screen, text="", bg="yellow").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify, bg="yellow").pack()

# Implementing event on register button

def register_user():

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Bruger oprettet", fg="black", font=("calibri", 11), bg="yellow").pack()

# Implementing event on login button

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login success

def login_sucess(): #MAIN SCREEN
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("VELKOMMEN TIL PROGRAMMET")
    login_success_screen.geometry("1500x750")
    Label(login_success_screen, text="VELKOMMEN SIMPS").pack()

# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x75")
    password_not_recog_screen.configure(bg="yellow")
    Label(password_not_recog_screen, text="Forkert kode", bg="yellow").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised, bg="yellow").pack()

# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x75")
    user_not_found_screen.configure(bg="yellow")
    Label(user_not_found_screen, text="Bruger ikke fundet", bg="yellow").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen, bg="yellow").pack()

# Deleting popups
def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x175")
    main_screen.title("Account Login")
    main_screen.configure(bg="yellow")
    Button(text="Login", height="2", width="30", command = login, bg="yellow").pack()
    Label(text="", bg="yellow").pack()
    Button(text="Register", height="2", width="30", command=register, bg="yellow").pack()

    main_screen.mainloop()


main_account_screen()
