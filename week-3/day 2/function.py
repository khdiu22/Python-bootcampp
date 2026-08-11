def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
score = float(input("Enter your score: "))
print(f"Your score is: {calculate_grade(score)}")


#اذا حطيت للبراميتر قيمه تصير فرعيه 

 #LAB 1
def greet():
    print("Welcome to python")
#greet()

#========================================================================================#
# LAB 2
def show_menu():
    print("1- coffee")
    print("2- Tea")
    print("3- Ginger")
# show_menu()
print("Outside the call")
# show_menu()

#========================================================================================#
# LAB 3
print("Line one")
def gotoFunc():
    print("From within the GoTo")
print("Where is line 2?") #out side
gotoFunc() #out side
print("I'm up here") #out side

def unknowScope():
    print("Line one")
    def gotoFunc():
        print("From within the GoTo")
    print("Where is line 2?")
    gotoFunc()
    print("I'm up here")
unknowScope()

#========================================================================================#
# LAB 4
def greet_student(name):
    print(f"Welcome {name}")
greet_student("khdijah and Sara")

#========================================================================================#
# LAB 5
def show_booking(destination, nights):
    print(f"You're traveling to {destination}, and stay for {nights} nights")
# show_booking("Jeddah", 3)
# show_booking("Doha", 5)
#def show_booking(destination = "Riyadh", nights = 1):
    print(f"You're traveling to {destination}, and stay for {nights} nights")
# show_booking("Jeddah", 3)
# show_booking("Doha", 5)
# show_booking("D", False)

#def show_booking(destination = "Riyadh", nights = "1"): 
    #if nights.isdigit():
        #nn = int(nights)
    #print(f"You're traveling to {destination}, and stay for {nn} nights")
#show_booking() #You're traveling to Riyadh, and stay for 1 nights
# show_booking("Jeddah", "3")
# show_booking("Doha", "5")

#========================================================================================#
# LAB 6
def getVAT(total, rate = 0.15):
    """This Function will get the total with VAT added to it, and return the sum"""
    not_subtotal = total + (total * rate)
    return not_subtotal
print(getVAT(154))
print(getVAT(154, 0.05))
print(getVAT.__doc__)
help(getVAT)