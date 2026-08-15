#generator Expression #يحسب القيمه لما نطلبها
numbers = range(1_000_000)
total = sum(
    number **2
    for number in numbers
)
print(total)
numbers = range(1,11)
sum = total( 
    number **3 #3
    for number in numbers #1
    if number %2 !=0 #2
)
print(total)
#shallow copy بنسخ وبتتعدل القائمه الداخليه والخارجيه
# لو عدلت على الداخليه بتتعدل الخارجيه والعكس لا 
original =["python","git"]
clone = original.copy()
clone.append("django") #دخلنا للقاءمه الخارجيه
print(original)
print(clone)
print(original is clone) # false
#######################################
original =[";adi","git"]
clone=original.copy()
clone.append("danjo")

original =[["sara",90],["omar",85]]
clone = original.copy() #تنسخ القائمه الخارجيه فقط
clone[0][1]=95 # دخلنا  للقائمه الداخليه
print(original)
print(clone)
print(original[0] is clone[0]) #True


################################################################################################
#ديب كوبي ا اقدر انسخ   بدون ماتتغير القائمه الخارجيه
from copy import deepcopy
original =[["sara",90],["omar",85]]
clone = deepcopy(original)#تنسخ الخارجيه والداخليه
clone[0][1] = 95
print(original)# مارح تتغير لانها عطتنا لست مستقله
print(clone)
print(original[0] is clone[0]) # False
####################################################################################################
#opertion cost
# set = 0(1)
#list =0(n)
names = ["sara","omar","lana"]
# searches items one by one o(on)بيمر عليهم كلهم
print("lana" in names)
name_set = set(names) # تحويل اللست الى سيت
print("lina"in name_set)
print("-" *30)
######################################################################################
