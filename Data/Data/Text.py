import tkinter as tk
import random
import os
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button


def close_window():
    window.destroy()
    os.system("python Data/Data/main.py")

translations = [
    "Hello, how are you?",  # Пример предложений на английском
    "What is your name?",
    "Where are you from?",
    "I love programming!",
    "Have a nice day!"
]

sentences = [
    "Привет, как дела?",  # Примеры соответствующих переводов на русский
    "Как тебя зовут?",
    "Откуда ты?",
    "Я люблю программирование!",
    "Хорошего дня!"
]

currentSentenceIndex = 0
currentSentence = ""
currentTranslation = ""

window = tk.Tk()
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


def showSentence():
    os.system("clear")
    sentence_label.config(text=currentSentence, font=("Roboto", 32))


def checkTranslation():
    translation = translation_entry.get()
    if translation == currentTranslation:
        result_label.config(text="Correct translate!", fg="green", font=("Roboto", 32))
    else:
        result_label.config(text="Incorrect translate!", fg="red", font=("Roboto", 32))
    translation_entry.delete(0, tk.END)
    getNextSentence()


def getNextSentence():
    global currentSentenceIndex, currentSentence, currentTranslation
    currentSentenceIndex += 1
    if currentSentenceIndex >= len(sentences):
        currentSentenceIndex = 0
    currentSentence = sentences[currentSentenceIndex]
    currentTranslation = translations[currentSentenceIndex]
    showSentence()


random.seed()
currentSentenceIndex = random.randint(0, len(sentences) - 1)
currentSentence = sentences[currentSentenceIndex]
currentTranslation = translations[currentSentenceIndex]
sentence_label = tk.Label(window, text=currentSentence, font=("Roboto", 32))
sentence_label.pack(pady=100)
translation_entry = tk.Entry(window, fg="#000", font=("Roboto", 32))
translation_entry.pack()
check_button = tk.Button(window, text="Check", command=checkTranslation, font=("Roboto", 32))
check_button.pack(pady=50)
result_label = tk.Label(window, text="", font=("Roboto", 32))
result_label.pack()
next_button = tk.Button(window, text="Next sentence", command=getNextSentence, font=("Roboto", 32))
next_button.pack(pady=50)
back_button = Button(window, text="←", font=("Roboto", 32), command=close_window)
back_button.pack(pady=10)
window.mainloop()