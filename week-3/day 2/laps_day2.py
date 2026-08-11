# Lap 1
course = "Web Development Bootcamp"
duration = 12

def type(course): #مارح ترجع لي  التايب لاني عرفت الداله ب اسم تايب بترجع الي داخل الداله
    print("Opss!")
print(course)
print(duration)
print(type(course)) # opss!
                  #None # we dont have return 

print(globals())# print out of spaces fuction
print(locals()) #تطبع الي داخل الفنكشن


# Lap 2

builiding = "Tuwaiq Acadmy"
cohort_size = 20

print(f"Welcome to {builiding} , class limit is {cohort_size}")
print("Tuwaiq" in builiding)
print("cohort_size" in globals()) #هل موجود النص ام لا وليس قيمته
print(globals()["course"]) #موجود خارج  نيم سبيس الفنكشن؟
#shift +Alit +Down

# -----
# Lap 3
loction ="outer"
#def outter():
    #print(f"from outter{loction}") #نبحث اول شي في الاوتر
    #def inner():
        #print("from inner")
        #print(f"from{loction}") #عندما اينر تحتاج متغيرًا،  تبحث من الأقرب إلى الأبعد:
    #inner()
#outter()
def outter(): 
    loction =1
    print(f"from outter{loction}")
    def inner():
        nonlocal loction # متغير موجود في الدالة الخارجية وأريد تعديله من الدالة الداخلية.
        # لو احذفها بيطلع كانه متغير جديد داخل الانر لا قيمه له
        loction +=2
        print("from inner")
        print(f"from{loction}")
    inner()
outter()
#Lap5 
def printer():
    print("welcome")
def desk():
    printer
def room():
    desk()
def house():
    pass
# lap 6
language ="Python"
def show_lang(language):
    print(language)#Dart
show_lang("Dart") # يطبع الاقرب
print(language) #Python

#lap 7
rate = 0.15
def getTotal(amount):
    total = amount *rate+amount
    return total
print(f"{getTotal(1999.99):.2f}")
print(round(getTotal(199.99) ,2 )) # تقريب الاثنين عباره عن كم فاصله بعد النقطه
#اي شي بعد النقطتين هو القلوبل
# Lap 8

def inspect_order(item , qty):
    subtotal = 25 * qty
    print(locals()) # يصير دكشنري
    print(locals() ["subtotal"])

inspect_order("Pen" , 10)
##
name = input("Enter your name")
for leter in name:
    print(leter)