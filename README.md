# 🧠 Quiz Game

A simple terminal-based quiz game built in Python that tests your knowledge across various topics!

## 📂 Project Structure

Quiz_game/
├── quize_question_list.py # Module containing 200 questions and answers
├── Quiz.py # Main script to play the quiz
└── README.md # Project documentation

## 📜 Description

This is a console-based quiz game where you can test your general knowledge in topics like:
- Sports
- General Knowledge
- Chemistry
- Physics
- Scientists
- Anime
- Games
... and more!

### 📁 `quiz_question_list.py`
- Contains a single function `Questions()`  
- Returns a dictionary of **200** question-answer pairs  
- Acts as the question bank module

### ▶️ `quiz.py`
- This is the **main game** file
- Imports questions from `quiz_question_list.py`
- Lets the user play the quiz interactively
- Supports simple text input for answers
- Checks correctness and shows the score
