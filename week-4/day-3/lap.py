
#class Dog:
 #   _legs = 4

#    def __init__(self, name):
 #       self.name = name

  #  def getLegs(self):
   #     return Dog._legs

    #def setLegs(self, number):
    #   self._legs = number


#myDog = Dog("Slugi")
#myDog.setLegs(3)
#print(myDog.getLegs())
#print(myDog._legs)

# Lap 1
#class Ticket:
 #   def __init__(self , name , status = "Open"):
  #      self.name = name
   #     self.status = status
#
 #   def newstatus(self , status):
  #      self.status = status

# myTicket = Ticket("Unable to open email" , "Closed")
#myTicket1 = Ticket("1000" , "In-Progress")
#myTicket2 = Ticket("1001" , "Pending")

#print(myTicket1.status)
#print(f"Ticket ID : {myTicket1.name} is {myTicket2.status}")
# lap 2
#class Greeter:
    #def __init__(self, message):
        #self.message = message

   # def greet(self, user):
    #    self.user = user
     #   return f"Hello {user}, {self.message}"


#mygreet = Greeter("Welcome to Tuwaiq")
#mymsg = mygreet.greet("Salem")
#print(mymsg)
#lap3
#class Welcome:
#    def __init__(self,name):
#        self.name = name
#    def welcome(self):
#        print(f"welcome {self.name}")

#students = [
#    Welcome("sara"),
#    Welcome("khdijah"),
#    Welcome("dala"),
#    Welcome("omar")
#]
#students[1].welcome()
#for student in students:
#    student.welcome()
#Lap 4

from pathlib import Path
path = Path("home") / "students" / "students.txt" #  الباث يشير الى الملف نفسه وليس مجلد
path.parent.mkdir(parents=True, exist_ok=True) #   انشئ لي مجلد اسمه ستيودنت دوت تكست هنا  انشئنا مجلد عن طريق المسار كامل
print(path.is_dir())
print(path.suffix)
print(path.is_file())
path.write_text("welcome to class", encoding="utf-8")


#Lap5
# class Student:
#     # __enrolled = True # لو _ وحده عادي يشتغل لو ثنتين لا 
#     def __init__(self, name):
#         self.name = name
#         self.score = []
#     def add_score(self, score):
#         if score < 0 or score > 100:
#             raise ValueError("Score must be between 0 and 100")
#         self.score.append(score)
#         #Setter
#     # @enrolled.setter
#     def setEnorllment(self, status):# لازم معها get
#         self.__enrolled = status
#         #Getter
#     # @enrold.seter
#     def getEnrollment(self):
#         return self.__enrolled
#     @property# استدعيها كنها فاريبل
#     def average(self):
#         if not self.score:
#             return 0
#         else:
#             return sum(self.score) / len(self.score)
# student = Student("khdijah")
# student.add_score(80)
# student.add_score(90)
# student.add_score(100)
# print(student.average) # بدون () اقدر استدعيها لاننا استخدمنا @property ت عامل مع هذه الدالة كأنها خاصية / attribute.
# print(student._Student__enrolled)# نتحايل عليه ب اسم الكلاس
# student.setEnorllment(False)
# student.enrolled =True
# print(student.getEnrollment())
# print(student.score)
# # صاير متغير  كاني اطلب فاريبلر بدون اقواس
#lab5
class Student:
    def __init__(self, name):
        self.name = name
        self.score = [] 
        self.__enrolled = False
    def add_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        self.score.append(score)

    @property
    def enrolled(self):
        return self.__enrolled

    # Setter
    @enrolled.setter
    def enrolled(self, status):
        self.__enrolled = status
    @property
    def average(self):
        if not self.score:
            return 0
        return sum(self.score) / len(self.score)
student = Student("khdijah")
student.add_score(80)
student.add_score(90)
student.add_score(100)
print(student.average)
student.enrolled = True
print(student.enrolled)
print(student.score)


#lap6
class Food:
    def __init__(self, name):
        self.name = name
    def showName(self):
        return self.name
class Fruites(Food):
    def __init__(self, name,cal):
        super().__init__(name)
        self.cal = cal
    @staticmethod
    def stripName(newNmame):
        return newNmame.strip()
    

myFruite = Fruites("Apple", 500)
print(myFruite.showName())
print(myFruite.stripName("  Fa  "))