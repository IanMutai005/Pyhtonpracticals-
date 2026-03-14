class Students:
    def __init__(self, name , grade):
        self.name = name 
        self.grade = grade   # 0-
        
    def get_grade(self):
        return self.grade





class Course :
    def __init__(self , name , max_students ) :
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, student) :
          if len(self.students) <self.max_students :
                self.students.append(student)
                return True
          return False

    def max_grade(self):
            max_score = max(students.grade for students in self.students)
            return max_score

    def average_grade(self):
            value = 0
            for student in self.students :
                  value += student.get_grade()
            return value / len(self.students)

    def lowest_grade(self):
            min_score = min(students.grade for students in self.students)
            return min_score
    



    
s1 = Students("Ian Mutai",90)
s2 = Students("Debby Monda",89)
s3 = Students ("Kongeso Bosco",85)
s4 = Students ("Mark Odhiambo", 80)
s5 = Students ("Katile Kitava",95)


Engineering = Course ("Engineering", 7)
Engineering.add_students(s1)
Engineering.add_students(s2)
Engineering.add_students(s3)
Engineering.add_students(s4)
Engineering.add_students(s5)

print(Engineering.average_grade())
print(Engineering.lowest_grade())
print(Engineering.max_grade())