from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
import os


def close_window():
    window.destroy()
    os.system("python Data/difficulty.py")


def load_words():
    global words, learned_words
    learned_words = 0
    with open("Data/Difficulty/dictionary2.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            word, translation, learned = line.strip().split("|")
            words.append((word, translation, learned == "True"))
            if learned == "True":
                learned_words += 1


def save_words():
    global words
    with open("Data/Difficulty/dictionary2.txt", "w", encoding="utf-8") as file:
        for word, translation, learned in words:
            file.write(f"{word}|{translation}|{str(learned)}\n")


def get_next_word_index():
    global current_word_index, words
    next_word_index = current_word_index + 1
    while next_word_index < len(words) and words[next_word_index][2]:
        next_word_index += 1
    if next_word_index < len(words):
        return next_word_index
    else:
        return -1


current_word_index = 0
words = []
learned_words = 0


def update_label(text_word, text_translation):
    label_word.configure(text=text_word)
    label_translation.configure(text=text_translation)


def show_word():
    global current_word_index, words
    if current_word_index < len(words):
        word, translation, learned = words[current_word_index]
        update_label(f"Word: {word}", "")
    else:
        update_label("No more words", "")


def on_first_dictionary_click():
    global current_word_index, words
    current_word_index = 0
    load_words()
    next_word_index = get_next_word_index()
    if next_word_index != -1:
        current_word_index = next_word_index
    show_word()


def on_next_one_click():
    global current_word_index, words
    next_word_index = get_next_word_index()
    if next_word_index != -1:
        current_word_index = next_word_index
    show_word()


def on_check_click():
    global current_word_index, words
    if current_word_index < len(words):
        word, translation, learned = words[current_word_index]
        update_label(f"Word: {word}", f"Translation: {translation}")
    else:
        update_label("No more words", "")


def on_done_click():
    global current_word_index, words, learned_words
    if current_word_index < len(words):
        word, translation, learned = words[current_word_index]
        if not learned:
            words[current_word_index] = (word, translation, not learned)
            learned_words += 1
            update_label("Word marked as learned.", "")
            next_word_index = get_next_word_index()
            if next_word_index != -1:
                current_word_index = next_word_index
    else:
        update_label("No more words", "")


def on_clear_statistics_click():
    global words, learned_words
    learned_words = 0
    for i in range(len(words)):
        word, translation, learned = words[i]
        if learned:
            words[i] = (word, translation, not learned)
    update_label("Statistics cleared.", "")


def on_save_click():

    save_words()
    update_label("Dictionary saved.", "")


def on_statistics_click():
    global learned_words
    text = f"Learned words: {learned_words}"
    update_label(text, "")


window = Tk()
window.state('zoomed')
window.title("Accelingvo")
window.geometry("1920x1080")
image = Image.open("Data/background.jpg")  # Замените на путь к вашему фоновому изображению
image = image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
background_image = ImageTk.PhotoImage(image)
labell = Label()
labell.pack()
labell.configure(image=background_image)
labell.place(relx=0, rely=0)
load_words()
label_word = Label(window, text="", font=("Roboto", 14), justify="left")
label_word.pack(pady=20)
label_translation = Label(window, text="", font=("Roboto", 14), justify="left")
label_translation.pack(pady=20)
first_dictionary_button = Button(window, text="Easy dictionary", font=("Roboto", 32), command=on_first_dictionary_click)
first_dictionary_button.pack(pady=10)
next_one_button = Button(window, text="Next word", font=("Roboto", 32), command=on_next_one_click)
next_one_button.pack(pady=10)
check_button = Button(window, text="Check word", font=("Roboto", 32), command=on_check_click)
check_button.pack(pady=10)
done_button = Button(window, text="Completed word", font=("Roboto", 32), command=on_done_click)
done_button.pack(pady=10)
clear_statistics_button = Button(window, text="Clear progress", font=("Roboto", 32), command=on_clear_statistics_click)
clear_statistics_button.pack(pady=10)
save_button = Button(window, text="Save progress", font=("Roboto", 32), command=on_save_click)
save_button.pack(pady=10)
statistics_button = Button(window, text="Show progress", font=("Roboto", 32), command=on_statistics_click)
statistics_button.pack(pady=10)
back_button = Button(window, text="←", font=("Roboto", 32), command=close_window)
back_button.pack(pady=10)
window.mainloop()