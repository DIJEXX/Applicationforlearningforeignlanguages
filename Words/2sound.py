import tkinter as tk
import pyaudio
import wave
from tkinter import Tk, Label, Entry, Button, Toplevel, Canvas

class AudioRecorder:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.frames = []
        self.stream = None
    def start_recording(self):
        format = pyaudio.paInt16
        channels = 1
        rate = 44100
        chunk = 1024

        self.stream = self.audio.open(format=format,
                                      channels=channels,
                                      rate=rate,
                                      input=True,
                                      frames_per_buffer=chunk)
        self.frames = []
        while True:
            data = self.stream.read(chunk)
            self.frames.append(data)
    def stop_recording(self):
        self.stream.stop_stream()
        self.stream.close()
        self.audio.terminate()
        filename = "recorded_audio.wav"
        wf = wave.open(filename, "wb")
        wf.setnchannels(1)
        wf.setsampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b"".join(self.frames))
        wf.close()
    def play_recording(self):
        wf = wave.open("recorded_audio.wav", "rb")
        format = self.audio.get_format_from_width(wf.getsampwidth())
        channels = wf.getnchannels()
        rate = wf.getframerate()
        chunk = 1024
        self.stream = self.audio.open(format=format,
                                      channels=channels,
                                      rate=rate,
                                      output=True,
                                      frames_per_buffer=chunk)
        data = wf.readframes(chunk)
        while data:
            self.stream.write(data)
            data = wf.readframes(chunk)
        self.stream.stop_stream()
        self.stream.close()
    def playright_recording(self):
        wf = wave.open("recordedright_audio.wav", "rb")
        format = self.audio.get_format_from_width(wf.getsampwidth())
        channels = wf.getnchannels()
        rate = wf.getframerate()
        chunk = 1024
        self.stream = self.audio.open(format=format,
                                      channels=channels,
                                      rate=rate,
                                      output=True,
                                      frames_per_buffer=chunk)
        data = wf.readframes(chunk)
        while data:
            self.stream.write(data)
            data = wf.readframes(chunk)
        self.stream.stop_stream()
        self.stream.close()
def start_recording():
    recorder.start_recording()
def stop_recording():
    recorder.stop_recording()
def play_recording():
    recorder.play_recording()
def playright_recording():
    recorder.playright_recording()
recorder = AudioRecorder()
root = tk.Tk()
root.title("Audio Recorder")
root.geometry("1920x1080")
root.configure(bg="#000")
welcome_label = Label(root, text="\n \n \nWelcome!\n \n ", bg="#000", fg="white", font=("Arial", 32))
welcome_label.pack()

start_button = tk.Button(root, text="Start Recording", command=start_recording, bg="#585858", fg="white", font=("Arial", 32))
start_button.pack()
stop_button = tk.Button(root, text="Stop Recording", command=stop_recording, bg="#585858", fg="white", font=("Arial", 32))
stop_button.pack()
play_button = tk.Button(root, text="Play Recording", command=play_recording, bg="#585858", fg="white", font=("Arial", 32))
playright_button = tk.Button(root, text="Play Right Recording", command=playright_recording, bg="#585858", fg="white", font=("Arial", 32))
playright_button.pack()
play_button.pack()
root.mainloop()