#class Student:
#    pass
#print(Student)
#print(type(Student))
#Calling a Class Creates an Obeject
#class Student:
    #pass
#student_one = Student() 
#student_tow = Student()
#print(student_one)
#print( student_one is student_tow) #false


#class Students:
#    def __init__(self,name,score):
#        self.name = name
#        self.score = score

#Students = Students("sara",92)
#print(Students.name)
#print(Students.score)
########################################################################
# self Refers to the Current Object
#class Student:
 #   def __init__(self,name):
  #      self.name = name
        
   # def introduce(self):
    # print(f" i am {self.name}")
#student = Student("Omar")
#student.introduce()

########################################################################
#class Student:
 #   def __init__(self,name,score):
  #       self.name = name
   #      self.score = score
#sara = Student("sara",92) #__init__(self, "sara", 92)
#omar = Student("omar",81)

#sara.score =95
         
#print(sara.score)
#print(omar.score)
#print(isinstance(omar, Student))
###############################################################################
# قيتر
#سيتر
#instance Methods Define object behavior
#class Student:
 #def __init__(self,name,score):
 #    self.name = name #  الاوبجكت الي استدعى الميثود
  #    self.score = score
        
 #def display_result(self):# السيلف تشير الى الاوبجكت الحالي 
 #    print (self.name ,self.score) 
     
#student = Student("Lina",88) #انشئنا اوبجكت اسمه Student
#student.display_result() #استدعاء الميثود عن طريق الاوبجكت
###########################################################################################
#class Attributes Are Shared Defaults
#class Student:
#    academy = "Tuwaiq Academy" #Class Attribute
 #   def __init__(self,name):
#        self.name = name #Instance Attribute
#sara = Student("sara")
#print(Student.academy)
#print(sara.academy) #ليه طبع لي اكاديمي لان سوينا لوكباك اب راح يدور بساره نفسها اذا مالقى يدور بالكلاس ويطبعها

########################################################################
#Methods Can Return Calculated Values
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
rectangle = Rectangle(5,3)
print(rectangle.area())
#####################################################################################

#Methods can Protect Valid state
#class BankAccount:
#    def __init__(self, balance=0):
#        self.balance =balance
#    def withdrae(self, amount):
#      if amount <= 0 or amount > self.balance:
#            return False
#      self.balance -= amount
#      return True
#account =BankAccount(500)
#print(account.withdrae(200))
#print(account.balance)
#####################################################################################
#Methods can change object state
#class Counter:
  #def __init__(self):
      #self.value =0
  #def increment(self):
     #self.value += 1
     
#counter = Counter()
#counter.increment()#1
#counter.increment()#2
#print((counter.value))#2
###########################################################################################
# __str__ gives an object a Readable Description
#class Student:
    #def __init__(self,name,score):
        #self.name = name
        #self.score = score
    #def __str__(self):#يحدد كيف يظهـ Object عند طباعته
     #return f"{self.name}: {self.score}"
#student = Student("sara",95)
#print(student)
#############################################################################################

#each instance Keeps Independent Sate
#class Counter:
  #def __init__(self):
      #self.value =0
  #def increment(self):
     #self.value += 1
#first =Counter()
#second = Counter()
#first.increment()
#print(first.value) #1
#print(second.value) #0
#############################################################################################33

#Attribute Access is Public by Default
#class Student:
    #def __init__(self,name,score):
        #self.name =name
        #self._score =score #يفضل لا تتعاملين معها مباشرة من خارج  Class
#student = Student("sara",95)
#print(student.name) 
#print(student._score) #بتنطبع

###########################################################################
#type and is instance identify object Types
#class Student:
    #pass
#student =  Student()
#print(type(student))
#print(type(student) is Student)
#print(isinstance(student, Student)) #هل هو Object من Student أو من Class يرث منه؟
#################################################################################
#A Small Class Keeps Data and Behavior Together
class Student:
    def __init__(self,name,scores):
        self.name = name
        self.scores = scores
    def average(self):
        return sum(self.scores) / len(self.scores)
    def add_score(self,score):
        if 0 <= score <= 100:
         self.scores.append(score)
student =Student("sara",[80,90])
student.add_score(100) # [80, 90, 100]
print(student.name, student.average()) #90.0

##########################################################################################     