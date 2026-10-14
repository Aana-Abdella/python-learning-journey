print("====================The 2nd Exercise=====================================")


class Calculator  :
    def add(self, a,b):
        return a + b

    def multiply(self, a, b):
        return a * b
calc = Calculator()
print( calc.add(4,6))
print( calc.multiply(4,7))


print("====================The 2nd Exercise=====================================")

class Student :
    university = "HU"
    def __init__(self, name):
        self.name = name

student1 = Student("Aanaa")
student2 = Student("Chala")

print(student1.name, Student.university)
print(student2.name, Student.university)

print("====================The 3rd Exercise=====================================")

class Student :
    university = "HU"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_university(cls, newname):
        cls.university = newname

    @staticmethod
    def is_adult(age):
        return age > 18

Student.change_university("Addis Abeba University")
student1 = Student("Aanaa", 20)
student2 = Student("Chala", 21)

print(student1.name, Student.university)
print(student2.name, Student.university)
print(student1.is_adult(20))
print(student2.is_adult(20))

print("====================The 4th Exercise=====================================")

class BankAccount:
    def __init__(self, owner , balance):
        self.owner = owner
        self.balance = balance

    @staticmethod
    def is_valid(amount):
        return amount > 0

    def deposit(self, amount):
            if BankAccount.is_valid(amount):
                self.balance += amount
                return True
            return False

    def display_balance(self):
        print(f"{self.owner}, {self.balance}")

account1 = BankAccount("Aana", 6000)
account2 = BankAccount("Chala", 500)

account1.deposit(600)

account1.display_balance()
account2.display_balance()
print(BankAccount.is_valid(500))   # True
print(BankAccount.is_valid(-100))  # False


