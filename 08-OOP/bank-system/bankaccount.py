class BankAccount:
    bank_name = "Aana Bank"
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def display_balance(self):
        print(f"{self.name}: {self.balance}")

    @classmethod
    def change_bank_bame(cls, new_bank_name):
        cls.bank_name = new_bank_name
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

account1 = BankAccount("Aanaa", 6000)
account2 = BankAccount("Chala", 500)

account2.deposit(6000)
account2.display_balance()
account1.display_balance()

print(BankAccount.is_valid_amount(500))
print(BankAccount.bank_name)

BankAccount.change_bank_bame("Chala Bank")
print(BankAccount.bank_name)
