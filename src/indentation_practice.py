def check_even_odd(num):      # No indent
    if num % 2 == 0:          # 4 spaces indent
        print("Even")         # 8 spaces (2 levels)
    else:                     # 4 spaces
        print("Odd")          # 8 spaces
check_even_odd(4)  # Output: Even
check_even_odd(9)  # Output: Odd

def greet_user(name):
    print("Welcome!")
    if name == "Admin":
        print("Hello Admin, you have full access.")
    else:
        print(f"Hello {name}, limited access granted.")
    print("Login successful.")
# call the function
greet_user("Admin")
greet_user("Jitendra")


def check_scores(scores):
    print("Checking scores...")
    for score in scores:
        if score >= 90:
            print("Excellent:", score)
        elif score >= 75:
            print("Good:", score)
        else:
            print("Needs Improvement:", score)
    print("Check complete.")

check_scores([95, 82, 67, 100, 73])


def analyze_students(students):
    print("Analyzing student scores...")
    for name, marks in students.items():
        print("Student:", name)
    for subject, score in marks.items():
        if score >= 90:
            print(subject, "- Excellent:", score)
        elif score >= 75:
            print(subject, "- Good:", score)
        else:
            print(subject, "- Needs Improvement:", score)
    print("-----")

students = {
    "Amit": {"Math": 92, "Science": 85},
    "Neha": {"Math": 76, "Science": 90},
    "Ravi": {"Math": 68, "Science": 74}
        }

analyze_students(students)