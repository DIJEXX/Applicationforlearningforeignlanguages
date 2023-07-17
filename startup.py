import os
from tkinter import Tk, Label, Button


def close_window():
    window.destroy()
    os.system("python Words/main.py")

window = Tk()
window.state('zoomed')
window.title("Accelingvo")
window.iconbitmap('Words/py.ico')
window.geometry("1920x1080")
window.configure(bg="#000")
label = Label(window, text="\n \n \n \n \n \n \n \n Добро пожаловать в Accelingvo! \n ", bg="#000", fg="white", font=("Arial", 32))
label.pack()
button = Button(window, text="Дальше", command=close_window, bg="#585858", fg="white", font=("Arial", 32))
button.pack()
window.mainloop()