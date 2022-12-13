from question_model import Question
import random

TRUE = ["True", "true", "t", "T", "TRUE"]
FALSE = ["False", "false", "f", "F", "FALSE"]
ANSWER = {"True": TRUE, "False": FALSE}

class QuizBrain:
  questions = []
  question_number = 0

  def initQuestions(self, question_data):
    for question in question_data:
      self.questions.append(Question(question['text'], question['answer']))

  def shuffleQuestions(self):
    random.shuffle(self.questions)
  
  def displayQuestion(self):
    return input(f"Q.{self.question_number+1}: {self.questions[self.question_number].text} (True/False)?: ")
  
  def checkAnswer(self, user_answer):
    if user_answer in ANSWER[self.questions[self.question_number].answer]:
      print("You got it right!")
      return True
    
    print("That's wrong.")
    return False

  def startQuiz(self):
    score = 0
    for i in range(len(self.questions)):
      user_answer = self.displayQuestion()

      if self.checkAnswer(user_answer):
        score += 1

      print(f"Your score: {score}/{self.question_number+1}")
      self.question_number += 1

    print(f"You completed the quiz. Your final score is {score}/{self.question_number+1}.")