import os
from tkinter import Tk, Label, Entry, Button, Toplevel, PhotoImage
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
            # cursor = connection.cursor()

            # create table
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

    # try:
    #     cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    #     result = cursor.fetchone()
    #     if result:
    #         first_window.withdraw()
    #         open_main_window()
    #     else:
    #         result_label.config(text="Invalid login credentials", fg="red")
    # except sqlite3.Error as error:
    #     result_label.config(text="Error during login: " + str(error), fg="red")
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
            # cursor = connection.cursor()

            # create table
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

    # try:
    #     cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    #     conn.commit()
    #     result_label.config(text="User registered successfully!", fg="green")
    # except sqlite3.Error as error:
    #     result_label.config(text="Error registering user: " + str(error), fg="red")
def open_main_window():
    global main_window
    main_window = Toplevel(first_window)
    main_window.title("Accelingvo")
    main_window.state('zoomed')
    main_window.iconbitmap('Words/py.ico')
    main_window.geometry("1920x1080")

    main_window.configure(bg="#000")

    welcome_label = Label(main_window, text="\n \n Главное меню \n", bg="#000", fg="white", font=("Arial", 32))
    welcome_label.pack()
    log_out_button = Button(main_window, text="Выйти", command=close_main_window, bg="#585858", fg="white", font=("Arial", 32))
    log_out_button.pack()

    words_button = Button(main_window, text="Словари", command=open_words_window, bg="#585858", fg="white", font=("Arial", 32))
    words_button.pack()

    text_button = Button(main_window, text="Предложения", command=open_text_window, bg="#585858", fg="white", font=("Arial", 32))
    text_button.pack()

    sound_button = Button(main_window, text="Произношение и аудирование", command=open_sound_window, bg="#585858", fg="white", font=("Arial", 32))
    sound_button.pack()

    difficulty_button = Button(main_window, text="Сменить сложность", command=open_difficulty_window, bg="#585858", fg="white", font=("Arial", 32))
    difficulty_button.pack()

def open_words_window():
    os.system("python Words/dictionary.py")
def open_text_window():
    os.system("python Words/text.py")
def open_sound_window():
    os.system("python Words/sound.py")
def open_difficulty_window():
    os.system("python Words/difficulty.py")
def close_main_window():
    main_window.destroy()
    first_window.deiconify()
def close_gl_window():
    first_window.deiconify()
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

register_label = Label(first_window, text="Регистрация", font=("Arial", 32))
register_label.pack()
register_username_label = Label(first_window, text="Логин:", font=("Arial", 32))
register_username_label.pack()
register_username_entry = Entry(first_window, font=("Arial", 32))
register_username_entry.pack()
register_email_label = Label(first_window, text="Почта:", font=("Arial", 32))
register_email_label.pack()
register_email_entry = Entry(first_window, font=("Arial", 32))
register_email_entry.pack()
register_password_label = Label(first_window, text="Пароль:", font=("Arial", 32))
register_password_label.pack()
register_password_entry = Entry(first_window, show="*", font=("Arial", 32))
register_password_entry.pack()

register_button = Button(first_window, text="Зарегистрироваться", command=register_user, font=("Arial", 32))
register_button.pack()

login_label = Label(first_window, text="Вход", font=("Arial", 32))
login_label.pack()
login_username_label = Label(first_window, text="Логин:", font=("Arial", 32))
login_username_label.pack()
login_username_entry = Entry(first_window, font=("Arial", 32))
login_username_entry.pack()
login_password_label = Label(first_window, text="Пароль:", font=("Arial", 32))
login_password_label.pack()
login_password_entry = Entry(first_window, show="*", font=("Arial", 32))
login_password_entry.pack()

login_button = Button(first_window, text="Войти", command=login_user, font=("Arial", 32))
login_button.pack()

first_window.mainloop()
