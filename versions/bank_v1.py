class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit of", amount, "successful. New balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance. Withdrawal unsuccessful.")
        else:
            self.balance -= amount
            print("Withdrawal of", amount, "successful. New balance:", self.balance)

    def check_balance(self):
        print("Account balance:", self.balance)

# Example usage
account = BankAccount("John Doe", "123456789", 1000)
account.deposit(500)
account.check_balance()
account.withdraw(2000)
account.withdraw(800)
account.check_balance()
