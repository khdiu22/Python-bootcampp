
#lap1
#الطريقه العاديه
numbers = [1,2,3,4,5]
sqaured_number =[]
for number in numbers:
    sqaured_number.append(number **2)
    print(sqaured_number) 
    
# List Comprehensionn
numbers = [1,2,3,4,5]

comp_numbers =[number **2 for number in numbers]
print(comp_numbers)
#########################################################################################################
#lap2
prices =[10,25,40]
prices_with_vat = [
    round(price *1.15,2)
    for price in prices
]
print(prices_with_vat)
########################################################################################################################
#lap3
names  = ["SaRa","ArEej","Mashael","nasser"]
lower  = [name.lower()for name in names]
upper  = [name.upper()for name in names]
titled = [name.title()for name in names]
print(lower,upper,titled)
###########################################################################################################################
#lap4
c_temp =[20,33,15,1]
f_temp =[
    (temp *1.8+32)
    for temp in c_temp
   if temp >0
]
print(f_temp)
##########################################################################################################################3
#lap5
nested_list =[[1,2],[3,4],[5,6]]
flattened_list = []
for row in nested_list:
    for column in row:
        flattened_list.append(column)
print(flattened_list)


comp_flattened_list =[column
for row in nested_list for column in row ]                      
print(comp_flattened_list)

################################################################################################################3
#lap6
scores =[45,55,65,75,86,95]
passing_score =[
    "pass" if score >=60 else "Failed"
    for score in scores
]
print(passing_score)
#######################################################################################################
#lap7
skills = ["PYTHON","GIT,","python","javascript",""]
skills_set = {
    skill.lower()
    for skill in skills
}
print(skills_set)
####################################################################################################################
#lap8

list_name =["sara","khdijah","nouf","Dala"]
counted_chars =[
    {"name":name,"count":len(name)} for name in list_name
]
print(counted_chars)
##########################################################################################################################3
#lap9
new_name =["mada","Khdijah","Yamam","Mashael"]
upp =(
    name.upper()
    for name in new_name
)
#print(list(upp))#
print(next(upp)) #print+remove
print(next(upp))
print("-"*5)
for x in upp:
    print(x)