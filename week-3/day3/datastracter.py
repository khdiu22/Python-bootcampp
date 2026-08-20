#class work. 
# n = input("Enter your name: ") 
# for letter in n: 
#     print(letter) 

# ----list 
 
# students = ['Sarah' , 'Omar' , 'Lina'] 
 
# print(students) 
# print(students[0]) 
# print(type(students)) 
#student[0]="khdijah"
# 
 
# colors = ['red' , 'green' , 'blue'] 
# print(colors[0]) 
# print(colors[1]) 
# print(colors[-1]) 
# print(colors[-3]) 

 
# numbers = [10 , 20 , 30 , 40 , 50] 
# print(numbers[1:4]) # [20 , 30 , 40] 
# print(numbers[:3]) # [10 , 20 , 30] 
# print(numbers[::2]) # [10 , 30 , 50] 
# print(numbers[::-1]) #reversed 
#Slicing

# tasks = ["plan" , "code"] 
 
# tasks[0] = "design" 
# tasks.append("test") 
# tasks.insert(1 , "review") 
# print(tasks) 

# # ---- 
 
# scores = [88 , 72 , 95 , 81] 
# scores.remove(72) 
# last = scores.pop() تحذف آخر عنصر من القائمة، وفي نفس الوقت تخزنه في متغير.
# scores.sort() # ترتب من الاصغر الى الاكبر
# print(scores) 
# print(last) # 81
 
# ---- 

#students = ["sara,","omar","lana"]
#for student in students:
#    print(student)

#for  student in enumerate (students): # index + value
#    print (student)

#students = ["sara,","omar","lana"]
#for student in students:
#    print(student) 

#for  index,student in enumerate (students): # تنطبع بدون اقواس او ""
 #   print (index,student)
 
# # ---- 
matrix = [ 
     [1 , 2 , 3], # index = 0
     [4 , 5 , 6] # index =1
 
 ] 
 
print(matrix[0]) 
print(matrix[1][2]) 


# # ----tuble 
# location = (24.7136 , 46.6753) 
 
# print(location[0]) 
# print(location[-1]) 
# # location[0] = 30 # error
# # ---- 
 
# student = ("Sarah" , 22 , "Python" , True , 3) 
 
# name , age , course , *outher = student  #outer =الباقي الي ماكتبناه يضع في لست = [True,3]
# print(name) 
# print(age) 
# print(course) 
# print(outher) #   
 

# # ----set 
 
# skills = {"Python" , "Git" , "Python"} 
 
# skills.add("Django") 
# print(skills) 
# print("Git" in skills) 
# print(len(skills)) 
 
# # ---- 
# backend = {"Python" , "Django" , "SQL"} 
# frontend = {"HTML" , "CSS" , "JavaScript" , "SQL"} 
 
# print(backend | frontend) #union  اجمع عناصر المجموعه بدون تكرار
# print(backend & frontend) #intersection  تكرار
# print(backend - frontend) #difference 
 
 
# # ---- 
 
# student = { 
#     "name": "Sarah" , 
#     "age": 22 , 
#     "course": "Python", 
 
# } 
 
# print(student["name"]) 
 
# ---- 
# student = {"name": "Sara" , "score": 90} 
 
# student ["score"] = 95 
# student ["grade"] = "A" 
 
# email = student.get("email" , "Not set")  #دوري لي على المفتاح ايميل، وإذا ما لقيتيه عطيني "نوت سيت" بدل ما يطلع خطا
# grade = student.pop("grade") 
 
# print(student) 
 
# ---- 
 
# student = {"name": "Sara" , "score": 90} 
 
# for key in student: 
#     print(key) 
 
# for key , value in student.items(): 
#     print(key , value) 
 
 
# # ---- 
 
# names = ["Sarah" , "Omar"] 
# skllis = {"Python" , "Git"} 
# student = {"name" : "Sarah" , "score":95} 
 
# print(len(names)) 
# print("Python" in skllis) 
# print("name" in student) #check kyes 
# print("score" in student) #check kyes 
# print(student["score"]) 
 
# ---- 
 
# students = [ 
#     {"name": "Sara" , "score": 95}, 
#     {"name": "Omar" , "score": 88}, 
 
 
# ] 
 
# for student in students: 
#     print(student["name"] , student["score"]) 






#++++++++++++++++++++++++++++++++++++++++++++++++++++++
