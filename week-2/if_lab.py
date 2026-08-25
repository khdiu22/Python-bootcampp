
name = input("enter your name:")

if name == "":
    print("name is empty")
    
else:
    score = int(input("enter your score:"))

    courses = input("chose the courses")

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
        print("grade:", grade)

    match courses :
        case "python":
            print("You chose",)
        case "java":
            print("you chose" )
        case "css":
            print("you chose" )
        case _:
            print("Course not available")      
