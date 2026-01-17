# Password-Generator-Using-Python
This is a game made using Python Which Helps in Basics of Random , Functions , logic &amp; Error Correction
🔐 Random Password Generator in Python
📖 Overview
This project is a console-based Random Password Generator built using Python’s random module. It allows users to generate secure, randomized passwords with varying levels of complexity. The program is interactive, user-friendly, and demonstrates fundamental programming concepts such as lists, loops, functions, recursion, and input validation.

✨ Features
Difficulty Levels:

Easy (Level 1): Lowercase letters + numbers, length between 6–8 characters.

Medium (Level 2): Uppercase + lowercase letters + numbers, length between 10–15 characters.

Hard (Level 3): Symbols + uppercase + lowercase letters + numbers, length between 15–20 characters.

Randomization: Each password is generated using random.choice() for unpredictability.

Interactive Input: Users select difficulty level and decide whether to generate another password.

Replay Functionality: After each password, the program asks if the user wants to continue or exit.

Error Handling: Invalid inputs for difficulty or continuation prompt trigger re-asks, ensuring smooth user experience.

🧩 How It Works
The program greets the user with a welcome message.

The user selects a difficulty level (1, 2, or 3).

Based on the difficulty:

The program chooses the appropriate character set (easy, medium, or hard).

A random password length is selected within the defined range.

The program generates the password by randomly selecting characters from the chosen set.

The user is asked whether they want to generate another password or exit.

The process repeats until the user chooses to exit.

🛠️ Technologies Used
Python 3

Modules: random

📂 Code Structure
Character Sets: Lists of symbols, lowercase letters, uppercase letters, and numbers.

Difficulty Logic: Combines character sets into three levels (easy, medium, hard).

Main Function (making_): Handles password generation, user input, and recursion.

Condition Function: Manages continuation or termination of the program.

🚀 Example Run
Code
Welcome to the Random Password generator

Choose a Difficulty level from 1 to 3 : 3

The Passcode is : &aZ9!kQmT2@x

Do you Want To Continue ? (Yes or No) : yes
🎯 Learning Outcomes
This project demonstrates:

How to use lists to store character sets.

Combining lists to adjust password strength.

Randomization logic for secure password generation.

Functions and recursion for modular design and replay options.

User interaction through input prompts and dynamic output.

Error handling for invalid inputs.

🔒 Security Note
This generator is designed for educational purposes. While it produces strong random passwords, for real-world applications you should use industry-standard libraries such as:

secrets (Python’s secure random generator)

Password managers (e.g., Bitwarden, LastPass)

📌 Future Improvements
Add option to customize password length manually.

Include exclusion rules (e.g., avoid similar characters like O and 0).

Save generated passwords to a file.

Add a GUI interface using tkinter or PyQt.

👨‍💻 Author
Created by Midhun as a Python practice project to explore randomization, recursion, and user interaction.
