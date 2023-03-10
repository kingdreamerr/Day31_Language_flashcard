from tkinter import *
from random import choice
import pandas
BACKGROUND_COLOR = "#B1DDC6"



# -----------------------------DATA-------------------------------------------#
try:
    data = pandas.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    data = pandas.read_csv('./data/french_words.csv')
except pandas.errors.EmptyDataError:
    data = pandas.read_csv('./data/french_words.csv')

words = data.to_dict(orient="records")
current_card = {}
# ------------------------------FUNCTIONS--------------------------------------#


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words)
    canvas.itemconfig(card_image, image=front_card)
    canvas.itemconfig(card_title, text='French', fill="black")
    canvas.itemconfig(word_name, text=current_card['French'], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_image, image=back_card)
    canvas.itemconfig(card_title, text='English', fill="white")
    canvas.itemconfig(word_name, text=current_card['English'], fill="white")

def correct():
    words.remove(current_card)
    data1 = pandas.DataFrame(words)
    data1.to_csv('./data/words_to_learn.csv',index=False)
    next_card()
# ------------------------------UI SETUP---------------------------------------#

window = Tk()
# window.minsize(width=600, height=600)
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

# CANVAS
canvas = Canvas(width=800, height=526, highlightthickness=0)
front_card = PhotoImage(file='./images/card_front.png')
back_card = PhotoImage(file='./images/card_back.png')
card_image = canvas.create_image(400, 263, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="", fill='black', font=("Ariel", 40, 'italic'))
word_name = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, 'bold'))

# correct button
correct_image = PhotoImage(file='./images/right.png')
correct_button = Button(image=correct_image, highlightthickness=0, command=correct)
correct_button.grid(column=0, row=1)


# wrong button
wrong_image = PhotoImage(file='./images/wrong.png')
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=1)
window.mainloop()