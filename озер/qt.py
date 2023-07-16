import os
import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QMainWindow

conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                username TEXT NOT NULL, 
                password TEXT NOT NULL)''')

class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fluentify")
        self.setGeometry(100, 100, 1920, 1080)

        self.register_label = QLabel(self)
        self.register_label.setText("Register:")
        self.register_label.move(10, 10)

        self.register_username_label = QLabel(self)
        self.register_username_label.setText("Username:")
        self.register_username_label.move(10, 40)
        self.register_username_entry = QLineEdit(self)
        self.register_username_entry.move(100, 40)

        self.register_password_label = QLabel(self)
        self.register_password_label.setText("Password:")
        self.register_password_label.move(10, 70)
        self.register_password_entry = QLineEdit(self)
        self.register_password_entry.setEchoMode(QLineEdit.Password)
        self.register_password_entry.move(100, 70)

        self.register_button = QPushButton(self)
        self.register_button.setText("Register")
        self.register_button.clicked.connect(self.register_user)
        self.register_button.move(10, 100)

        self.login_label = QLabel(self)
        self.login_label.setText("Login:")
        self.login_label.move(10, 140)

        self.login_username_label = QLabel(self)
        self.login_username_label.setText("Username:")
        self.login_username_label.move(10, 170)
        self.login_username_entry = QLineEdit(self)
        self.login_username_entry.move(100, 170)

        self.login_password_label = QLabel(self)
        self.login_password_label.setText("Password:")
        self.login_password_label.move(10, 200)
        self.login_password_entry = QLineEdit(self)
        self.login_password_entry.setEchoMode(QLineEdit.Password)
        self.login_password_entry.move(100, 200)

        self.login_button = QPushButton(self)
        self.login_button.setText("Login")
        self.login_button.clicked.connect(self.login_user)
        self.login_button.move(10, 230)

        self.result_label = QLabel(self)
        self.result_label.setText("")
        self.result_label.move(10, 260)

    def login_user(self):
        username = self.login_username_entry.text()
        password = self.login_password_entry.text()
        try:
            cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            result = cursor.fetchone()
            if result:
                self.open_main_window()
                self.hide()
            else:
                self.result_label.setText("Invalid login credentials")
                self.result_label.setStyleSheet("color: red")
        except sqlite3.Error as error:
            self.result_label.setText("Error during login: " + str(error))
            self.result_label.setStyleSheet("color: red")

    def register_user(self):
        username = self.register_username_entry.text().strip()
        password = self.register_password_entry.text().strip()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            self.result_label.setText("User registered successfully!")
            self.result_label.setStyleSheet("color: green")
        except sqlite3.Error as error:
            self.result_label.setText("Error registering user: " + str(error))
            self.result_label.setStyleSheet("color: red")

    def open_main_window(self):
        main_window.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 1500, 600)

        self.welcome_label = QLabel(self)
        self.welcome_label.setText("Welcome!")
        self.welcome_label.move(10, 10)

        self.log_out_button = QPushButton(self)
        self.log_out_button.setText("Log Out")
        self.log_out_button.clicked.connect(self.close_main_window)
        self.log_out_button.move(10, 40)

        self.account_button = QPushButton(self)
        self.account_button.setText("Account")
        self.account_button.clicked.connect(self.close_main_window)
        self.account_button.move(10, 70)

        self.other_button = QPushButton(self)
        self.other_button.setText("Words")
        self.other_button.clicked.connect(self.open_other_window)
        self.other_button.move(10, 100)

    def open_other_window(self):
        os.system("python Words/main.py")

    def close_main_window(self):
        self.close()
        first_window.show()

app = QApplication(sys.argv)

first_window = FirstWindow()
main_window = MainWindow()

first_window.show()

sys.exit(app.exec_())

conn.close()