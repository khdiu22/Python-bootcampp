students = [
    {
        "name": "Sara",
        "scores": (90, 85, 95),
        "skills": {"Python", "HTML"}
    },
    {
        "name": "khdijah",
        "scores": (80, 75, 90),
        "skills": {"c+", "CSS"}
    },
    {
        "name": "Dalal",
        "scores": (100, 90, 95),
        "skills": {"java", "Django"} #set
    }
]


for student in students:
    total = 0 

    for score in student["scores"]:
        total += score

    average = total /len(student["scores"])

    student["average"] = average 
    
    student["skills"].add("Git")


for student in students:
    print("Name:", student["name"])
    print(f"average: {student['average']:.2f}")
    print("Skills:", student["skills"])




