
# التعامل مع مسارات الملفات
# Path objects Build Locations Portably
from pathlib import Path # Path هو Class يساعدك تتعاملين مع مسارات الملفات والمجلدات بطريقة أسهل.
data_file = Path ("data") / "student.txt" #يعني أنشأنا Path يشير إلى مجلد اسمه:
print(data_file) #يطبع المسار:
print(data_file.name)
print(data_file.suffix) #تعطيك امتداد الملف:

#Inspect Path befoe Using Them

data_dir = Path("data")
data_dir.mkdir(exist_ok=True) #إذا مجلد  الداتا غير موجود → ينشئه. واذا كان  موجود لاتعطيني ايرور
data_file = data_dir / "student.txt" #نشاء مسار الملف
print(data_dir.is_dir())
print(data_file.exists()) # true or false

# File Modes Decide Waht May Change
# "r" read an existing file
# "w" write and replace content # يقوم بمسح واستبدال أي محتوى قديم داخل الملف ببيانات جديده إذا لم يكن الملف موجودًا أصلاً، سيقوم بإنشائه تلقائيًا
# "a" append after existung content
# "x" create only when absent
# a= append  
# #cn-us  يدعم بس الانقليزي
with open("notes.txt", "a",encoding = "utf-8") as file: # يدعم اللغه العربيه utf-8 
    file.write("New note\n")
    
# with Closes the file
path = Path("notes.txt") 
with path.open("r", encoding="utf-8")as file:
    content = file.read()#  الريد من المتغير فايل
print(content)
print(file.closed) #True
#with Closes  # بيجي بالاختبارمهم


path = Path("notes.txt")
with path.open("r", encoding="utf-8")as file:
    
    text =file.read() # طريقه مختصره لقراه الملف
    same_text = path.read_text(encoding="utf-8") # ريد تكست تقرا الملف كامل  وتقفل الملف 
    print(text == same_text) # والفايل ريد
####################################################################
#path = Path("students.txt")
#with path.open("r", encoding="utf-8")as file:
#    for line in file: # # لان الملف يمر عليه سطر سطر
#        name= line.strip()
#        if name: # يتحقق مما إذا كان السطر يحتوي على نص بالفعل أم أنه سطر فارغ.
         #  print(name)
         
#write replacec Existing content
#كتابة نص جديد واستبدال المحتوى القديم في ملف باستخدام وضع الكتابة
path = Path("students.txt")
with path.open("w", encoding="utf-8")as file:
    count = file.write("sara\nAli\n")# مع النيو لاين صارت تسعه
    print(count)
    


path = Path("activity.log")
with path.open("a", encoding="utf-8")as file:
        file.write("student enrolled: sara\n")
        print("Active saved")
#  مااستعمل الدت رايد في اللوب استعمل جوين
names = ["sara","نوره","Ali"]
text = "\n".join(names) + "\n" # تدمج كولكشن سطر واحد
Path("student.txt").write_text( #تقوم بفتح الملف، كتابة النص كاملاً، وإغلاق الملف تلقائيًا في سطر واحد
text,
encoding="utf-8"
)
#cvs 
import csv
with open ("students.csv", "w",
          encoding="utf-8", newline="") as file:
          writer = csv.writer(file)
          writer.writerow(["name","course"])
          writer.writerow(["sara","python"])
          writer.writerow(["ali","Django"])
import json 
students = [
    {"name":"sara","score":92},
    {"name":"Ali","score":85},
]
with open("students.json", "w", encoding="utf-8")as file:
    json.dump(students, file, indent=2)
with open("students.json", "r", encoding="utf-8")as file:
    loaded = json.load(file)
print(loaded[0]["name"])
# لود يقرا
#دمب يسوي رايد
try:
 score = int(input("score:"))
except ValueError:
    print("enter a whole number")
    print(ValueError) 
print("Program continues")

from pathlib import Path
try:
    text = Path ("students1.txt").read_text(
        encoding="utf-8"
    )
except FileNotFoundError:
    print("student file not found")
except PermissionError:
    print("student file cannot be read")

path = Path("students.txt")
try:
     text = path.read_text(encoding="utf-8")
except FileNotFoundError:
     print("File not found")
else:
     print(text)
finally:
     print("Load attempt finished") # الفاينلي دايم تشتغل
     # اذا  تراي اشتغلت انا مااحتاج الاكسبت بس احتاج الايلس
     
def validate_score(score):
    if not 0 <= score <= 100:
        raise ValueError("score must be 0 to 100") # الريس  كانها اكسبت بس اتحكم فيها
    return score
try:
    score = validate_score(120)
except ValueError as error:
    print(error)
#custmore #استخدمها اذا بوقف الفلو
class StudentNotFoundError(Exception):
    pass


def find_student(name, students):
    for student in students:
        if student["name"] == name:
            return student
    raise StudentNotFoundError(name)


students = [{"name": "Sara"}]

try:
    print(find_student("Ali", students))
except StudentNotFoundError as error: # جابها من الكلاس
    print("Missing student:", error)