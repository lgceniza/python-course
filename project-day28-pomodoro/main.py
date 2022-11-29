from tkinter import *

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

def display_timer(minutes, seconds, rep, reset=False):
  new_text = 'TIMER' if reset else ('WORK!' if rep % 2 else 'BREAK!')
  timer_label.config(text=new_text)
  canvas.itemconfig(timer_text, text=f'{minutes:0>2}:{seconds:0>2}')

def reset_timer():
  display_timer(0, 0, 0, True)
  progress_label.config(text='')
  canvas.after_cancel(timer)

def start_timer():
  minutes = WORK_MIN
  seconds = 0
  rep = 7
  countdown(minutes, seconds, rep)

def countdown(minutes, seconds, rep):
  display_timer(minutes, seconds, rep)
  
  if minutes or seconds:
    global timer
    timer = canvas.after(1000, countdown, minutes if seconds else minutes-1, seconds-1 if seconds else 59, rep)
  else:
    canvas.after_cancel(timer)
    progress_label_text = progress_label.cget('text')+'✓' if rep % 2 else progress_label.cget('text')
    progress_label.config(text=progress_label_text)

    rep -= 1
    if rep:
      minutes = WORK_MIN if rep % 2 else SHORT_BREAK_MIN
    else:
      minutes = LONG_BREAK_MIN
      rep = 8

    timer = canvas.after(1000, countdown, minutes, 0, rep)


window = Tk()
window.title('Pomodoro')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=224)
tomato_png = PhotoImage(file='tomato.png')
canvas.create_image(103, 112, image=tomato_png)
timer_text = canvas.create_text(103, 128, text='00:00', fill=YELLOW, font=(FONT_NAME, 20, 'bold'))

timer_label = Label(fg=GREEN, text='TIMER', font=(FONT_NAME, 40, 'bold'))
progress_label = Label(fg=GREEN, text='')
start_btn = Button(text='Start', command=start_timer)
reset_btn = Button(text='Reset', command=reset_timer)

layout = {canvas: (1,1), timer_label: (0,1), start_btn: (2,0), reset_btn: (2,2), progress_label: (3,1)}
for widget in layout:
  widget.grid(row=layout[widget][0], column=layout[widget][1])

window.mainloop()
