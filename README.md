# Week 1: Python Basics — Personal Introduction Program

## Project overview
This beginner project asks the user for their name, age, city, course, and hobby, then prints a friendly personal introduction.

## Learning objectives
- Understand variables and strings.
- Receive information with `input()`.
- Display text with `print()`.
- Use `.strip()` to remove extra spaces.
- Use f-strings to insert variable values into sentences.
- Practise running a Python file from the terminal.

## Files
```text
week1-python-basics/
├── README.md
├── personal_intro.py
├── requirements.txt
├── sample_output.txt
├── test_cases.txt
├── submission_notes.md
└── .gitignore
```

## Requirements
- Python 3.10 or newer (Python 3.13 is supported).
- No third-party packages are needed.

## Setup and run (Windows)
1. Install Python from https://www.python.org/downloads/ and enable **Add Python to PATH** during installation.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Open **Terminal → New Terminal**.
5. Run the program:
   ```powershell
   py personal_intro.py
   ```
   If the `py` command is unavailable, try `python personal_intro.py`.

## Example output
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

## How the program works
1. Each `input()` asks a question and saves the answer in a variable.
2. `.strip()` removes accidental spaces at the beginning or end.
3. `print()` displays the introduction.
4. The f-strings place each saved answer into a readable sentence.

## Testing
See [test_cases.txt](test_cases.txt) for manual test examples. Try normal inputs, names with spaces, and different hobbies. The program should display the values entered by the user.

## Screenshot requirement
A real `screenshot.png` should show the program running in your terminal. To create it:
1. Run `py personal_intro.py` in VS Code.
2. Enter sample values and keep the final output visible.
3. Press **Win + Shift + S**, select the terminal area, and save the image as `screenshot.png` in this repository folder.
4. Upload `screenshot.png` to the repository on GitHub.

I have not included a fabricated screenshot: capture the actual program running on your computer for genuine submission evidence.

## What I learned
I learned how to store text in variables, ask questions using `input()`, display results with `print()`, and format a personalised message using f-strings.
