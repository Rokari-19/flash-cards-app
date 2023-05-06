from tkinter import *
import pandas as pd
from random import *


BACKGROUND_COLOR = "#B1DDC6"
og_filename = "./data/french_words.csv"
front_card_img = "./images/card_front.png"
back_card_img = "./images/card_back.png"
fields = ["French", "English"]
# ----------------read csv---------------- #
try:
    data = pd.read_csv("learned_words.csv")
    data_dict = data.to_dict(orient="records")
    word_choice = {}
except FileNotFoundError:
    data = pd.read_csv(og_filename)
    data_dict = data.to_dict(orient="records")
    word_choice = {}


def next_card():
    global word_choice, flip_timer
    window.after_cancel(flip_timer)
    word_choice = choice(data_dict)
    canvas.itemconfig(lang_text, text="French", fill="Black")
    canvas.itemconfig(word_text, text=word_choice["French"], fill="Black")
    canvas.itemconfig(can_image, image=card_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    global word_choice, fields
    canvas.itemconfig(lang_text, text="English", fill="White")
    canvas.itemconfig(word_text, text=word_choice["English"], fill="White")
    canvas.itemconfig(can_image, image=card_back)
    remove()


def remove():
    data_dict.remove(word_choice)
    df = pd.DataFrame(data_dict)
    df.to_csv("learned_words.csv")


# ----------------ui setup---------------- #
window = Tk()
window.title("FlashCard App")
flip_timer = window.after(3000, flip_card)
cross_img = PhotoImage(file="./images/wrong.png")
check_img = PhotoImage(file="./images/right.png")

window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file=front_card_img)
card_back = PhotoImage(file=back_card_img)
can_image = canvas.create_image(400, 263, image=card_front)
lang_text = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "normal"))
word_text = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
cross = Button(image=cross_img, highlightthickness=0, command=next_card)
cross.grid(column=0, row=1)

check = Button(image=check_img, highlightthickness=0, command=next_card)
check.grid(column=1, row=1)
next_card()
window.mainloop()
