import os
from tkinter import *
from PIL import Image, ImageTk
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
import sv_ttk

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
Label(window, text="Добро пожаловать в Accelingvo!").pack(pady=30)
Label(window, text="Welcome to Accelingvo!").pack(pady=10)
Label(window, text="(Выберите родной язык/Choose native language):").pack(pady=30)
Button(window, text="Русский", command=close_window).place(relx=0.5, rely=0.4, anchor="center")
Button(window, text="English", command=close_window1).place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()