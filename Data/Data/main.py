import os
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk


def open_words_window():
    main_window.destroy()
    os.system("python Data/Data/difficulty.py")


def open_text_window():
    main_window.destroy()
    os.system("python Data/Data/text.py")


def open_sound_window():
    main_window.destroy()
    os.system("python Data/Data/sound.py")

def close_main_window():
    main_window.destroy()
    os.system("python Data/Data/registration.py")


main_window = Tk()
main_window.title("Accelingvo")
main_window.state('zoomed')
main_window.iconbitmap('Data/py.ico')
main_window.geometry("1920x1080")
main_window.configure(bg='blue')
image = Image.open("Data/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((main_window.winfo_screenwidth(), main_window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)
labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)
welcome_label = Label(main_window, text="Main menu", font=("Roboto", 32))
welcome_label.pack(pady=100)
words_button = Button(main_window, text="Dictionaries", command=open_words_window, font=("Roboto", 32))
words_button.pack(pady=10)
text_button = Button(main_window, text="Sentences", command=open_text_window, font=("Roboto", 32))
text_button.pack(pady=10)
sound_button = Button(main_window, text="Speaking and Listening", command=open_sound_window, font=("Roboto", 32))
sound_button.pack(pady=10)
log_out_button = Button(main_window, text="Exit", command=close_main_window, font=("Roboto", 32))
log_out_button.pack(pady=10)
main_window.mainloop()