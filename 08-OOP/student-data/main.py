class Student:
    def __init__(self, name, age, grade, marks= None):
        self.name = name
        self.age = age
        self.grade = grade
        self.marks = []

        if marks:
            for mark in marks:
                self.add_mark(mark)
    def get_introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, and This is my {self.grade}th years in campus ."
    def study(self, subject):
        return f"{self.name} is studying {subject}."
    def add_mark(self, mark):
        if mark < 0 or mark > 100:
            print("Invalid mark. Please enter a value between 0 and 100.")
            return
        self.marks.append(mark)
    def calculate_average(self):
        if not self.marks:
            return 0
        total = 0
        for mark in self.marks :
            total += mark
        return total / len(self.marks) 
   

student1 = Student (
    "Aanaa", 
    23,
    4,
    [50,60,70 ]
)
print(student1.get_introduce())
print(student1.study("Software Engineering"))
print(student1.calculate_average())
student1.add_mark(80)
print(student1.calculate_average())


