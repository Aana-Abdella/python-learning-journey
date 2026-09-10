class Student:
    def __init__(self, name, age, grade, mark ):
        self.name = name
        self.age = age
        self.grade = grade
        self.mark = mark

    def get_introduce(self):
        return f"My name is {self.name}, I am {self.age} years old, and This is my {self.grade}th years in campus ."
    def study(self, subject):
        return f"{self.name} is studying {subject}."
    def calculate_average(self):
        total = 0
        for a in self.mark :
            total += a
        return total / len(self.mark) 

student1 = Student("Aanaa", 23, 4, [50,60,70 ])
print(student1.get_introduce())
print(student1.study("Software Engineering"))
print(student1.calculate_average())


