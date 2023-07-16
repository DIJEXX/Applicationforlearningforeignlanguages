import os
from tkinter import Tk, Label, Button


def close_gl_window():
    gl_window.destroy()
    os.system("python main.py")

gl_window = Tk()
gl_window.title("Paralingva")
gl_window.iconbitmap('Words/py.ico')
gl_window.geometry("1920x1080")
gl_window.configure(bg="#000")
gl_label = Label(gl_window, text="\n \n \n \n \n \n \n \n Добро пожаловать в Paralingva! \n ", bg="#000", fg="white", font=("Arial", 32))
gl_label.pack()
gl_button = Button(gl_window, text="Дальше", command=close_gl_window, bg="#585858", fg="white", font=("Arial", 32))
gl_button.pack()
gl_window.mainloop()