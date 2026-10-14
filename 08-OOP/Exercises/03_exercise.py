print("================The 1st Exercise=========================================")

class Phone :
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

phone1 = Phone("Samsung S24", "100k ETB")
phone2 = Phone("Iphone 17", "280k ETB")

print(phone1.brand, phone1.price)
print(phone2.brand, phone2.price)


print("====================The 2nd Exercise=====================================")


class Students :
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Students("Aanaa", 21)
student2 = Students("Chala", 22)

student2 = Students("Chala", 23)

print(student1.name, student1.age)
print(student2.name, student2.age)

print("===================The 3rd Exercise======================================")

class BankAccount:
    def __init__(self,owner, balance):
        self.owner = owner
        self.balance = balance

account1 = BankAccount("Aanaa", 6000)
account2 = BankAccount("Chala", 6000)

print(account1.owner, account1.balance)
print(account2.owner, account2.balance)

print("===================The 4rth Exersice ======================================")

class Student :
    university = "Haramaya University" # Class Attributes

    def __init__(self, name):
        self.name = name   # Instance Attributes

student3 = Student("Aana")
student4 = Student("Chala")

print(student3.name, student3.university)
print(student4.name, student4.university)


print("===================The 5th Exersice ======================================")

class Student:
    university = "Haramya University"
    def __init__(self, name):
        self.name=name
    @classmethod
    def change_uniersity(cls, new_name):
        cls.university = new_name

student5 = Student("Ana")
student6 = Student("cala")

Student.change_uniersity("AU")

print(student6.university)
print(student5.university)

print("===================The 6th Exersice ======================================")

class Student :
    def __init__(self, name, score):
        self.name = name
        self.score = score
    @staticmethod
    def is_passing(score):
        return score >= 50
student7 = Student("Anex", 80)
student8 = Student("chalex", 70)

print(Student.is_passing(student7.score))
print(Student.is_passing(student8.score))

