import os
from tkinter import Tk, Label, Entry, Button
import pymysql
from pymysql import Error
from PIL import Image, ImageTk

def login_user():
    username = login_username_entry.get()
    passw = login_password_entry.get()
    try:
        connection = pymysql.connect(
            host="93.81.253.61",
            port=3306,
            user="chelik",
            password="1234",
            database="sakila",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)
        try:
            with connection.cursor() as cursor:
                sql = "SELECT * FROM teamdb  WHERE username=%s AND passw=%s"
                cursor.execute(sql, (username, passw))
                result = cursor.fetchone()
                print(result)
                if result:
                    first_window.withdraw()
                    open_main_window()
                else:
                    result_label.config(text="Неверные логин или пароль", fg="red")

                print("select")

        except Error as e:
            print(e)
        finally:
            connection.close()
    except Exception as ex:
        print("Connection refused...")
        print(ex)
def register_user():
    username = register_username_entry.get().strip()
    email = register_email_entry.get().strip()
    passw = register_password_entry.get().strip()

    try:

        connection = pymysql.connect(
            host="93.81.253.61",
            port=3306,
            user="chelik",
            password="1234",
            database="sakila",
            cursorclass=pymysql.cursors.DictCursor
        )
        print("successfully connected...")
        print("#" * 20)
        try:
            with connection.cursor() as cursor:
                create_table_query = "CREATE TABLE IF NOT EXISTS `teamdb`(id int AUTO_INCREMENT," \
                                     " username varchar(32)," \
                                     " email varchar(32)," \
                                     " passw varchar(32), PRIMARY KEY (id));"
                cursor.execute(create_table_query)
                insert_query = """INSERT INTO teamdb (username, email, passw) VALUES (%s, %s, %s)"""
                vals = (username, email, passw)
                cursor.execute(insert_query, vals)
                result_label.config(text="Пользователь успешно зарегистрирован!", fg="green")
                connection.commit()
                print("Table created successfully")
        except Error as e:
            print(e)
        finally:
            connection.close()
    except Exception as ex:
        print("Connection refused...")
        print(ex)

def open_words_window():
    os.system("python Words/dictionary.py")
def open_text_window():
    os.system("python Words/text.py")
def open_sound_window():
    os.system("python Words/sound.py")
def open_difficulty_window():
    os.system("python Words/difficulty.py")
def close_main_window():
    first_window.deiconify()

def close_gl_window():
    first_window.deiconify()

def open_main_window():
    os.system("python Words/main.py")

first_window = Tk()
first_window.state('zoomed')
first_window.title("Accelingvo")
first_window.iconbitmap('Words/py.ico')
first_window.geometry("1920x1080")
image = Image.open("Words/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((first_window.winfo_screenwidth(), first_window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)
labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)

register_label = Label(first_window, text="Регистрация", font=("Roboto", 28))
register_label.pack(pady=20)
register_username_label = Label(first_window, text="Логин:", font=("Roboto", 20))
register_username_label.pack()
register_username_entry = Entry(first_window, font=("Roboto", 20))
register_username_entry.pack()
register_email_label = Label(first_window, text="Почта:", font=("Roboto", 20))
register_email_label.pack()
register_email_entry = Entry(first_window, font=("Roboto", 20))
register_email_entry.pack()
register_password_label = Label(first_window, text="Пароль:", font=("Roboto", 20))
register_password_label.pack()
register_password_entry = Entry(first_window, show="*", font=("Roboto", 20))
register_password_entry.pack()

register_button = Button(first_window, text="Зарегистрироваться", command=register_user, font=("Roboto", 28))
register_button.pack(pady=20)

login_label = Label(first_window, text="Вход", font=("Roboto", 20))
login_label.pack(pady=20)
login_username_label = Label(first_window, text="Логин:", font=("Roboto", 20))
login_username_label.pack()
login_username_entry = Entry(first_window, font=("Roboto", 20))
login_username_entry.pack()
login_password_label = Label(first_window, text="Пароль:", font=("Roboto", 20))
login_password_label.pack()
login_password_entry = Entry(first_window, show="*", font=("Roboto", 20))
login_password_entry.pack()
login_button = Button(first_window, text="Войти", command=login_user, font=("Roboto", 28))
login_button.pack(pady=20)
result_label = Label(first_window, text="", font=("Arial", 24))
result_label.pack()
first_window.mainloop()
