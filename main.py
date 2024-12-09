# Initial values for the GPA
total_points = 0
total_hours = 0

# Array for all the courses of the student
courses = []

# CourseNameError definition
class CourseNameError(Exception):
    """
    Exception raised when the course name is invalid length.
    """
    pass


# CreditError definition
class CreditError(Exception):
    """
    Exception raised when the course credit is invalid.
    """
    pass


# GradeError definition
class GradeError(Exception):
    """
    Exception raised when the course credit is invalid.
    """
    pass

def main():
    # Welcome Message
    print("Welcome to the GPA Calculator\n")
    print("Enter the name, credit hours and the total grade in the course for each course")
    print("Press ctrl + D to end and display the result\n")

    # Getting user input
    get_user_input()
    print()


def get_user_input():

    while (True):
        try:
            # Taking input from the user
            name = input("Enter course name: ")
            credits = input("Enter course credits: ")
            grade = input("Enter course grade out of 100: ")
            print()
        
        # Ending the program
        except EOFError:
            break

        # Validating user input
        if not validate_input(name, credits, grade):
            continue

        # Adding course to the courses list as a dict
        course = {
            "name": name,
            "credits": credits,
            "grade": grade
        }

        courses.append(course)

    return




def validate_input(name, credits, grade):
    # Checking for a valid in range name
    if len(name) > 10 or len(name) <= 0:
        print_error(CourseNameError, message="outOfRange")

    
    # Checking for a valid credit hours
    try:
        # Checking if it is not a number (integer)
        credits = int(credits)

        # Checking for a valid range
        if credits <= 0 or credits > 8:
            print_error(CreditError, message="outOfRange")
            return False

    except ValueError:
        print_error(CreditError, message="Not a number")
        return False

    # Checking for a valid course grade
    try:
        # Checking if it is not a number
        grade = float(grade)

        # Checking for a valid range
        if grade < 0 or grade > 100:
            print_error(GradeError, message="outOfRange")
            return False

    except ValueError:
        print_error(GradeError, message="Not a number")
        return False
    

    return True



def print_error(Error, message):
    print("\n\n")
    print("-"* 20)
    print("\n")

    # If course name is blank or more than 10 letters (out of range)
    if Error == CourseNameError and message == "outOfRange":
        print("Invalid course name it should not be more than 10 letters")
        print("Try to enter the course code instead of the name")

    # If course credit is blank or not a number
    elif Error == CreditError and message == "Not a number":
        print("Invalid course credit hour, hours should be an integer number")
    
    # If course credit 0 or less or more than 8 hours per course
    elif Error == CreditError and message == "outOfRange":
        print("Invalid course credit hour, hours should be between 1 and 8")
        print("Try to enter a valid credit hour")
    
    # If course grade is blank or not a number
    elif Error == GradeError and message == "Not a number":
        print("Invalid course grade points, grade should be an integer number")
        
    # If course grade is less than 0 or more than 100
    elif Error == GradeError and message == "outOfRange":
        print("Invalid course grade, grade should be between 0 and 100")
    
    print("\n")
    print("-"* 20)
    print("\n\n")
    
    return


if __name__ == "__main__":
    main()