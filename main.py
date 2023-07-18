import os
from tkinter import *
from tkinter import ttk
import tkinter.ttk as ttk
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

# Создание фонового изображения
image = Image.open("Data/background.jpg")
image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)
label = Label(window, image=background_image)
label.pack()

# Настройка стилей
style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")
style.configure('TButton', font=('Arial', 30))
style.configure('TLabel', font=('Arial', 30))

# Добро пожаловать
ttk.Label(window, text="Добро пожаловать в Accelingvo!", style='TLabel').pack(pady=30)
ttk.Label(window, text="Welcome to Accelingvo!", style='TLabel').pack(pady=10)

# Выбор родного языка
ttk.Label(window, text="(Выберите родной язык/Choose native language):", style='TLabel').pack(pady=30)

# Кнопки
ttk.Button(window, text="Русский", command=close_window, style='TButton').place(relx=0.5, rely=0.4, anchor="center")
ttk.Button(window, text="English", command=close_window1, style='TButton').place(relx=0.5, rely=0.5, anchor="center")

window.mainloop()