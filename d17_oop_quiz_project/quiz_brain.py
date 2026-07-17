
#TODO: Ask the questions -> next_question()
#TODO: Checking if the answer were correct
#TODO: Check if we're at the end of the quiz

#TODO: Sample Question ---> Q.1: A slug's blood is green. (True / False):

class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.score = 0
        self.question_list = q_list
        
    
    def next_question(self):
        for object in self.question_list:
            user_choice = input(f"Q. {self.question_no + 1}: {object.text} (True / False)\n").title()
            correct_answer = object.answer
            if user_choice != correct_answer:
                print("Your Answer is Wrong.")
                print(f"Your Final Score: {self.score}")
                break
            elif self.question_no <= len(self.question_list):
                print("Correct")
                self.question_no += 1
                self.score += 1
                if self.question_no == len(self.question_list):
                    print("Game Ends")
                    print(f"Your Final Score: {self.score}")
                    break
            else:
                print("Game Ends")
                print(f"Your Final Score: {self.score}")
                break
    
    def next_question_API(self):
        for object in self.question_list:
            user_choice = input(f"Q. {self.question_no + 1}: {object.text} (True / False)\n").title()
            if user_choice != object.q_correct_ans:
                print('Your answer is Wrong.')
                print(f"Your final score: {self.score}")
                break
            elif self.question_no <= len(self.question_list):
                print("Correct")
                self.question_no += 1
                self.score += 1
                if self.question_no == len(self.question_list):
                    print("Game Ends")
                    print(f"Your Final Score: {self.score}")
                    break
            else:
                print("Game Over.")
                print(f"Your Final Score: {self.score}")
                break