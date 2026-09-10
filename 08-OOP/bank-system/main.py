class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"

account1 = BankAccount("123456", "Alice", 1000)
account1.deposit(500)
account1.withdraw(200)
print(account1)

account2 = BankAccount("789012", "Bob")
account2.deposit(300)
account2.withdraw(100)
print(account2)

account3 = BankAccount("345678", "Charlie", 2000)
account3.deposit(1000)
account3.withdraw(500)
print(account3)