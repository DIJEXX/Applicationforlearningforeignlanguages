import tkinter as tk
import random
import time

pairs1 = [
    ("Family", "Семья"),
    ("House", "Дом"),
    ("Dog", "Собака"),
    ("Cat", "Кошка"),
    ("Car", "Машина"),
    ("Book", "Книга"),
    ("Tree", "Дерево"),
    ("Sun", "Солнце"),
    ("Water", "Вода"),
    ("Friend", "Друг"),
]

pairs2 = [
    ("Apple", "Яблоко"),
    ("Banana", "Банан"),
    ("Chair", "Стул"),
    ("Table", "Стол"),
    ("Dog", "Собака"),
    ("Cat", "Кошка"),
    ("Sun", "Солнце"),
    ("Moon", "Луна"),
    ("Book", "Книга"),
    ("Pen", "Ручка"),
]

current_pairs = pairs1

def check_match(btn):
    global matched_buttons
    if btn in matched_buttons or len(matched_buttons) == 2:
        return
    btn.config(state=tk.DISABLED)
    matched_buttons.append(btn)
    btn.config(fg="red")
    window.update()
    if len(matched_buttons) == 2:
        window.after(1000, check_matching_pairs)

def check_matching_pairs():
    global matched_buttons
    if matched_buttons[0].cget("text") == matched_buttons[1].cget("text"):
        matched_buttons[0].config(fg="green")
        matched_buttons[1].config(fg="green")
        window.update()
        time.sleep(1)
        matched_buttons[0].destroy()
        matched_buttons[1].destroy()
        buttons.remove(matched_buttons[0])
        buttons.remove(matched_buttons[1])
        matched_buttons = []
        check_game_over()
    else:
        for btn in matched_buttons:
            btn.config(fg="#183b66")
            btn.config(state=tk.NORMAL)
        matched_buttons = []

def check_game_over():
    global buttons
    if len(buttons) == 0:
        create_buttons()

def create_buttons():
    global current_pairs, buttons
    buttons = []
    random.shuffle(current_pairs)
    for i, pair in enumerate(current_pairs):
        en_word, ru_word = pair
        frame = tk.Frame(window)
        frame.pack()
        button_en = tk.Button(frame, text=en_word, font=("Times New Roman", 32, "bold"), foreground="#183b66",
                              background="#8fc6da")
        button_ru = tk.Button(frame, text=ru_word, font=("Times New Roman", 32, "bold"), foreground="#183b66",
                              background="#8fc6da")
        button_en.config(command=lambda btn=button_en: check_match(btn))
        button_ru.config(command=lambda btn=button_ru: check_match(btn))
        button_en.pack(side=tk.LEFT, padx=10)
        button_ru.pack(side=tk.LEFT, padx=10)
        buttons.append(button_en)
        buttons.append(button_ru)

def change_pairs():
    global current_pairs
    if current_pairs == pairs1:
        current_pairs = pairs2
    else:
        current_pairs = pairs1
    restart_game()

def restart_game():
    global buttons
    for btn in buttons:
        btn.destroy()
    buttons.clear()
    matched_buttons.clear()
    create_buttons()

window = tk.Tk()
window.title("Accelingvo")
window.iconbitmap('Data/py.ico')
window.geometry("800x600")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width - 800) / 2)
window_y = int((screen_height - 600) / 2)

window.geometry(f"800x600+{window_x}+{window_y}")

matched_buttons = []
create_buttons()

change_button = tk.Button(window, text="Change Pairs", font=("Times New Roman", 20, "bold"), foreground="#183b66",
                          background="#8fc6da", command=change_pairs)
change_button.pack(pady=10)

window.mainloop()
