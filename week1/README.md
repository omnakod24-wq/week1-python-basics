# Week 1: Python Basics — Personal Introduction Program

## Project overview
This beginner project asks the user for their name, age, city, course, and hobby, then prints a friendly personal introduction.

## What I learned
- Variables store information.
- `input()` asks the user questions.
- `print()` displays information.
- Strings and f-strings help create readable messages.
- `.strip()` removes extra spaces from the beginning and end of an answer.

## Files
- `personal_intro.py` — the Python program.
- `requirements.txt` — dependencies (none are required).
- `test_cases.txt` — simple manual tests.
- `screenshot.png` — add a real screenshot of the program running before final submission.

## Requirements
Install Python 3.10 or newer. No third-party Python packages are needed.

## Run on Windows
1. Install Python from https://www.python.org/downloads/ and select **Add Python to PATH**.
2. Open this `week1` folder in VS Code.
3. Select **Terminal → New Terminal**.
4. Run:
   ```powershell
   py personal_intro.py
   ```
   If `py` does not work, try `python personal_intro.py`.

## Example
```text
Enter your name: Alex
Enter your age: 21
Enter your city: Pune
Enter your course: BCA
Enter your hobby: Coding

--- My Introduction ---
My name is Alex.
I am 21 years old.
I live in Pune.
I am studying BCA.
My hobby is Coding.
```

## How it works
The program asks five questions, stores the answers in variables, and uses f-strings to display the information in friendly sentences.

## Testing
Check `test_cases.txt` and try different names, ages, cities, courses, and hobbies.

## Screenshot instructions
A genuine screenshot cannot be captured from GitHub itself. Run the program on your computer, press **Win + Shift + S**, select the terminal showing the output, and save the image as `screenshot.png` inside this `week1` folder. Then upload it to GitHub.
