class BankAccount:
    def __init__(self, owner, balance ) :
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount <= self.deposit :
            self.balance -= amount
        else:
            print("Insufficient balance")

account = BankAccount("Aanaa", 5000)
account.deposit(1000)
print(f"Dear {account.owner} your balnce is {account.balance} Thank You ")