# Lap 1
for attempts in range(3):
    print(f"Attempts: {attempts +1}")
    
# lap2
for num in range(2,11,2): # النهايه هنا 10
    print(num)
    
#Lap3
for secondToLanch in range (10,0,-1): #نبدا من 10 وونتهي 1  عد تنازلي
    print(f"t-{secondToLanch}")
    
#Lap4
course ="Python"
for leeter in course:
    print (leeter)
    
#Lap5
students = ["khdijah","sarah","dalal"]
for student in students:
    print(f"profrresing student is: {student}")
    
#Lap 6
for number in range(1,11):
    if number %2 == 0:
        print(f"{number}is even")
        print("--------") 
        
#lap7
number = [4,7,10,12,14,16,21]
even_counter = 0
if num %2 == 0: 
    even_counter +=1
print(f"total even numbers is:{even_counter *10}")       

#LAP8
prices = [25,30,55,115]
total = 0
for price in prices:
    total += price
print(f"youer total is{total}Vat {total * 0.15:.2f}")      
#print(f"youer total is{total}Vat {total * (15/100)")    
    
# LAP9
count =0
while count <5:
     count += 1
     print(f"count...{count}")
     print("LOOp completed")
# LAP10
message= "Please enter youer age"
age_text = input("please enter youer age:".strip())
while not age_text.isdigit():
    age_text = input(message).strip()
age = int(age_text)
print(f"you ard:{age}")


#Lap11 # **
#This can be deletde bec it is redundant
password = " "

print("Please enter youer password :")
password = input("Please enter your password")
while password != "1234":
  
    password = input("Incorrect password ,try agin :")
print("Access Granted!")
# Lap 12
for score in [80,55,45,90]:
    if score <50:
        pass
    print(f"if passed the{score}")
    for record in [80,55,45,90]:
        continue
    print(f"if did not skip{record}")
    for badscore in [80,55,45,90]:
        if badscore <50:
            break
        print("we saw{badscore}")
#lap 13
for row in range(1,4):
    for colum in range(1,4):
        print(f"ROW: {row}, colum:{colum}")

for row in range(1,4):
    for colum in range(1,4):
        print(f"{row}x{colum}={row * colum}")
# lap 13,12 how to thinking like nested loop
#row = 1
    #colum = 1
    #colum = 2
    #colum = 3

#row = 2
    #colum = 1
    #colum = 2
    #colum = 3

#row = 3
    #colum = 1
    #colum = 2
    #colum = 3#

