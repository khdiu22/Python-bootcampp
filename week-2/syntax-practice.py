import csv


student_name = "nada"  
print(student_name)
score = 95
if score >= 90:
    print("Excellent score")
else:
    print("thank you)")



student_name, student_age, student_is_registered = "nada", 24, True
course_name = "Python"
teacher_name = "python-khdijah"

print(f"""
welcome {student_name} to {course_name}
you are {student_age} years old
registered: {student_is_registered}
""")




student_name, student_age, student_is_registered = "nada",24,True
print(type(student_name))

print(type(student_age))
print(type(student_is_registered))
print(isinstance(student_age,int))


age =input("enter your age:")
if (isinstance(age,int)):
    print("you are",age+5,"after 5 years")
else:
    print("you are",int(age)+5,"after 5 years")
    
    
teacher_name ="khdijah"
print(teacher_name)

index =int(input("enter your index:"))

if (index <= len(teacher_name)):
    print(teacher_name[index])
else:
    print("index out of range")
#lap 3 in week2 (الاثنين) 

 
student_name = "Ali"
program_name ="Python Bootcamp"
student_age = 21
student_is_registered = True
print(f"""
student_name ={student_name}
program_name = {program_name}
student_age = {student_age}
registered ={student_is_registered}
welcome {student_name} to {program_name}
you are {student_age} years old
Thank you for joining us!
""")
x = 0
y = 1
x , y = y , x
print(x)
print(y)

