"""Week 2 project: Student Grade Calculator.

Accepts a student's name and marks, validates the marks, and displays a grade.
"""

def calculate_grade(marks):
    """Return the grade and an encouraging message for marks from 0 to 100."""
    if marks >= 90:
        return "A", "Excellent work! Keep shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! Keep practising! 💪"
    elif marks >= 60:
        return "D", "You passed! Work hard to improve! 📚"
    else:
        return "F", "Don't give up. Learn from mistakes and try again! 🌱"


def get_valid_marks():
    """Keep asking until the user enters a whole number from 0 to 100."""
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Invalid marks. Please enter a number from 0 to 100.")
        except ValueError:
            print("Invalid input. Please enter a whole number, such as 85.")


def main():
    """Run the Student Grade Calculator."""
    name = input("Enter student name: ").strip()
    while not name:
        print("Student name cannot be empty.")
        name = input("Enter student name: ").strip()

    marks = get_valid_marks()
    grade, message = calculate_grade(marks)

    print("\n" + "=" * 32)
    print(f"RESULT FOR {name.upper()}")
    print("=" * 32)
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")
    print("=" * 32)


if __name__ == "__main__":
    main()
