import os
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk


def close_window():
    window.destroy()
    os.system("python Data/registration.py")

def close_window1():
    window.destroy()
    os.system("python Data/Data/registration.py")


window = Tk()
window.state('zoomed')
window.title("Acceligvo")
window.geometry("1920x1080")
window.iconbitmap('Data/py.ico')
image = Image.open("Data/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)
labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)  # Растянуть фоновое изображение на весь экран
label = Label(window, text="Добро пожаловать в Accelingvo!", font=("Roboto", 32))
label.pack( pady=50)
label = Label(window, text="Welcome to Accelingvo!", font=("Roboto", 32))
label.pack()
label = Label(window, text="(Выберите родной язык/Choose native language):", font=("Roboto", 32))
label.pack(pady=50)
button = Button(window, text="Русский", command=close_window, font=("Roboto", 32))
button.place(relx=0.5, rely=0.4, anchor="center")
button1 = Button(window, text="English", command=close_window1, font=("Roboto", 32))
button1.place(relx=0.5, rely=0.5, anchor="center")
window.mainloop()