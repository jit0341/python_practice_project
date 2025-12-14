## An enhanced version or a different
# iteration of the basic quiz game.

def ask_question(question, correct_answers):
    answer = input(question + " ")
    if answer.lower() in correct_answers:
        print("Correct!")
        return 1
    else:
        print(f"Wrong! The correct answer is {correct_answers[0]}.")
        return 0

def run_quiz():
    print("Welcome to the Python Quiz!")
    print("-----------------------------")
    
    questions = [
        ("1. What is the output of 2 + 2?", ["4"]),
        ("2. What keyword is used to define a function in Python?", ["def"]),
        ("3. Which data type is used to store True or False?", ["bool", "boolean"]),
        ("4. What is the file extension of Python files?", [".py"]),
    ]

    score = 0
    for q in questions:
        score += ask_question(q[0], q[1])
    
    print("-----------------------------")
    print(f"You got {score} out of {len(questions)} questions correct.")
    percentage = (score / len(questions)) * 100
    print(f"That's {percentage:.2f}%!")

run_quiz()
