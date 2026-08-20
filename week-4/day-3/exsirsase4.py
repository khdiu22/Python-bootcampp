# Practice
from pathlib import Path
import json

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)  

data_file = data_dir / "students1.json"

print(data_dir.is_dir())  
print(data_file.exists())  

students = [
    {"name" : "khdijah" , "score" :93 } , 
    {"name" : "nada" , "score": 87} ,
    {"name" : "Sara" , "score" : 98}
]


with data_file.open( "w" , encoding="utf-8") as file:
    json.dump(students, file , indent = 4)

try:
   with data_file.open( "r" , encoding="utf-8") as file:
    loaded_students = json.load(file)
   print(loaded_students)
except FileNotFoundError:
   print("Students file not found")
except json.JSONDecodeError:
   print("Invalid JSON format")


class InvalidStudentError(Exception):
    pass

def find_student(name , students ):
    for student in students:
        if student["name"] == name:
         return student
    raise InvalidStudentError(name)