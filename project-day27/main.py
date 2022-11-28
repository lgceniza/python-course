from tkinter import Tk, Label, Button, Entry

def on_click():
  label_result.config(text=calculate(int(input_box.get())))

def calculate(num):
  return round(num * 1.609)
  

window = Tk()
window.title('Miles to Km Converter')
window.config(padx=10, pady=10)

input_box = Entry(width=8)
label_miles = Label(text='Miles')
label_km = Label(text='Km')
label_equals = Label(text='is equal to')
label_result = Label(text='0')
button = Button(text='Calculate', command=on_click)

widgets = [input_box, label_miles, label_km, label_equals, label_result, button]
pos = {input_box: (0,1), label_miles: (0,2), label_km: (1,2), label_equals: (1,0), label_result: (1,1), button: (2,1)}

for widget in widgets:
  widget.grid(row=pos[widget][0], column=pos[widget][1])

window.mainloop()
