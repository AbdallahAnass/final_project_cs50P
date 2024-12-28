import project

def test_validate_input():
    # Course name exceeds length
    assert project.validate_input("Algorithm", 8, 99) == True
    assert project.validate_input("Math 1", 8, 99) == True

    assert project.validate_input("Data structure and algorithm", 8, 99) == False
    assert project.validate_input("Computer organization", 8, 99) == False

    # Credit hours out of range
    assert project.validate_input("TM105", 7, 70) == True
    assert project.validate_input("EL112", 4, 70) == True

    assert project.validate_input("M269", 12, 99) == False
    assert project.validate_input("M269", -1, 99) == False

    # Credit hours not a number
    assert project.validate_input("TM112", 8, 87) == True
    assert project.validate_input("GR118", 3, 60) == True

    assert project.validate_input("TM112", "three", 87) == False
    assert project.validate_input("TM112", "3 credits hours", 87) == False

    # Grade is out of range
    assert project.validate_input("TM105", 4, 70) == True
    assert project.validate_input("TM103", 3, 66) == True

    assert project.validate_input("M269", 12, 101) == False
    assert project.validate_input("MT101", 12, -1) == False

    # Grade is not a number
    assert project.validate_input("MT132", 4, 77) == True
    assert project.validate_input("MT131", 3, 66) == True

    assert project.validate_input("TM112", 8, "nine") == False
    assert project.validate_input("EL099", 8, "sixty four") == False


def test_add_course():

    # Adding a course already exists
    project.courses = [
        {"name":"TM112", "credits": 8, "grade": 99}, 
        {"name":"MT132", "credits": 4, "grade": 70}
                       ]

    assert project.add_course("TM112", 8, 99) == False
    assert project.add_course("MT132", 4, 70) == False

    # Adding a new course
    assert project.add_course("EL112", 8, 99) == True
    assert project.add_course("GR118", 8, 99) == True


def test_calculate_grade():
    # if no courses in the list
    project.courses = []
    assert project.calculate_grade() == False

    # if there are courses in the list
    project.courses = [
        {"name":"TM112", "credits": 8, "grade": 99}, 
        {"name":"MT132", "credits": 4, "grade": 91.5}
                       ]
    
    assert project.calculate_grade() == True
    
    # A grade is calculated
    project.courses = [
        {"name":"TM112", "credits": 8, "grade": 99}, 
        {"name":"MT132", "credits": 4, "grade": 91.5}
                       ]
    
    assert project.calculate_grade() == True


    assert project.courses[0]["grade_letter"] == "A"
    assert project.courses[0]["points"] == 32

    assert project.courses[1]["grade_letter"] == "A"
    assert project.courses[1]["points"] == 16

    # B+ grade is calculated
    project.courses = [
        {"name":"TM112", "credits": 8, "grade": 88}, 
        {"name":"MT132", "credits": 4, "grade": 83}
                       ]
    
    assert project.calculate_grade() == True


    assert project.courses[0]["grade_letter"] == "B+"
    assert project.courses[0]["points"] == 28

    assert project.courses[1]["grade_letter"] == "B+"
    assert project.courses[1]["points"] == 14


    # B grade is calculated
    project.courses = [
        {"name":"TM112", "credits": 8, "grade": 80}, 
        {"name":"MT132", "credits": 4, "grade": 74}
                       ]
    
    assert project.calculate_grade() == True


    assert project.courses[0]["grade_letter"] == "B"
    assert project.courses[0]["points"] == 24

    assert project.courses[1]["grade_letter"] == "B"
    assert project.courses[1]["points"] == 12

    # C+ grade is calculated
    project.courses = [
        {"name":"TM112", "credits": 8, "grade": 72}, 
        {"name":"MT132", "credits": 4, "grade": 67}
                       ]
    
    assert project.calculate_grade() == True


    assert project.courses[0]["grade_letter"] == "C+"
    assert project.courses[0]["points"] == 20

    assert project.courses[1]["grade_letter"] == "C+"
    assert project.courses[1]["points"] == 10


    # C grade is calculated
    project.courses = [
        {"name":"TM112", "credits": 8, "grade": 64}, 
        {"name":"MT132", "credits": 4, "grade": 59}
                       ]
    
    assert project.calculate_grade() == True


    assert project.courses[0]["grade_letter"] == "C"
    assert project.courses[0]["points"] == 16

    assert project.courses[1]["grade_letter"] == "C"
    assert project.courses[1]["points"] == 8


    # D grade is calculated
    project.courses = [
        {"name":"TM112", "credits": 8, "grade": 56}, 
        {"name":"MT132", "credits": 4, "grade": 50}
                       ]
    
    assert project.calculate_grade() == True


    assert project.courses[0]["grade_letter"] == "D"
    assert project.courses[0]["points"] == 12

    assert project.courses[1]["grade_letter"] == "D"
    assert project.courses[1]["points"] == 6

    # F grade is calculated
    project.courses = [
        {"name":"TM112", "credits": 8, "grade": 40}, 
        {"name":"MT132", "credits": 4, "grade": 10}
                       ]
    
    assert project.calculate_grade() == True


    assert project.courses[0]["grade_letter"] == "F"
    assert project.courses[0]["points"] == 0

    assert project.courses[1]["grade_letter"] == "F"
    assert project.courses[1]["points"] == 0


def test_calculate_GPA():
    # if no courses in the list
    project.courses = []
    assert project.calculate_GPA() == 0

    # if there are courses in the list
    project.courses = [
        {
            "name":"TM112",
            "credits": 8,
            "grade": 99,
            "grade_letter": "A",
            "points": 32
        }, 

        {
            "name":"MT132",
            "credits": 4,
            "grade": 90,
            "grade_letter": "A",
            "points": 16
        }
    ]
    
    assert project.calculate_GPA() == 4.0

    project.courses = [
        {
            "name":"TM112",
            "credits": 8,
            "grade": 99,
            "grade_letter": "A",
            "points": 32
        }, 

        {
            "name":"MT132",
            "credits": 4,
            "grade": 85,
            "grade_letter": "B+",
            "points": 14
        }
    ]
    
    assert round(project.calculate_GPA(), 2) == 3.83

    project.courses = [
        {
            "name":"TM112",
            "credits": 8,
            "grade": 64,
            "grade_letter": "C",
            "points": 16
        }, 

        {
            "name":"MT132",
            "credits": 4,
            "grade": 85,
            "grade_letter": "B+",
            "points": 14
        }
    ]
    
    assert project.calculate_GPA() == 2.5


    project.courses = [
        {
            "name":"TM112",
            "credits": 8,
            "grade": 3,
            "grade_letter": "F",
            "points": 0
        }, 

        {
            "name":"MT132",
            "credits": 4,
            "grade": 0,
            "grade_letter": "F",
            "points": 0
        }
    ]
    
    assert project.calculate_GPA() == 0