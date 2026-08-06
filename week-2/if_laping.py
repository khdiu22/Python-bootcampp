 # Lap1
# age =20
# if age >= 18 :
#     print("welcome")
#     print("chode completed")
# #Lap2
# temprator = 31
# if temprator >= 35: 
#     print("its hot outside")
# else:
#     print("Cool")
    
 #Lap3 #يفحص الشرط الصحيح بعدها يطبعه هو فقط حتى لو كان الي بعده صحيح
Score = 2000
 
if Score >= 90:
     print("A")
elif Score >= 80:
     print("B")
elif Score >= 70:
     print("C")
else:
     print("You need too improve")

#LAB 4  
is_active = True
is_verified = True
role = "editor"
is_blocked = False

if is_active and is_verified:
    print("Account is ready")

if role == "admin" or role == "editor":
    print("User can edit")

if not is_blocked:
    print("User is not blocked") 

else:
    print("User is blocked")
    
    
    
    
    
    
    
# #lap5 Nested if #تنفذ else للجمله الشرطيه الثانيه لان الشرط الاول صحيح لكن الثاني لا
#if داخل if
account_active =True
has_permission =False
if account_active:
  if has_permission:
     print("ACCES GRANTED")
  else:
      print("Acces denied")
else:
    print("Account is not active")

# #lap6
# name = "khdijah"
# cart =[]  
# balance = 990
# if name:
#     print("name has value")
# if not cart: #not=True
#      print("Youer cart is empty")
# print(bool(balance)) # اي رقم غير الصفر يعتبر صحيح  bool =True or False

# #lap7
name = input("Enter your name: ").strip()  #  لاتحذف في وسط الاسم حذف المسافات من البداية والنهاية

if not name:
    print("Please enter a name")
elif not name.replace(" ", "").isalpha():
    print("Name must contain letters")
else:
    print(f"Valid name: {name}")
    print(name.replace(" ", ""))

# #lap8
# age_text = input ("enter yoer name".strip)
# if age_text.isdigit():
#     age = int(age_text)
#     print(f"you will be{age+5}in 5 years")
# else:
#     print("Enter a number")   

       
# #Lap9
# Score_text = input("Enter number between 0 and 100: ")
# if Score_text.isdigit():
#     score_x = int(Score_text)
#     if score_x >= 0 and score_x <=100:
        
#         print("Valid score")
#         is_score_valid = True
#     else:
#         print("Scores is invalid")
# else:
#     print("Plase enter a number")


#Lap10
membership = ["Admin","Editor","Viewer"]
current_membership =input("Enter youer membership:").strip().lower()
if current_membership.title()in membership:
    print("You are allowed to view the content")
    print(current_membership)
else:
    print("Please contact admin team")
    print(current_membership)
    
 #Lap11 
command = input("Please enter a command (start,stop,status)")
match command:
    case "start":
     print(".......starrting system")
    case "stop":
        print("stoping system")
    case "status":
        print("System is up and running👌")
    case _:
        print("Please enter a proper command")