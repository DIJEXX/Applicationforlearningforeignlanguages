from tkinter import Tk, Label, Button, StringVar
from PIL import Image, ImageTk
import os


def close_window():
    window.destroy()
    os.system("python Data/Data/main.py")


def easy():
    window.destroy()
    os.system("python Data/Data/Difficulty/dictionary1.py")


def medium():
    window.destroy()
    os.system("python Data/Data/Difficulty/dictionary2.py")


def hard():
    window.destroy()
    os.system("python Data/Data/Difficulty/dictionary3.py")

window = Tk()
window.state('zoomed')
window.title("Accelingvo")
window.iconbitmap('Data/py.ico')
window.geometry("1920x1080")
image = Image.open("Data/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)
labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)
selected_difficulty = StringVar()
gl_difficulty_label = Label(window, text="Select difficulty:", font=("Roboto", 32))
gl_difficulty_label.pack(pady=100)
gl_button_easy = Button(window, text="Easy", command=easy, fg="green", font=("Roboto", 32))
gl_button_easy.pack(pady=10)
gl_button_medium = Button(window, text="Medium", command=medium, fg="orange", font=("Roboto", 32))
gl_button_medium.pack(pady=10)
gl_button_hard = Button(window, text="Hard", command=hard, fg="red", font=("Roboto", 32))
gl_button_hard.pack(pady=10)
back_button = Button(window, text="←", font=("Roboto", 32), command=close_window)
back_button.pack(pady=10)
window.mainloop()