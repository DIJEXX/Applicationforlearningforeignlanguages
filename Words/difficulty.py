from tkinter import Tk, Label, Button, StringVar
from PIL import Image, ImageTk
def change_difficulty(difficulty):
    selected_difficulty.set(difficulty)

gl_window = Tk()
gl_window.state('zoomed')
gl_window.title("Accelingvo")
gl_window.iconbitmap('Words/py.ico')
gl_window.geometry("1920x1080")
image = Image.open("Words/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((gl_window.winfo_screenwidth(), gl_window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)

labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)

selected_difficulty = StringVar()

gl_difficulty_label = Label(gl_window, text="Выберите сложность:", font=("Arial", 32))
gl_difficulty_label.pack(pady=100)
gl_button_easy = Button(gl_window, text="Легкая", command=lambda: change_difficulty("Легкая"), fg="green", font=("Arial", 32))
gl_button_easy.pack(pady=10)
gl_button_medium = Button(gl_window, text="Средняя", command=lambda: change_difficulty("Средняя"), fg="orange", font=("Arial", 32))
gl_button_medium.pack(pady=10)
gl_button_hard = Button(gl_window, text="Тяжелая", command=lambda: change_difficulty("Тяжелая"), fg="red", font=("Arial", 32))
gl_button_hard.pack(pady=10)
selected_difficulty_label_text = "Выбранная сложность: "
selected_difficulty_label = Label(gl_window, text=selected_difficulty_label_text, font=("Arial", 32))
selected_difficulty_label.pack(pady=10)
selected_difficulty_label_value = Label(gl_window, textvariable=selected_difficulty, font=("Arial", 32))
selected_difficulty_label_value.pack()
gl_window.mainloop()