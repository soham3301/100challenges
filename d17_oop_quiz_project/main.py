from data import question_data
from question_model import Question, QuestionAPI
from quiz_brain import QuizBrain

from data_from_api import my_data

# question_bank = []

# for item in question_data:
#     question_bank.append(Question(item["text"], item["answer"]))

# the_brain = QuizBrain(question_bank)
# the_brain.next_question()

question_bank_from_api = []

for item in my_data:
    question_bank_from_api.append(QuestionAPI(item["question"], item["correct_answer"], item["incorrect_answers"]))

brain_for_api = QuizBrain(question_bank_from_api)
brain_for_api.next_question_API()