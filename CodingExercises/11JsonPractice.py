# Quiz building

import json

with open("11JsonPractice.json", 'r') as file:
    content = file.read()

data = json.loads(content)

for que in data:
    print(que['question'])
    for index, alternative in enumerate(que["alternatives"]):
        print(f"{index+1} - {alternative}")
    user_answer = int(input("Enter your answer: "))
    que['user_selection'] = user_answer-1

print(data)

score = 0
for index, answer in enumerate(data):
    if answer['noted_answer'] == answer['user_selection']:
        score += 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"
    print(f"{index+1} - Your Answer: {answer['user_selection']+1}, "
          f"Correct Answer is: {answer['noted_answer']+1}")


print(f"{score} / {len(data)}")
