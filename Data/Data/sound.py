import tkinter as tk
from tkinter import messagebox, Label, Tk, Button
import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
from playsound import playsound
from PIL import Image, ImageTk
import os


def close_window():
    window.destroy()
    os.system("python Data/Data/main.py")

tts = pyttsx3.init()
tts.setProperty('rate', '50')
tts.setProperty('volume', 1.0)
tts.setProperty('language', 'english')
tts.setProperty('voice', 'english')


sentences = [
    "Привет, как дела?",
    "Как тебя зовут?",
    "Откуда ты?",
    "Я люблю программирование!",
    "Хорошего дня!"
]



def speak(text):
    tts.runAndWait()
    tts.say(text)

def next_sentence():
    global current_sentence_index
    current_sentence_index = (current_sentence_index + 1) % len(sentences)
    label.config(text=sentences[current_sentence_index])
    speak(sentences[current_sentence_index])


def record_voice():
    # Запись аудио
    fs = 44100  # Частота дискретизации
    seconds = 5  # Продолжительность записи (в секундах)
    audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    write("recorded_voice.wav", fs, audio)
    messagebox.showinfo("Recording", "Recording finished.")


def play_audio():
    playsound("recorded_voice.wav")


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
label = tk.Label(window, text=sentences[0], font=("Roboto", 48))
label.pack(pady=100)
button_next = tk.Button(window, text="Next", command=next_sentence, font=("Roboto", 32))
button_next.pack(pady=10)
button_record = tk.Button(window, text="Record voice (5 second)", command=record_voice, font=("Roboto", 32))
button_record.pack(pady=10)
button_play = tk.Button(window, text="Listen voice", command=play_audio, font=("Roboto", 32))
button_play.pack(pady=10)
back_button = Button(window, text="←", font=("Roboto", 32), command=close_window)
back_button.pack(pady=10)
current_sentence_index = 0
speak(sentences[current_sentence_index])
window.mainloop()

# from speechkit import Session, SpeechSynthesis, ShortAudioRecognition
# import io
# import wave
# import pyaudio
#
# oauth_token = "AgAAAAA7tVFvAATuwQAAAADn-ick2Yc1A09fQKWo7rzn3whLEaD4LUI"
# catalog_id = "b1gbumena7clpv4fquba"
# session = Session.from_yandex_passport_oauth_token(oauth_token, catalog_id)
# synthesizeAudio = SpeechSynthesis(session)
# synthesizeAudio.synthesize(
#     'out.wav', text='Hello World!',
#     voice='oksana', format='lpcm', sampleRateHertz='16000'
# )
# audio_data = synthesizeAudio.synthesize_stream(
# text='Привет мир, снова!',
# voice='oksana', format='lpcm', sampleRateHertz='16000'
# )
#
#
# # Читаем файл
# with open('voice.wav', 'rb') as f:
#     data = f.read()
#
# # Создаем экземпляр класса с помощью `session` полученного ранее
# recognizeShortAudio = ShortAudioRecognition(session)
#
# # Передаем файл и его формат в метод `.recognize()`,
# # который возвращает строку с текстом
# text = recognizeShortAudio.recognize(
#     data, format='lpcm', sampleRateHertz='48000')
# print(text)
# def record_audio(seconds, sample_rate,
#                  chunk_size=4000, num_channels=1) -> bytes:
#     """
#     Записывает аудио данной продолжительности и возвращает бинарный объект с данными
#
#     :param integer seconds: Время записи в секундах
#     :param integer sample_rate: частота дискретизации, такая же
#         какую вы указали в параметре sampleRateHertz
#     :param integer chunk_size: размер семпла записи
#     :param integer num_channels: количество каналов, в режимер синхронного
#         распознавания спичкит принимает моно дорожку,
#         поэтому стоит оставить значение `1`
#     :return: Возвращает объект BytesIO с аудио данными в формате WAV
#     :rtype: bytes
#     """
#
#     p = pyaudio.PyAudio()
#     stream = p.open(
#         format=pyaudio.paInt16,
#         channels=num_channels,
#         rate=sample_rate,
#         input=True,
#         frames_per_buffer=chunk_size
#     )
#     frames = []
#     try:
#         for i in range(0, int(sample_rate / chunk_size * seconds)):
#             data = stream.read(chunk_size)
#             frames.append(data)
#     finally:
#         stream.stop_stream()
#         stream.close()
#         p.terminate()
#
#     container = io.BytesIO()
#     wf = wave.open(container, 'wb')
#     wf.setnchannels(num_channels)
#     wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
#     wf.setframerate(sample_rate)
#     wf.writeframes(b''.join(frames))
#     container.seek(0)
#     return container
#
#
# sample_rate = 16000  # частота дискретизации должна
# # совпадать при записи и распознавании
#
# # Записываем аудио продолжительностью 3 секунды
# data = record_audio(3, sample_rate)
#
# # Отправляем на распознавание
# text = recognizeShortAudio.recognize(
#     data, format='lpcm', sampleRateHertz=sample_rate)
# print(text)