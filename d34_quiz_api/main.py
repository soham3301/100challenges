
import html
import requests

questions = {

}

score = 0

response = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")
response.raise_for_status()

data = response.json()["results"]

for question_group in data:
    questions[question_group["question"]] = question_group["correct_answer"] == "True"

for question, answer in questions.items():
    print(f"Score: {score}")
    print(f"{html.unescape(question)}")
    user_input = input('''
Type 1 for True
Type 2 for False
''')
    if user_input == "1":
        if answer:
            score += 1
            print("Correct")
        else:
            print("Incorrect")
    elif user_input == "2":
        if not answer:
            score += 1
            print("Correct")
        else:
            print("Incorrect")
    else:
        print("You Missed a Chance")

print(f"Total Score: {score}")