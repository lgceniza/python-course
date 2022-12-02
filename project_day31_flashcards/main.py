from tkinter import *
from tkinter import messagebox
from pandas import read_csv

BACKGROUND_COLOR = "#B1DDC6"

def flip_canvas(i):
  canvas.itemconfig(card_image, image=cards[i])
  canvas.itemconfig(language_text, text=f'{languages[i]}')
  canvas.itemconfig(word_text, text=f"{data[data_keys[id]] if i else data_keys[id]}")

def flip_card():
  flip_canvas(1)
  canvas.after_cancel(card_flip_event)

def next_card():
  flip_canvas(0)
  global card_flip_event
  card_flip_event = canvas.after(3000, flip_card)

def right():
  global id, number_of_cards
  data.pop(data_keys[id])
  data_keys.pop(id)
  number_of_cards -= 1
  try:
    id %= number_of_cards
    next_card()
  except:
    messagebox.showinfo('Congratulations!', 'You have completed the flash cards!')

def wrong():
  global id, number_of_cards
  id += 1
  id %= number_of_cards
  next_card()

data_dict = read_csv('data/korean_words.csv').to_dict('list')
languages = list(data_dict.keys())
data = {word: data_dict[languages[1]][index] for index, word in enumerate(data_dict[languages[0]])}
data_keys = list(data.keys())
number_of_cards = 100
id = 0


window = Tk()
window.title('Flashcards')
window.config(padx=50, pady=50, width=900, height=876, bg=BACKGROUND_COLOR)

card_front_png = PhotoImage(file='images/card_front.png')
card_back_png = PhotoImage(file='images/card_back.png')
right_png = PhotoImage(file='images/right.png')
wrong_png = PhotoImage(file='images/wrong.png')
cards = [card_front_png, card_back_png]

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = canvas.create_image(0, 0, anchor='nw', image=card_front_png)
language_text = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='', font=('Arial', 60, 'bold'))

right_btn = Button(image=right_png, borderwidth=0, command=right)
wrong_btn = Button(image=wrong_png, borderwidth=0, command=wrong)

canvas.grid(row=0, column=0, rowspan=4, columnspan=2)
right_btn.grid(row=4, column=1)
wrong_btn.grid(row=4, column=0)

next_card()

window.mainloop()
