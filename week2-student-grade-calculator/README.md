# Week 2: Student Grade Calculator

## Project overview
This beginner-friendly Python program asks for a student's name and marks, checks that the marks are valid, calculates a grade, and displays an encouraging message.

## Grade rules
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: 0-59

Marks must be a whole number between 0 and 100.

## Files and folder structure
- grade_calculator.py — main Python program
- test_cases.txt — manual test cases and expected results
- screenshots/README.md — notes for adding your own terminal screenshots
- screenshots/sample-output.svg — illustrative sample output

## Requirements
- Python 3 installed
- A terminal or command prompt

## How to run
1. Download or clone this repository.
2. Open a terminal in the week2-student-grade-calculator folder.
3. Run: python grade_calculator.py
4. Enter a student name and marks when prompted.

On Windows, you can also run: py grade_calculator.py

## Example
Enter student name: Priya
Enter marks (0-100): 85

================================
RESULT FOR PRIYA
================================
Marks: 85/100
Grade: B
Message: Very Good! Keep it up! 👍
================================

## Code and functions
- calculate_grade(marks): uses if-elif-else statements to return a grade and an encouraging message.
- get_valid_marks(): uses a while loop to keep asking until marks are a whole number from 0 to 100. ValueError is handled for non-numeric input.
- main(): gets the student's name, calls the other functions, and prints the result.

## Validation
- Empty names are rejected.
- Non-numeric marks are rejected.
- Marks below 0 or above 100 are rejected.
- The program asks again after invalid marks.

## Testing
Follow the cases in test_cases.txt. Test grade boundaries such as 59/60, 69/70, 79/80, and 89/90, as well as invalid input.

## Screenshot evidence
The sample SVG is an illustrative output preview, not a screenshot captured from a live terminal. For your own evidence, run the program in a terminal and take a screenshot showing the input and result. Save it in the screenshots folder.

## Learning objectives
This project practises input/output, comparison operators, if-elif-else, while loops, functions, and basic error handling.
