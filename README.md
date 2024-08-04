# Kaun Banega Arabpati (KBA) PYTHON RELATED QUIZ GAME
 
# Introduction
Welcome to the Kaun Banega Arabpati quiz program! This interactive Python program mimics the popular quiz show, where players answer multiple-choice questions to win increasing amounts of money. This README provides an overview of the program’s features, how it works, and instructions for customizing the quiz by adding or modifying questions.

# Features
1. Interactive Quiz: Players can participate in a quiz where each correct answer increases their winnings.
Multiple Choice Questions: Each question has four possible answers, and players must select the correct one.

2. Progressive Winnings: The prize money increases with each correct answer, with milestone amounts guaranteed at certain points.

3. Quit Option: Players can quit the game at any point and take home their current winnings.

4. Customizable: The quiz can be easily customized by adding, removing, or modifying questions.
How the Code Works

5. Data Initialization:
The python list contains all the questions, each with its options and the correct answer's index.
The levels list contains the prize amounts corresponding to each question.

6. User Interaction:
The program begins by asking the user for their name and date of birth.
It then welcomes the user and starts the quiz.

7. Quiz Loop:
For each question, the program displays the question and its options.
The user inputs their answer, and the program checks if it is correct.
8. If the answer is correct, the program updates the user's winnings.
If the user answers incorrectly, the game ends, and the user takes home their current winnings.
The user can also choose to quit the game at any time, taking home their current winnings.

9. Milestone Prizes:
Certain milestones guarantee a minimum prize, even if the player answers incorrectly afterward (e.g., Rs. 10,000, Rs. 320,000, Rs. 10,000,000).

10. Game End:
The game ends when the player answers incorrectly or answers all questions correctly.
The program congratulates the user and displays their final winnings.

# How to Customize the Quiz
You can easily add, remove, or modify questions to tailor the quiz to your needs.

"Adding a Question"
To add a question, append a new list to the python list. 

1. Each question should follow this format:
python
Copy code
[
    'Question text',
    'Option 1',
    'Option 2',
    'Option 3',
    'Option 4',
    correct_option_index
]

2. For example, to add a new question:
python
Copy code
python.append([
    'Q16. What is the capital of France?',
    '1. Berlin',
    '2. Madrid',
    '3. Paris',
    '4. Rome',
    3
])
3. Removing a Question
To remove a question, simply delete the corresponding list from the python list. For example, to remove the first question:

python
Copy code
del python[0]

4. Modifying a Question
To modify a question, update the relevant list in the python list. For example, to change the text of the first question:

python
Copy code
python[0] = [
    'Q1. What is the capital of Germany?',
    '1. Berlin',
    '2. Madrid',
    '3. Paris',
    '4. Rome',
    1
]
# Install pip
pip install colorama
# Feedback and Suggestions
We value your feedback! If you have any suggestions for new features, questions, or improvements, or if you encounter any issues while using the program, please let us know. Your input will help us enhance the quiz experience.

# Author
Made by Ishant Yadav
  with ![alt text](image.png) in India.
