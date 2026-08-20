# Practice

class Student:
    def init(self , name ):
        self.name = name
        self.scores = [] 

    def add_score(self , score):
        if 0 <= score <= 100:
            self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) /len (self.scores)


class Course:
    def init(self):
        self.students = []

    def add_student(self , student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print("Name:", student.name)
            print("Scores:", student.scores)
            print("Average:", student.average())

s1 = Student("Sarah")
s1.add_score(90)
s1.add_score(89)

s2 = Student("Omar")
s2.add_score(88)
s2.add_score(90)

s3 = Student("Jojo")
s3.add_score(100)
course = Course()
course.add_student(s1)
course.add_student(s2)

course.display_students()