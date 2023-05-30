class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

def create_account():
    account_number = input("Enter account number: ")
    balance = float(input("Enter initial balance: "))
    return Account(account_number, balance)

def deposit(account, amount):
    account.balance += amount
    print(f"Deposited {amount}. New balance: {account.balance}")

def withdraw(account, amount):
    if account.balance >= amount:
        account.balance -= amount
        print(f"Withdrew {amount}. New balance: {account.balance}")
    else:
        print("Insufficient balance")

def display_balance(account):
    print(f"Account number: {account.account_number}")
    print(f"Balance: {account.balance}")

def save_accounts(accounts):
    with open("accounts.txt", "w") as file:
        for account in accounts:
            file.write(f"{account.account_number},{account.balance}\n")

def load_accounts():
    accounts = []
    try:
        with open("accounts.txt", "r") as file:
            for line in file:
                account_number, balance = line.strip().split(",")
                account = Account(account_number, float(balance))
                accounts.append(account)
    except FileNotFoundError:
        pass
    return accounts

def transfer(accounts):
    sender_number = input("Enter sender's account number: ")
    receiver_number = input("Enter receiver's account number: ")
    amount = float(input("Enter amount to transfer: "))

    sender = None
    receiver = None

    for account in accounts:
        if account.account_number == sender_number:
            sender = account
        elif account.account_number == receiver_number:
            receiver = account

    if sender and receiver:
        if sender.balance >= amount:
            sender.balance -= amount
            receiver.balance += amount
            print(f"Transfer of {amount} from {sender_number} to {receiver_number} was successful.")
        else:
            print("Insufficient balance in the sender's account.")
    else:
        print("One or both account numbers are incorrect.")

def main():
    accounts = load_accounts()

    while True:
        print("\n-- Banking Menu --")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Balance")
        print("5. Transfer")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            account = create_account()
            accounts.append(account)
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            for account in accounts:
                if account.account_number == account_number:
                    deposit(account, amount)
                    break
            else:
                print("Account not found.")
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            for account in accounts:
                if account.account_number == account_number:
                    withdraw(account, amount)
                    break
            else:
                print("Account not found.")
        elif choice == "4":
            account_number = input("Enter account number: ")
            for account in accounts:
                if account.account_number == account_number:
                    display_balance(account)
                    break
            else:
                print("Account not found.")
        elif choice == "5":
            transfer(accounts)
        elif choice == "6":
            save_accounts(accounts)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()