import hashlib
import os
import tkinter as tk
from tkinter import messagebox

# Constants
SECRET_KEY_FILE = "secret.key"
ACCOUNTS_FILE = "accounts.txt"

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

def create_account():
    account_number = account_number_entry.get()
    balance = float(balance_entry.get())
    account = Account(account_number, balance)
    accounts.append(account)
    messagebox.showinfo("Account Creation", "Account created successfully.")

def deposit():
    account_number = account_number_entry.get()
    amount = float(amount_entry.get())
    for account in accounts:
        if account.account_number == account_number:
            account.balance += amount
            messagebox.showinfo("Deposit", f"Deposited {amount}. New balance: {account.balance}")
            break
    else:
        messagebox.showerror("Error", "Account not found.")

def withdraw():
    account_number = account_number_entry.get()
    amount = float(amount_entry.get())
    for account in accounts:
        if account.account_number == account_number:
            if account.balance >= amount:
                account.balance -= amount
                messagebox.showinfo("Withdrawal", f"Withdrew {amount}. New balance: {account.balance}")
            else:
                messagebox.showerror("Error", "Insufficient balance.")
            break
    else:
        messagebox.showerror("Error", "Account not found.")

def display_balance():
    account_number = account_number_entry.get()
    for account in accounts:
        if account.account_number == account_number:
            messagebox.showinfo("Balance", f"Account number: {account.account_number}\nBalance: {account.balance}")
            break
    else:
        messagebox.showerror("Error", "Account not found.")

def save_accounts():
    data = ""
    for account in accounts:
        data += f"{account.account_number},{account.balance}\n"

    salted_data = add_salt(data)
    hash_value = hashlib.sha256(salted_data.encode()).hexdigest()

    with open(ACCOUNTS_FILE, "w") as file:
        file.write(f"{salted_data}{hash_value}")

def load_accounts():
    accounts = []
    try:
        with open(ACCOUNTS_FILE, "r") as file:
            data = file.read()
            hash_value = data[-64:]
            data = data[:-64]

            if verify_hash(data, hash_value):
                lines = data.split("\n")
                for line in lines:
                    account_number, balance = line.strip().split(",")
                    account = Account(account_number, float(balance))
                    accounts.append(account)
            else:
                messagebox.showerror("Error", "Data integrity compromised. Cannot load accounts.")
    except FileNotFoundError:
        pass
    return accounts

def add_salt(data):
    # Generate a random salt
    salt = os.urandom(16).hex()
    return salt + data

def verify_hash(data, hash_value):
    # Retrieve the salt from the data
    salt = data[:32]
    data = data[32:]
    salted_data = salt + data

    # Generate the hash of the salted data
    calculated_hash = hashlib.sha256(salted_data.encode()).hexdigest()

    return hash_value == calculated_hash

def transfer():
    sender_number = sender_entry.get()
    receiver_number = receiver_entry.get()
    amount = float(transfer_amount_entry.get())

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
            messagebox.showinfo("Transfer", f"Transfer of {amount} from {sender_number} to {receiver_number} was successful.")
        else:
            messagebox.showerror("Error", "Insufficient balance in the sender's account.")
    else:
        messagebox.showerror("Error", "One or both account numbers are incorrect.")

def main():
    global accounts

    accounts = load_accounts()

    window = tk.Tk()
    window.title("Banking System")

    # Create account
    create_account_frame = tk.LabelFrame(window, text="Create Account")
    create_account_frame.pack(padx=10, pady=10)

    account_number_label = tk.Label(create_account_frame, text="Account Number:")
    account_number_label.grid(row=0, column=0)
    account_number_entry = tk.Entry(create_account_frame)
    account_number_entry.grid(row=0, column=1)

    balance_label = tk.Label(create_account_frame, text="Initial Balance:")
    balance_label.grid(row=1, column=0)
    balance_entry = tk.Entry(create_account_frame)
    balance_entry.grid(row=1, column=1)

    create_button = tk.Button(create_account_frame, text="Create", command=create_account)
    create_button.grid(row=2, columnspan=2, pady=5)

    # Deposit
    deposit_frame = tk.LabelFrame(window, text="Deposit")
    deposit_frame.pack(padx=10, pady=10)

    account_number_label = tk.Label(deposit_frame, text="Account Number:")
    account_number_label.grid(row=0, column=0)
    account_number_entry = tk.Entry(deposit_frame)
    account_number_entry.grid(row=0, column=1)

    amount_label = tk.Label(deposit_frame, text="Amount:")
    amount_label.grid(row=1, column=0)
    amount_entry = tk.Entry(deposit_frame)
    amount_entry.grid(row=1, column=1)

    deposit_button = tk.Button(deposit_frame, text="Deposit", command=deposit)
    deposit_button.grid(row=2, columnspan=2, pady=5)

    # Withdraw
    withdraw_frame = tk.LabelFrame(window, text="Withdraw")
    withdraw_frame.pack(padx=10, pady=10)

    account_number_label = tk.Label(withdraw_frame, text="Account Number:")
    account_number_label.grid(row=0, column=0)
    account_number_entry = tk.Entry(withdraw_frame)
    account_number_entry.grid(row=0, column=1)

    amount_label = tk.Label(withdraw_frame, text="Amount:")
    amount_label.grid(row=1, column=0)
    amount_entry = tk.Entry(withdraw_frame)
    amount_entry.grid(row=1, column=1)

    withdraw_button = tk.Button(withdraw_frame, text="Withdraw", command=withdraw)
    withdraw_button.grid(row=2, columnspan=2, pady=5)

    # Display Balance
    display_balance_frame = tk.LabelFrame(window, text="Display Balance")
    display_balance_frame.pack(padx=10, pady=10)

    account_number_label = tk.Label(display_balance_frame, text="Account Number:")
    account_number_label.grid(row=0, column=0)
    account_number_entry = tk.Entry(display_balance_frame)
    account_number_entry.grid(row=0, column=1)

    display_balance_button = tk.Button(display_balance_frame, text="Display Balance", command=display_balance)
    display_balance_button.grid(row=1, columnspan=2, pady=5)

    # Transfer
    transfer_frame = tk.LabelFrame(window, text="Transfer")
    transfer_frame.pack(padx=10, pady=10)

    sender_label = tk.Label(transfer_frame, text="Sender Account Number:")
    sender_label.grid(row=0, column=0)
    sender_entry = tk.Entry(transfer_frame)
    sender_entry.grid(row=0, column=1)

    receiver_label = tk.Label(transfer_frame, text="Receiver Account Number:")
    receiver_label.grid(row=1, column=0)
    receiver_entry = tk.Entry(transfer_frame)
    receiver_entry.grid(row=1, column=1)

    transfer_amount_label = tk.Label(transfer_frame, text="Transfer Amount:")
    transfer_amount_label.grid(row=2, column=0)
    transfer_amount_entry = tk.Entry(transfer_frame)
    transfer_amount_entry.grid(row=2, column=1)

    transfer_button = tk.Button(transfer_frame, text="Transfer", command=transfer)
    transfer_button.grid(row=3, columnspan=2, pady=5)

    window.mainloop()

    save_accounts()

if __name__ == "__main__":
    main()
