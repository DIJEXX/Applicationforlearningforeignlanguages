from tkinter import *
from tkinter import messagebox
from gtts import gTTS
import os
import pandas as pd
import random
import playsound
 
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
unknown_words = {}
 
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def is_known():
    if len(to_learn) > 1:
        to_learn.remove(current_card)
        print(len(to_learn))
        data = pd.DataFrame(to_learn)
        data.to_csv("data/words_to_learn.csv", index=False)
        next_card()
    else:
        messagebox.showinfo(title="Congratulation!",message="There's no word to learn!\nYou've review all the words!\nGood job, keep up the good work!")
        os.remove("data/words_to_learn.csv")
        window.quit()
 
def next_card():
    language = 'de'
    global  current_card, flip_timer
    current_card = random.choice(to_learn)
    selected_card = current_card["German"]
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=selected_card, fill="black")
    canvas.itemconfig(card_side, image=card_front_img)
    window.after(100)
    audio_output = gTTS(text=current_card["German"], lang=language)
    audio_output.save("german_word.mp3")
    playsound.playsound("german_word.mp3", False)
    os.remove("german_word.mp3")
    flip_timer = window.after(3000, func=flip_card)
 
 
def flip_card():
    language = 'en'
    selected_card = current_card["English"]
    canvas.itemconfig(card_side, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=selected_card, fill="white")
    audio_output = gTTS(text=current_card["English"], lang=language)
    audio_output.save("english_word.mp3")
    playsound.playsound('english_word.mp3',False)
    os.remove("english_word.mp3")
 
window = Tk()
window.title("BeeLingual(Vocabulary Building App for German)")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
 
flip_timer = window.after(3000, func=flip_card)
 
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_side = canvas.create_image(400, 263,  image=card_front_img)
card_title = canvas.create_text(400, 150, text="German", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
 
cross_button = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_button, highlightthickness=0, command=next_card, bd=0)
unknown_button.grid(row=1, column=0)
 
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known, bd=0)
known_button.grid(row=1, column=1)
 
next_card()
 
window.mainloop()