from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
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
window.mainloop()