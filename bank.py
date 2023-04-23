# import pygame - fuk py gui bs, we using this for a banking screen and all that

bank1 = 0 

def user_input():
    pass

while True: #simply exist to make sure the user inputs only float/interger values
    try:
        user_input_here = round(float(input("enter money here : ")),2) #ignore this line
        break
    except:
        print("Enter numbers only")

bank1 = bank1 + user_input_here

print(f"This is your current bank balance : {bank1}")


class Bank:

    bank_balance = 0

    def __init__(self):
        pass

bank_accounts = []