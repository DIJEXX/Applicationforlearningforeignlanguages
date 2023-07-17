import os
from tkinter import Tk, Label, Entry, Button, Toplevel, PhotoImage
from PIL import Image, ImageTk

def open_words_window():
    os.system("python Words/dictionary.py")
def open_text_window():
    os.system("python Words/text.py")
def open_sound_window():
    os.system("python Words/sound.py")
def open_difficulty_window():
    os.system("python Words/difficulty.py")
def close_main_window():
    os.system("python Words/registration.py")
    main_window.destroy()


main_window = Tk()
main_window.title("Accelingvo")
main_window.state('zoomed')
main_window.iconbitmap('Words/py.ico')
main_window.geometry("1920x1080")
image = Image.open("Words/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((main_window.winfo_screenwidth(), main_window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)
labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)

welcome_label = Label(main_window, text="Главное меню", font=("Arial", 32))
welcome_label.pack(pady=100)
log_out_button = Button(main_window, text="Выйти", command=close_main_window, font=("Arial", 32))
log_out_button.pack()

words_button = Button(main_window, text="Словари", command=open_words_window, font=("Arial", 32))
words_button.pack()

text_button = Button(main_window, text="Предложения", command=open_text_window, font=("Arial", 32))
text_button.pack()

sound_button = Button(main_window, text="Произношение и аудирование", command=open_sound_window, font=("Arial", 32))
sound_button.pack()

difficulty_button = Button(main_window, text="Сменить сложность", command=open_difficulty_window,font=("Arial", 32))
difficulty_button.pack()
main_window.mainloop()
