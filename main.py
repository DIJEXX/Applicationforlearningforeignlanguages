import os
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk


def close_window():
    window.destroy()
    os.system("python Words/registration.py")


window = Tk()
window.state('zoomed')
window.title("Acceligvo")
window.geometry("1920x1080")
window.iconbitmap('Words/py.ico')
image = Image.open("Words/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)
labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)  # Растянуть фоновое изображение на весь экран
label = Label(window, text="Добро пожаловать в Accelingvo! ", font=("Roboto", 32))
label.pack(padx=0, pady=400)
button = Button(window, text="Дальше", command=close_window, font=("Roboto", 32))
button.place(relx=0.5, rely=0.5, anchor="center")  # Разместить кнопку по центру экрана

window.mainloop()
