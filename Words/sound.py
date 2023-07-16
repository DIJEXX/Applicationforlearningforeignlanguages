import tkinter as tk
from tkinter import messagebox, Label
import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound

# Список предложений на английском языке
sentences = [
    "Hello, how are you?",
    "What is your name?",
    "Where are you from?",
    "How old are you?",
    "What do you like to do in your free time?"
]

# Инициализация движка для преобразования текста в речь
engine = pyttsx3.init()

# Функция для преобразования текста в речь
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Функция для обработки нажатия кнопки "Далее"
def next_sentence():
    global current_sentence_index
    current_sentence_index = (current_sentence_index + 1) % len(sentences)
    label.config(text=sentences[current_sentence_index])
    speak(sentences[current_sentence_index])

# Функция для записи голоса
def record_voice():
    # Запись аудио
    fs = 44100  # Частота дискретизации
    seconds = 5  # Продолжительность записи (в секундах)
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)

    # Ожидание окончания записи
    sd.wait()

    # Сохранение записанного аудио в файл
    write("recorded_voice.wav", fs, audio)

    messagebox.showinfo("Recording", "Recording finished.")

# Функция для прослушивания аудиозаписи
def play_audio():
    playsound("recorded_voice.wav")
# Создание главного окна
window = tk.Tk()
window.title("English Sentences")
window.geometry("1920x1080")
window.configure(bg="#000")
# Текстовая метка для отображения предложений
bb = Label(window, text="", bg="#000", fg="white", font=("Arial", 32))
bb.pack()
label = tk.Label(window, text=sentences[0], bg="#000", fg="white", font=("Arial", 48))
label.pack(pady=20)
cc = Label(window, text="", bg="#000", fg="white", font=("Arial", 32))
cc.pack()
# Кнопка "Далее"
button_next = tk.Button(window, text="Next", command=next_sentence, bg="#585858", fg="white", font=("Arial", 32))
button_next.pack(pady=10)

# Кнопка "Записать голос"
button_record = tk.Button(window, text="Record Voice", command=record_voice, bg="#585858", fg="white", font=("Arial", 32))
button_record.pack(pady=10)

# Кнопка "Прослушать запись"
button_play = tk.Button(window, text="Play Audio", command=play_audio, bg="#585858", fg="white", font=("Arial", 32))
button_play.pack(pady=10)

# Индекс текущего предложения
current_sentence_index = 0

# Проигрывание первого предложения
speak(sentences[current_sentence_index])

# Запуск главного цикла окна
window.mainloop()