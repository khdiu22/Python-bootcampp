#comprehension طريقه مختصره عشان تسوي لي  الداتا ستركتر 

numbers =[1,2,3,4,5]

squares = [
    number ** 2 #Expression
    for number in numbers 
    if number % 2 == 1 #كلوز print odd number
]
print(squares) 
######################################################################################################################
# لما اشوف = اكسبرشن == كلوز
prices =[10,25,40]
prices_with_vat =[
    round(price * 1.15,2) #Expression ,round  تعطينا تقريب و2 رقمين بعد الفاصله
    for price in prices
]
print(prices_with_vat)
######################################################################################################################

#A filter keeps only items that match a condition
scores =[42,67,91,58,75]

passing_scores = [
    score 
    for score in scores
    if score >= 60 
]
print(passing_scores)
#[ EXPRESSION  for LOOP  if CONDITION filtring ]

######################################################################################################################
raw_names =[" sara ","","omar","lina"]

clean_names = [
    name.strip().title() 
    
    for name in raw_names
    
    if name.strip() # True 
]
#filtring and transformation cane work together

print(clean_names)
######################################################################################################################
numbers=[1,2,"c"]
letters = ["A" ,"B"]
#matrxc
paris =[
    (number, letter)# ملتي اكسبرسن
    for number in numbers #raw
    for letter in letters # raw
]
print(paris)
######################
#numbers=[1,2,3]
#letters = ["A" ,"B"]
#paris =[
#    (number, letter)
#    for number in numbers
#    for letter in letters
#]
#print(paris)

######################################################################################################################
#conditional Expression produces one of two values
scores = [42,67,91]
lables =[
    "pass" if score >= 60 else "retry"  #يحدد وش القيمة اللي بتنحط في القائمه اكسبرشن 
    for score in scores
]
print(lables)
######################################################################################################################
#مهم
emils = [
    "SARA@EXAMLE.COM",
    "omar@example.com",
    "lina@school.sa"
]
domains = {
    email.split("@")[1].lower() #قسم الإيميل عند @:
    for email in emils
}
print(domains)
######################################################################################################################
#write key:value before the for numbers = range(1,6)
#squares ={
#    number: number**2     
#    for number in numbers
#}
#print(squares)
####################################################################################################
# جنريتر اسرع من اللست