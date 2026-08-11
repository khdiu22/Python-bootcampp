students = ["sara,nada,,omar"]
print(students)
print(students[0])
print(type(students))

colors = ["red","green","blue"]
print(colors[0])
print(colors[1])
print(colors[-1])

numbers = [10,20,30,40,50]
print(numbers[1:4])#[20,30,40]
print(numbers[:3]) #[10,20,30]
print(numbers[::2]) #[10,20,30]
print(numbers[::-1]) # reversed


tasks = ["plan","code"]
tasks[0] = "design"
tasks.append ("test")
tasks.insert(1,"review")
print(tasks) 

scores = [88,72,95,81]
scores.remove(72)
last = scores.pop()
scores.sort()
print(scores)
print(last)

students = ["sara,","omar","lana"]
for student in students:
    print(student)
for  student in enumerate (students): #تعداد
    print (student)

students = ["sara,","omar","lana"]
for student in students:
    print(student)
for  index,student in enumerate (students): #تعداد
    print (index,student)
    
matrix = [
    [1,2,3],
    [4,5,6]
]    
print(matrix[0])
print(matrix[1][2]) #6

loction = (24,7136,46,6753)
print( loction[0])
print( loction[-1])
#loction[0]=25 #TYPEEROR
student = ["sara","22","python",1,1]
name , age,course,*outher =student
print(name)
print(age)
print(course)
print(outher) #unbacking اذا مااعرف 
print(course)


skils ={"python","git","python"}
skils.add("Django")
print(skils)
print("git" in skils)
print(len(skils))
backend = {"python","Django","SQL"}
frontend= {"Html","css","javascript","SQL"}
print(backend|frontend) #union
print(backend&frontend) #intersection
print(backend-frontend) #difference

student ={
    "name":"sara",
    "age":22,
    "course":"python"
}

print(student["name"])
#pop تحذف
# git تاخذ تو ارقيومنت هي نفس الاندكس
#next

student = {"name":"sara","score":90}
student["score"] = 95
student["grade"] = "A"
email = student.get("email" ," not set")                
grade = student.pop("grade")




student = {"name":"sara","score":95}
for key in student:
   print(key)
for key,value in student.items():
    print(key,value)
    
    
names =["sara","lana"]
skils ={"python","git","student"}
student ={"name":"sara", "score": 95}
print(len(names))
print("python" in skils)
print(student[scores])
print("python" in skils)
print("name"in student) #checks keys

for student in students:
    print(student["name"], student ["score"])
    



