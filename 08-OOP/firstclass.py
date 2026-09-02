class Myclass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
person1 = Myclass("Aanaa")
print(person1.greet())

class Student:
    def __init__(self, student_id, name, age, department, maths_score, python_score, java_score, english_score, skills):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.department = department
        self.maths_score = maths_score
        self.python_score = python_score
        self.java_score = java_score
        self.english_score = english_score
        self.skills = skills

    def is_eligible(self):
        return 18 <= self.age <= 25

    def calculate_total(self):
        return self.maths_score + self.python_score + self.java_score + self.english_score

    def calculate_average(self):
        return self.calculate_total() / 4

    def performance(self):
        average = self.calculate_average()
        if average >= 90:
            return "Performance Excellent"
        elif average >= 80:
            return "Performance Very Good"
        elif average >= 70:
            return "Performance Good"
        elif average >= 60:
            return "Performance Pass"
        else:
            return "Performance Failed"

    def has_skill(self, skill):
        return skill in self.skills


class Mclass:
        x = 10

p1 = Mclass()
print(p1.x)

p2 = Mclass()
del p2

get(p2.x)


class Person:
    pass