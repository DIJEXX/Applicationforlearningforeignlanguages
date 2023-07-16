import tkinter as tk
import random
import os
from tkinter import Tk, Label, Entry, Button, Toplevel

sentences = [
    "Hello, how are you?",  # Пример предложений на английском
    "What is your name?",
    "Where are you from?",
    "I love programming!",
    "Have a nice day!"
]

translations = [
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
window.title("Paralingva")
window.iconbitmap('Words/py.ico')
window.geometry("1920x1080")
window.configure(bg="#000")
def showSentence():
    os.system("clear")
    sentence_label.config(text=currentSentence, bg="#000", fg="white", font=("Arial", 32))

def checkTranslation():
    translation = translation_entry.get()
    if translation == currentTranslation:
        result_label.config(text="Правильный перевод!", bg="#000", fg="green", font=("Arial", 32))
    else:
        result_label.config(text="Неправильный перевод!", bg="#000", fg="red", font=("Arial", 32))
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

sentence_label = tk.Label(window, text=currentSentence, bg="#000", fg="white", font=("Arial", 32))
sentence_label.pack()

translation_entry = tk.Entry(window, fg="#000", font=("Arial", 32))
translation_entry.pack()

check_button = tk.Button(window, text="Проверить", command=checkTranslation, bg="#585858", fg="white", font=("Arial", 32))
check_button.pack()

result_label = tk.Label(window, text="", bg="#000", fg="white", font=("Arial", 32))
result_label.pack()

next_button = tk.Button(window, text="Следующее предложение", command=getNextSentence, bg="#585858", fg="white", font=("Arial", 32))
next_button.pack()

window.mainloop()