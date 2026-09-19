class BankAccount:
    def __init__(self,account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):        
        if amount > 0:
            self.__balance += amount
            print(f"Dear {self.owner} you deposited {amount}, Your current balance is {self.__balance} .")
        else: 
            print("Please Enter valid Number")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance :
            self.__balance -= amount
            print(f"Dear {self.owner} you withdraw {amount}, your current balance is {self.__balance}")
        else:
            print("Insufficient balance or Invalid amount")

    def transfer(self, amount, reciept_account):
        if 0 < amount <= self.__balance :
            self.__balance -= amount
            reciept_account.deposit(amount)
            print(f"Dear {self.owner} you have transfered {amount} to {reciept_account.owner}")
    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = amount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance=0, interest_rate=0.05):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
account1 = SavingsAccount(10111 , "Aanaa", 6000, 0.05)

print(account1.balance)
account1.add_interest()
print(account1.balance)

withdraw_amount = 500
account1.withdraw(withdraw_amount)
account2 = BankAccount(10112 , "Obsa", 1000)
account1.transfer(500, account2)
account3 = BankAccount(10113 , "Sarah", 0)

account3.balance = 2000


print(account1.balance)
print(account2.balance)
print(account1.owner)
print(account3.balance)
