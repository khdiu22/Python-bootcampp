from copy import deepcopy

students = [
    {"name": "khdijah", "scores": [80, 70, 90]},
    {"name": "dana", "scores": [40, 50, 55]},
    {"name": "Nora", "scores": [60, 75, 65]}
]
report = [
    {
        "name": student["name"],
        "scores": student["scores"],
        "average": round(sum(student["scores"]) / len(student["scores"]))
    }
    for student in students
]
print(report)
passed_students = [
    student
    for student in report
    if student["average"] >= 60
]

print(passed_students)
students_by_name = {
    student["name"]: student
    for student in passed_students
}
print(students_by_name)
backup = deepcopy(passed_students)

backup[0]["scores"][0] = 100
print("Original:", passed_students)
print("Backup:", backup)