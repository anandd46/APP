import random

questions = [
    "What is a Python module?",
    "What is a Python package?",
    "What is recursion?",
    "What is a lambda function?"
]

question = random.choice(questions)

print("--- Python Quiz ---")
print("Question:")
print(question)

answer = input("Enter your answer: ")

print("Your answer is:", answer)
print("Answer recorded successfully")
