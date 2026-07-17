from data import question_data, api_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in api_data:
    the_question = item["question"]
    the_answer = item["correct_answer"]
    question_bank.append(Question(the_question, the_answer))

the_brain = QuizBrain(question_bank)
the_brain.next_question()


















# question_bank_from_api = []

# for item in my_data:
#     question_bank_from_api.append(QuestionAPI(item["question"], item["correct_answer"], item["incorrect_answers"]))

# brain_for_api = QuizBrain(question_bank_from_api)
# brain_for_api.next_question_API()