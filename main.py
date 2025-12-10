# main.py

from school.teachers import Teacher
from school.students import Student

def main():
    # Create teacher list
    teachers = [
        Teacher("Mr. Jitendra Bhartia", "Math"),
        Teacher("Pooja Mam", "Science"),
        Teacher("Nikki Mam", "English")
    ]

    # Create 25 students of Class 8
    students = [
        Student("Ankit Kumar Sahu", "8th"),
        student("Karunesh Singh","8th"),
        student("Ansh Sahu","8th"),
        student("Mona Singh","8th"),
        student("Murli Kumar Rajwade","8th"),
        student("Priyanka Sonwani","8th"),
        student("Rohit Kumar Yadav","8th"),
        student("Radha Sahu","8th"),
        Student("Sakshi Bisen", "8th"),
        student("Dhiraj Kumar Dubey","8th"),
        student("Vanshraj Singh","8th"),
        student("Prince Kumar Singh","8th"),
        student("Priyanka Sahu","8th"),
        student("Javendra Kumar Rajwade","8th"),
        student("Vikram Rajwade","8th"),
        student("Abhay Raj Singh","8th"),
        student("Chaman Kumar","8th"),
        student("Neeraj Kumar","8th"),
        student("Prashant Kumar","8th"),
        Student("Sneha Kashi", "8th"),
        student("Ayush Kumar Singh", "8th"),
        student("Arman Ansari","8th"),
        student("Shivesh Singh","8th"),
        student("Durgavati Rajwade","8th"),
        student("Amrita","8th"),
    ]

        # ... add all 25 names
    

    # Add exam marks
    students[0].add_mark("Unit Test", "Math", 85)
    students[0].add_mark("Unit Test", "Science", 78)
    students[0].add_mark("Quarterly", "Math", 90)

    students[1].add_mark("Unit Test", "Science", 88)
    students[1].add_mark("Half Yearly", "English", 76)

    # Display Teacher info
    print("Teachers:")
    for t in teachers:
        print(" ", t)
    print("\n--- Students Record ---")

    # Display Student info
    for s in students:
        print(s)
        for exam, subjects in s.exam_marks.items():
            print(f"  {exam}:")
            for subject, marks in subjects.items():
                print(f"    {subject}: {marks}")
        print()

if __name__ == "__main__":
    main()
