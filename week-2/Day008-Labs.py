#LAP1
from os import name

results = 10 + 5 *2 -4 /2

print(f"Results: {results}")


#LAP2
total_items = 17
box_capacity = 5
full_box = total_items//box_capacity
remaining_items  = total_items % box_capacity

print(f"you can fill up to {full_box} boxes")
print(f"you will have {remaining_items} remaining items")



#LAP3
base_calc = 2 +3 * 2 **2
gcalc = (2 +3) * 2 **2

print(f"base calculation result: {base_calc}")
print(f"grouped calculation result: {gcalc}")


#LAP4
user_age = 25
has_permission = True
is_eligible = (True if (user_age >= 18 and has_permission) else False)

print(f"Is eligible: {is_eligible}")

#LAP5
Score = 10
Score +=5
#score = score +5
Score *=5
print(f"Final score: {Score}")


#LAB 6
membership = ["Admin", "Editor", "Viewer"]
current_membership = "Editor"
if current_membership in membership:
    print("welcome")

if current_membership or "Admin" in membership:
    print("welcome")

if current_membership and "Viewwer" in membership:
    print("welcome")

membership = ["Admin", "Editor", "Viewer"]
current_membership = ["Editor"]
if current_membership[1] in membership:
    print("welcome")

membership = ["Admin", "Editor", "Viewer"]
current_membership = "Editor"
if current_membership == membership[1]:
    print("welcome")

membership = ["Admin", "Editor", "Viewer"]
current_membership = "Editor"
if current_membership[0] == "E":
    print("welcome")

#LAP7
sentence = ["Python" , "web" ,  "development"]

# new_sentence = sentence.find("web") # غلط لان find  stringتاتي فقط مع ال 
if "Python" in sentence:
    print("Macth found")
else:
    print(" no match found")    
#print(type(new_sentence))
#print(f"Sentence: {new_sentence}")


#LAB 8
message = "Python Programming"
first_char = message[0]
last_char = message[-1]
print(f"First character is {first_char} and last character is {last_char}")

#Slicing 
sliced_message = message[:6] # 0 index to 5
print(sliced_message) # = Python
reversed_message = message[::-1] # ابدا من النهايه وارجع
print(reversed_message) #= gnimmargorP nohtyP
print(f"""Your message was {message}
if we take the first 6 characters is will be {sliced_message}
if we reverese it, it will be {reversed_message}
""")


#LAB9
my_email = "user@example.com"
cleaned_email = my_email.strip().lower()
message = message.title() #  اول حرف تخليه كبير
print(f"Your cleaned email is: {cleaned_email}")
print(f"Your formatted message is: {message}")


 #LAB 10
csv_text = "apple,orange,banana,cherry,dates"
splitted_text = csv_text.split(",") # []
print(sliced_message)
joined_text = " - ".join(splitted_text)
print(f"""Your list is {csv_text}
Splitted like this {splitted_text}
rejoned like this {joined_text}
""")

#LAB 11
name = "Khalid"
try:
    # strings are immutable; create a new string instead of assigning to an index
    name = "A" + name[1:] #1 to end + 0 = A = Ahalid
except TypeError as e:
    print(e)


x = 5
y = 5
if (x == y):
    print("They are the same value")
else:
    print("They are not the same value")

x = 5
y = 5
if (x is y):
    print("They are the same object")
else:
    print("They are not the same object")

print(id(x))
print(id(y))

x = [5]
y = [5]
if (x is y):
    print("They are the same value")
else:
    print("They are not the same value")

print(id(x))
print(id(y))

#LAB 12
message = "Python Web Development"
new_message = message.replace("Development", "Programing")
print(new_message)

is_online = None
print (is_online == None)
is_online = None
print (is_online != None)

is_online = None
if(is_online): # نفس is_online == True
    print("True")
elif(is_online != True and is_online != False):
     print("False")
else:
    print("None")
#print(is_online)

