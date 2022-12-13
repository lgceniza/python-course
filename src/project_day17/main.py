from data import question_data
from quiz_brain import QuizBrain

quiz = QuizBrain()
quiz.initQuestions(question_data)
quiz.shuffleQuestions()

quiz.startQuiz()
