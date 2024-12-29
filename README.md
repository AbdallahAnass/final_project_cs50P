# GPA Calculator

#### Video Demo: <https://youtu.be/LTSGe90CNH0>

#### Description:

### Academic GPA Calculator

The GPA Calculator is a python app that allows you to calculate your academic GPA in university or school that has the GPA system with credit hours for each course.

### Manual input of points

- User can input the name of the course and also the credit hours as well as the total points that he scored.

### CSV file input

- User can input all the courses details through a CSV file done manually or by software like Microsoft Excel or libre office or any other application that supports generating CSV files.

### Table of courses

- After the user enters all the courses details, he has the option to print out a nice formatted table of the courses that has been added.

### Show GPA

- User can select the option to display GPA that is calculated based on the courses he added.

### Getting Started

1- Install python
2- Install PrettyTable library
3- Run the program using `./project.py`

## planning.txt file

- In this file you can see the scale of grades which that has been used to calculate the quality points of each course in the application.
- Also the grade letters and the corresponding total number of points as a range for each grade.
- Finally, 4 steps of the general flow of the application.

### project.py file

- This file contains the main logic and information about the program. It has different functions that breaks the hole application into smaller services.
- First it contains libraries importing such as csv library which used to interact with csv file and also PrettyTable library which is used to display the well formatted table of courses.
- Second it contains two global variables `total_points`, which is used to store the total number of points of all the courses, and `total_hours` which is used to store the total number of credit hours of all the courses.
- Third it contains a global array the is used to store all entered courses information as a dict object that has three main keys: `name`(which represents the name of the course), `credit` (which represent the credit hour of the course), `grade` (which represents the points that the user achieved in the course).
- fourth it contains 3 Error classes definitions that represent different errors throughout the application

#### `main()`

- This function is the main function. It used first to display a welcome message for the user and then display a menu for the user to choose from the process that he want to preform.

#### `get_user_input()`

- This function allows the user to enter the details of the course and then pass it the `add_course` function to continue the application flow.

#### `validate_input(name, credits, grade)`

- This function validates and checks the entered details by the user for each course. First it checks the length of the course title (name) that has a limit of 10 characters. Second it checks the number of credits hours which can't exceed the 8 credits hours. Third it checks the total number of points scored in the course.

#### `add_course(name, credits, grade)`

- This function adds a new course to the global list of courses that we defined it on the start of the program. It adds the new course as a dict.

#### `calculate_grade()`

- This function calculates the `grade_letter` and `points` for each course added the the `courses` list based on the points that the user scored in the course. It also has a dict which maps each `grade_letter` to a number of points. Then it calculates the number of points and adds it to the course `points` field in each course in the list.

#### read_csv()

- This function prompts the user to enter a path for a CSV file containing the courses which he took. Then it parses the CSV file and adds it to the `courses` list.

#### show_courses()

- This function displays the courses information in a well formatted table using the PrettyTable library for the user to review and validate that he entered the correct information.

#### print_error

- This function prints the error message and handle them trough the program using the error classes definitions that was added to be top of the file.

### test_project file

- This file contains the unit tests for some functions mentioned in the `project.py` file.

### test.csv file

- This file contains a sample of a CSV file which contains the courses and their information. The CSV file is used to check the working of `read_csv()` function in the `project.py` file.
