import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def close_window():
    window.destroy()
    os.system("python Data/themes.py")

window = tk.Tk()
window.state('zoomed')
window.title("Accelingvo")
window.iconbitmap('Data/py.ico')
window.geometry("1920x1080")
image = Image.open("Data/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)
style = ttk.Style()
style.configure("BW.TLabel", font=("Times New Roman", 32), foreground="#183b66", padding=8, background="#8fc6da")
style.configure("BW.TButton", font=("Times New Roman", 32, "bold"), foreground="#183b66", padding=12, background="#8fc6da")
labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)
gl_difficulty_label = ttk.Label(window, text="Собери пару (Семья):", style="BW.TLabel")
gl_difficulty_label.pack(pady=100)
back_button = ttk.Button(window, text="←", command=close_window, style="BW.TButton")
back_button.pack(pady=10)
window.mainloop()