# Lap 1
for attempts in range(3):
    print(f"Attempts: {attempts +1}")
    
# lap2
for num in range(2,11,2): # النهايه هنا 11
    print(num)
    
#Lap3
for secondToLanch in range (10,0,-1):
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
        print(f"{number}is odd")
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


#Lap11 #  الشرط غير صحيح  طالما المستخدم كتب بيكون باللوب حتى يكون فارغ ويطلع
password = "python123"
print("Please enter youer password :")
while password != "":
  
    password = input("Enter youer password:")




