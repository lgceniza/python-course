from html import unescape
from question_model import Question
from data import question_data

class QuizBrain:
  def __init__(self):
    self.questions = [Question(unescape(question['question']), question['correct_answer']) for question in question_data]
    self.question_number = 0
    self.score = 0
    self.current_question = None

  def notDone(self):
    return self.question_number < len(self.questions)

  def getQuestion(self):
    try:
      self.current_question = self.questions[self.question_number]
      self.question_number += 1
      return self.current_question
    except IndexError:
      pass

  def checkAnswer(self, user_answer):
    if user_answer == self.current_question.answer:
      self.score += 1
      return True
    return False
