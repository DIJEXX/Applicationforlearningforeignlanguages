from tkinter import Tk, Label, Button, StringVar

def change_difficulty(difficulty):
    selected_difficulty.set(difficulty)

gl_window = Tk()
gl_window.state('zoomed')
gl_window.title("Accelingvo")
gl_window.iconbitmap('Words/py.ico')
gl_window.geometry("1920x1080")
gl_window.configure(bg="#000")

selected_difficulty = StringVar()

gl_difficulty_label = Label(gl_window, text="\n Выберите сложность:", bg="#000", fg="white", font=("Arial", 32))
gl_difficulty_label.pack()
aa = Label(gl_window, text="", bg="#000", fg="white", font=("Arial", 32))
aa.pack()
gl_button_easy = Button(gl_window, text="Легкая", command=lambda: change_difficulty("Легкая"), bg="#585858", fg="green", font=("Arial", 32))
gl_button_easy.pack()
bb = Label(gl_window, text="", bg="#000", fg="white", font=("Arial", 32))
bb.pack()
gl_button_medium = Button(gl_window, text="Средняя", command=lambda: change_difficulty("Средняя"), bg="#585858", fg="orange", font=("Arial", 32))
gl_button_medium.pack()
cc = Label(gl_window, text="", bg="#000", fg="white", font=("Arial", 32))
cc.pack()
gl_button_hard = Button(gl_window, text="Тяжелая", command=lambda: change_difficulty("Тяжелая"), bg="#585858", fg="red", font=("Arial", 32))
gl_button_hard.pack()
dd = Label(gl_window, text="", bg="#000", fg="white", font=("Arial", 32))
dd.pack()
selected_difficulty_label_text = "Выбранная сложность: "
selected_difficulty_label = Label(gl_window, text=selected_difficulty_label_text, bg="#000", fg="white", font=("Arial", 32))
selected_difficulty_label.pack()
selected_difficulty_label_value = Label(gl_window, textvariable=selected_difficulty, bg="#000", fg="white", font=("Arial", 32))
selected_difficulty_label_value.pack()
gl_window.mainloop()