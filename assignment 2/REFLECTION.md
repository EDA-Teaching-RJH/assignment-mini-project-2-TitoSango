Reflection

Project Overview
I created a Python application that reads student data from a CSV file, validates the data, stores valid entries as objects, processes grades, and writes the results to an output file.

Concepts Demonstrated
This project demonstrates several key module concepts. I used Object-Oriented Programming by creating a Person superclass and a Student subclass, which demonstrates inheritance. I used Regular Expressions to validate names, emails, and mark values before processing them. I used File I/O by reading data from a CSV file and writing the processed results to a text file. 

I also used Python libraries such as csv, re, and statistics, and created my own reusable module in utils.py to organise validation and processing logic. In addition, I implemented testing for the main functions in the project to ensure they behaved correctly.

Development Process
I began by planning an application that could cover multiple assessment criteria at once. I first created the class structure for Person and Student. Then I developed the utility functions for validation, file reading, and processing. After that, I connected everything in the main application so the program could display results and generate an output report. Finally, I added tests and comments to improve clarity and reliability.

Challenges
One challenge I encountered was related to file structure and execution. Initially, the program could not find the CSV file because I was running the script from the wrong directory. I fixed this by ensuring all files were in the same folder and running the program from the correct location.

Another issue I faced was with testing, as pytest was not recognised at first. I resolved this by running it using `python3 -m pytest`, which worked correctly in the development environment.

I also found it challenging to design regex patterns that were simple but still effective for filtering invalid input.

Learning Outcome
This project improved my understanding of how different Python concepts work together in a complete application. It helped me better understand inheritance, validation using regular expressions, and the importance of structuring code into separate modules. It also reinforced the value of testing and proper file organisation when building programs.
