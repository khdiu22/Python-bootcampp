# ليش الدكشنري لازم تكون امبيوتبل عشان هي المرجع الرفرنس
# ومو شرط تكون سترنق
# is_active ,result =True,None 
#اقدر اغير قيمه نون الى فولس ب استخدام الاف 
#isinstance() #تعلمني اذا التايب يساوي العنصر ترو اور فولس
#    الانبت لازم اسوي اول شي كاستنق بعدين فالديشن مثل از دجت از الفا از دسمل
#كل شي اوت بوت سترينق
#  الوايل كوندشن والفور لها كاونتر
# * catch all
#لو مثلا ابي اطبع اسامي يكون اول حرف a  وينتهي بb عن طريق الاف وفور 
# اشياء مقدر اتحكم فيها في النستد ماهي

number =[1,2,3,4] # الطريقه العاديه
num =[]
for numbers in number:
    num.append(numbers * 2)
    print(num)
#طريقه ال كومبارشن
number =[1,2,3,4]
num =[numbers*2 for numbers in number]
print(num)
#[Exception for item in iterable]
#[numbers*2 for numbers in number]
#x*2=    وش ابي اسوي بالعنصر
#for  المتغير الموقت 
#in numbers   من اي كولكشن اخذ العناصر
number=[1,2,3]
num_new=[numbers*2 for numbers in number]
print(num_new)

