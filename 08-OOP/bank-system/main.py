class BankAccount:
    def __init__(self,account_number, account_owner, balance=0):
        self.account_number = account_number
        self.account_owner = account_owner
        self.__balance = balance

    def deposit(self, amount):        
        if amount > 0:
            self.__balance += amount
            print(f"Dear {self.account_owner} you deposited {amount}, Your current balance is {self.__balance} .")
        else: 
            print("Please Enter valid Number")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance :
            self.__balance -= amount
            print(f"Dear {self.account_owner} you withdraw {amount}, your current balance is {self.__balance}")
        else:
            print("Insufficient balance or Invalid amount")

    def transfer(self, amount, reciept_account):
        if 0 < amount <= self.__balance :
            self.__balance -= amount
            reciept_account.deposit(amount)
            print(f"Dear {self.account_owner} you have transfered {amount} to {reciept_account.account_owner}")
    def get_balance(self):
        return self.__balance

account1 = BankAccount(10111 , "Aanaa", 6000)
print(account1.get_balance())
withdraw_amount = 500
account1.withdraw(withdraw_amount)
account2 = BankAccount(10112 , "Obsa", 1000)
account1.transfer(500, account2)
print(account1.get_balance())
print(account2.get_balance())
