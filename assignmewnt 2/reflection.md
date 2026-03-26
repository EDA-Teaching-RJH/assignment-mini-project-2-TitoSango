# Reflection

## Project Overview
I created a Python application that reads student data from a CSV file, validates the data, stores valid entries as objects, processes grades, and writes the results to an output file.

## Concepts Demonstrated
This project demonstrates several module concepts. I used Object-Oriented Programming by creating a Person superclass and a Student subclass, which shows inheritance. I used Regular Expressions to validate names, emails, and mark values. I used File I/O by reading data from a CSV file and writing processed results to a text file. I also used Python libraries such as csv, re, and statistics, and I created my own reusable utility module in utils.py. Finally, I added testing for the main functions in the project.

## Development Process
I began by planning a simple application that could cover multiple assessment categories at once. First, I created the class structure for Person and Student. Then I built the utility functions for validation, file reading, and processing. After that, I connected everything in the main application so the program could display results and generate an output report. Finally, I added tests and comments to make the code clearer and more robust.

## Challenges
One challenge was making sure the project structure stayed organised. At first, it would have been easy to put everything into one file, but that would have become messy and harder to explain. I solved this by separating the classes, reusable functions, and main execution into different files. Another challenge was designing regex patterns that were simple but still useful for filtering invalid input.

## Learning Outcome
This project improved my understanding of how different Python concepts can work together in one complete application. It also helped me understand inheritance more clearly, as well as the importance of validation, testing, and modular design.