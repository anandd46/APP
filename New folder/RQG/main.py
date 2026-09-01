import random


quiz = [
    ("What is the capital of France?", "Paris"),
    ("What is the largest planet in our solar system?", "Jupiter"),
    ("What is the chemical symbol for gold?", "Au"),
    ("What is the square root of 64?", "8"),
    ("What is the capital of Japan?", "Tokyo"),
    ("What is the largest ocean on Earth?", "Pacific Ocean"),
    ("What is the chemical formula for water?", "H2O"),
]

random.shuffle(quiz)

print("----- Python Quiz -----")
print("Answer the following questions.\n")

score = 0

for number, (question, correct_answer) in enumerate(quiz, start=1):
    print(f"{number}. {question}")
    answer = input("Your answer: ").strip()

    if answer.lower() == correct_answer.lower():
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong. Correct answer: {correct_answer}\n")

print(f"Quiz completed! Your score: {score}/{len(quiz)}")
