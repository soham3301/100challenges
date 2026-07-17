class Question():
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


class QuestionAPI():
    def __init__(self, q_text, q_correct_ans, q_incorrect_ans):
        self.text = q_text
        self.q_correct_ans = q_correct_ans
        self.q_incorrect_ans = q_incorrect_ans