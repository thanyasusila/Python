class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited amount:", amount)
        print("Current balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn amount:", amount)
            print("Current balance:", self.balance)
        else:
            print("Insufficient balance")

account = BankAccount()

account.deposit(5000)

account.withdraw(2000)
