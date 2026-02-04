# 2. Create a BankAccount class with private balance and methods to deposit and check balance.
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance
account = BankAccount(1000)
account.deposit(500)
print(f"Current Balance: {account.get_balance()}")
