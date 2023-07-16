import os
import sqlite3
from tkinter import Tk, Label, Entry, Button, Toplevel

conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL)''')
def login_user():
    username = login_username_entry.get()
    password = login_password_entry.get()
    try:
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()
        if result:
            first_window.withdraw()
            open_main_window()
        else:
            result_label.config(text="Invalid login credentials", fg="red")
    except sqlite3.Error as error:
        result_label.config(text="Error during login: " + str(error), fg="red")
def register_user():
    username = register_username_entry.get().strip()
    email = register_email_entry.get().strip()
    password = register_password_entry.get().strip()
    try:
        cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
        conn.commit()
        result_label.config(text="User registered successfully!", fg="green")
    except sqlite3.Error as error:
        result_label.config(text="Error registering user: " + str(error), fg="red")
def open_main_window():
    global main_window
    main_window = Toplevel(first_window)
    main_window.title("Paralingva")
    main_window.state('zoomed')
    main_window.iconbitmap('Words/py.ico')
    main_window.geometry("1920x1080")
    main_window.configure(bg="#000")
    welcome_label = Label(main_window, text="\n \n Главное меню \n", bg="#000", fg="white", font=("Arial", 32))
    welcome_label.pack()
    log_out_button = Button(main_window, text="Выйти", command=close_main_window, bg="#585858", fg="white", font=("Arial", 32))
    log_out_button.pack()
    # fff = Label(main_window, text="", bg="#000", fg="white", font=("Arial", 32))
    # fff.pack()
    # account_button = Button(main_window, text="Account", command=close_main_window, bg="#585858", fg="white", font=("Arial", 32))
    # account_button.pack()
    gg = Label(main_window, text="", bg="#000", fg="white", font=("Arial", 32))
    gg.pack()
    words_button = Button(main_window, text="Словари", command=open_words_window, bg="#585858", fg="white", font=("Arial", 32))
    words_button.pack()
    bb = Label(main_window, text="", bg="#000", fg="white", font=("Arial", 32))
    bb.pack()
    text_button = Button(main_window, text="Предложения", command=open_text_window, bg="#585858", fg="white", font=("Arial", 32))
    text_button.pack()
    dd = Label(main_window, text="", bg="#000", fg="white", font=("Arial", 32))
    dd.pack()
    sound_button = Button(main_window, text="Произношение и аудирование", command=open_sound_window, bg="#585858", fg="white", font=("Arial", 32))
    sound_button.pack()
def open_words_window():
    os.system("python Words/main.py")
def open_text_window():
    os.system("python Words/text.py")
def open_sound_window():
    os.system("python Words/sound.py")
def close_main_window():
    main_window.destroy()
    first_window.deiconify()
def close_gl_window():
    first_window.deiconify()
first_window = Tk()
first_window.state('zoomed')
first_window.title("Paralingva")
first_window.iconbitmap('Words/py.ico')
first_window.geometry("1920x1080")
first_window.configure(bg="#000")
register_label = Label(first_window, text="Регистрация", bg="#000", fg="white", font=("Arial", 32))
register_label.pack()
register_username_label = Label(first_window, text="Логин:", bg="#000", fg="white", font=("Arial", 32))
register_username_label.pack()
register_username_entry = Entry(first_window, font=("Arial", 32))
register_username_entry.pack()
register_email_label = Label(first_window, text="Почта:", bg="#000", fg="white", font=("Arial", 32))
register_email_label.pack()
register_email_entry = Entry(first_window, font=("Arial", 32))
register_email_entry.pack()
register_password_label = Label(first_window, text="Пароль:", bg="#000", fg="white", font=("Arial", 32))
register_password_label.pack()
register_password_entry = Entry(first_window, show="*", font=("Arial", 32))
register_password_entry.pack()
ccc = Label(first_window, text="", bg="#000", fg="white", font=("Arial", 32))
ccc.pack()
register_button = Button(first_window, text="Зарегистрироваться", command=register_user, bg="#585858", fg="white", font=("Arial", 32))
register_button.pack()
vvv = Label(first_window, text="", bg="#000", fg="white", font=("Arial", 32))
vvv.pack()
login_label = Label(first_window, text="Вход", bg="#000", fg="white", font=("Arial", 32))
login_label.pack()
login_username_label = Label(first_window, text="Логин:", bg="#000", fg="white", font=("Arial", 32))
login_username_label.pack()
login_username_entry = Entry(first_window, font=("Arial", 32))
login_username_entry.pack()
login_password_label = Label(first_window, text="Пароль:", bg="#000", fg="white", font=("Arial", 32))
login_password_label.pack()
login_password_entry = Entry(first_window, show="*", font=("Arial", 32))
login_password_entry.pack()
ooo = Label(first_window, text="", bg="#000", fg="white", font=("Arial", 32))
ooo.pack()
login_button = Button(first_window, text="Войти", command=login_user, bg="#585858", fg="white", font=("Arial", 32))
login_button.pack()
result_label = Label(first_window, text="", bg="#000", fg="white", font=("Arial", 32))
result_label.pack()
first_window.mainloop()
conn.close()