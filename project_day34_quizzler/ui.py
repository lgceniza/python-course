import tkinter as tk
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
WHITE = "#f7f1f0"
GREEN = "#37eb34"
RED = "#de4c3c"
TITLE = "Quizzler"

class App(tk.Tk):
  def __init__(self, quiz_brain: QuizBrain):
    super().__init__()
    self.quiz = quiz_brain
    self.title(TITLE)
    self.config(padx=20, bg=THEME_COLOR)
    self.resizable(False, False)
    
    self.canvas = tk.Canvas()
    self.canvas.config(width=300, height=250, bg=WHITE)
    self.question_text = self.canvas.create_text(
      150,
      125,
      width=280,
      text='',
      font=('Arial', 20, 'italic'),
      fill=THEME_COLOR)

    self.scoreLabel = tk.Label(fg=WHITE, text=f'Score: 0/{len(self.quiz.questions)}', font=('Arial', 15, 'normal'))
    
    true_image = tk.PhotoImage(file='images/true.png')
    false_image = tk.PhotoImage(file='images/false.png')
    self.true_btn = tk.Button(image=true_image, command=lambda: self.checkAnswer('True'))
    self.false_btn = tk.Button(image=false_image, command=lambda: self.checkAnswer('False'))

    self.arrange()
    self.displayQuestion()

    self.mainloop()
  
  def arrange(self):
    self.scoreLabel.grid(row=0, column=0, columnspan=2, pady=20)
    self.canvas.grid(row=1, column=0, rowspan=2, columnspan=2, pady=20)
    self.true_btn.grid(row=3, column=1, pady=20)
    self.false_btn.grid(row=3, column=0, pady=20)
  
  def start(self):
    self.displayQuestion()

  def displayQuestion(self):
    try:
      question = self.quiz.getQuestion()
      self.canvas.itemconfig(self.question_text, text=question.text)
      self.canvas.after_cancel('reset_color')
    except AttributeError:
      pass

  def checkAnswer(self, answer):
    if self.quiz.checkAnswer(answer):
      color = GREEN
    else:
      color = RED
    self.canvas.config(bg=color)
    self.reset_color = self.canvas.after(1000, self.canvas.config, {'bg': WHITE})

    self.displayScore()
    if self.quiz.notDone():
      self.displayQuestion()
    else:
      self.gameOver()

  def displayScore(self):
    self.scoreLabel.config(text=f'Score: {self.quiz.score}/{len(self.quiz.questions)}')

  def gameOver(self):
    messagebox.showinfo("Game Over!", f"You've completed the quiz! Your final score was {self.quiz.score}/{self.quiz.question_number}.")
    self.quit()
