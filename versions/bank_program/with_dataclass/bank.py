import random
from dataclasses import dataclass
#everything here will be entirely determined by user_input4e4ee




class Account:
    #making iniitals
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def creating_account(self):
        account_number = random.randint(1000,9999)
        balance = random.randint(0,99)
        return Account(account_number, balance)

    def deleting_account(self):
        pass
    
    #simple banking functions like deposit, withdrawal, transfer, checking_balance
    def deposit(self):
        pass

    def withdrawal(self):
        pass

    def transfer(self):
        pass

    def main(self):
        pass

# if __name__ == "__main__":
#     account.main()