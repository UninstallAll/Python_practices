import json


with open('question.json', 'r') as file:
    content = file.read()

data = json.loads(content)


for questions in data:
    print(questions['question_text'])
    for index, alternative in enumerate(questions['alternatives']):
        print(index + 1,'-', alternative)
    user_choice = int(input('Enter your choice: '))
    questions['user_choice'] = user_choice



score = 0
for index, questions in enumerate(data):
    if questions['user_choice'] == questions['correct_answer']:
        score += 1
        result = "Correct!"
    else:
        result = "Wrong!"

    message = f"{result},{index + 1}, Your answer is {questions['user_choice']}"
    print(message)


print(data)
print(score, '/', len(data))