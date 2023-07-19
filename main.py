import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


def close_window():
    window.destroy()
    os.system("python Data/main.py")

def close_window1():
    window.destroy()
    os.system("python Data/Eng/registration.py")


window = Tk()
window.state('zoomed')
window.title("Acceligvo")
window.geometry("1920x1080")
window.iconbitmap('Data/py.ico')
image = Image.open("Data/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)

style = ttk.Style()
style.configure("BW.TLabel", font=("Times New Roman", 32), foreground="#183b66", padding=8, background="#8fc6da")
style.configure("BW.TButton", font=("Times New Roman", 32, "bold"), foreground="#183b66", padding=12, background="#8fc6da")

labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)  # Растянуть фоновое изображение на весь экран
label = ttk.Label(window, text="Добро пожаловать в Accelingvo!", style="BW.TLabel")
label.pack( pady=50)
label = ttk.Label(window, text="Welcome to Accelingvo!", style="BW.TLabel")
label.pack()
label = ttk.Label(window, text="(Выберите родной язык/Choose native language):", style="BW.TLabel")
label.pack(pady=50)
button = ttk.Button(window, text="Русский", command=close_window, style="BW.TButton")
button.place(relx=0.5, rely=0.4, anchor="center")
button1 = ttk.Button(window, text="English", command=close_window1, style="BW.TButton")
button1.place(relx=0.5, rely=0.5, anchor="center")
window.mainloop()