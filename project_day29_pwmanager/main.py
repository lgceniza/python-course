from tkinter import *
from tkinter import messagebox

from sys import path
path.append('/Users/euniceceniza/Documents/training/python-course')
from project_day5_pwgenerator import generate

LETTERS = 8
NUMBERS = 4
SYMBOLS = 4

def generate_password():
  new_password = generate(LETTERS, SYMBOLS, NUMBERS)
  password_input.delete(0, END)
  password_input.insert(0, new_password)
  password_input.clipboard_clear()
  password_input.clipboard_append(new_password)

def save_password():
  website = website_input.get()
  username = username_input.get()
  password = password_input.get()

  if website and username and password:
    website_input.delete(0, END)
    username_input.delete(0, END)
    password_input.delete(0, END)
    messagebox.showinfo(title='Information', message='Password has been saved.')

    with open('passwords.txt', 'a') as f:
      record = "{\n Website: " + website + "\n Username: " + username + "\n Password: " + password + "\n}\n"
      f.write(record)

    return
  
  messagebox.showerror(title='Error', message='Please fill in the required fields.')


window = Tk()
window.title('MyPass')
window.config(padx=100, pady=100, width=500, height=400)

logo_png = PhotoImage(file='logo.png')
image_label = Label(image=logo_png)
website_label = Label(text='Website:', width=12, anchor='w')
username_label = Label(text='Username/Email:', width=12, anchor='w')
password_label = Label(text='Password:', width=12, anchor='w')
website_input = Entry(width=40)
username_input = Entry(width=40)
password_input = Entry(width=25, font=('Monaco'))
generate_btn = Button(text='Generate Password', command=generate_password)
add_btn = Button(text='Add', width=40, command=save_password)

layout = {image_label: (0,1), website_label: (1,0), username_label: (2,0),
          password_label: (3,0), website_input: (1,1), username_input: (2,1),
          password_input: (3,1), generate_btn: (3,2), add_btn: (4,0)}
for widget in layout:
  widget.grid(row=layout[widget][0], column=layout[widget][1])

website_input.grid(columnspan=2)
username_input.grid(columnspan=2)
password_input.grid(columnspan=1)
generate_btn.grid(columnspan=1)
add_btn.grid(columnspan=3)

window.mainloop()
