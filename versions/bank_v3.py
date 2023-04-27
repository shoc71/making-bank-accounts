'''

create bank accounts
store vaules associated with those bank accounts
transfer money bewteen those bank accounts
censor numbers for the bank accounts

'''
from dataclasses import dataclass, field
import random


@dataclass(order=True)
class Profile():
    name : str = ""
    age : int = 0
    job : str = ""
    salary : float = 0
    paying_interval : float = 0

    def __post_init__(self): #fixing input errors before they happen, the location of this might change
        if type(self.name) is not str:
            raise TypeError("Field 'name' must be a string")
        self.age = int(self.age)
        if self.age < 0:
            raise ValueError("Field 'age' must be a positive value")
        if type(self.job) is not str:
            raise TypeError("Field 'job' must be a string")
        if self.salary < 0:
            raise ValueError("Field 'salary' must be a positive value")
        if self.paying_interval < 0:
            raise ValueError("Field 'paying_interval' must be a positive value")
        

@dataclass
class Bank_Account(Profile):
    card_number : str = ""
    card_password : str = ""
    account_vaule : float = 0
    number_of_transcation : int = 0

# @dataclass(order=True)
# class Random_Profile(Profile):
#     name : str = random.choice(["Joe Smith","Emark Dave","Esven Eleven","Shawn Braun","Ryan Bryan"])
#     age : int = random.randint(18,95)
#     job : str = random.choice(["doctor","lawyer","janitor","lawyer"])
#     salary : float = random.randint(0,1000)
#     paying_interval : float = random.choice([1,2,3,4,6,12])

# @dataclass
# class Random_Account(Random_Profile):
#     card_number : str = random.choice(["XXXX_1234","XXXX_1444"])
#     card_password : str = random.choice(["XXXX_1234","XXXX_1444"])
#     account_vaule : float = random.randint(0,1000)
#     number_of_transcation : int = random.randint(0,1000)

class Program:

    def __init__(self):
        self.new = Bank_Account("new-man",23,"doctor",100,12,"5544","pass123",123,2)
        self.random_troll = Bank_Account()
        self.user = Bank_Account()
        self.user_input_counter = 0
        self.paying_intervals_to_numbers = ["hourly","daily", "weekly", "biweekly", "monthly", "yearly"]

    def do_random(self):
        self.random_name = random.choice(["Joe Smith","Emark Dave","Esven Eleven","Shawn Braun","Ryan Bryan"])
        self.random_age = random.randint(18,95)
        self.random_job = random.choice(["doctor","lawyer","janitor","queen"])
        self.random_salary = random.randint(0,1000)
        self.random_paying_interval = random.choice([1,2,3,4,6,12])
        self.random_card_number = random.randint(1000,9999)
        self.random_card_number = f"XXXX_{self.random_card_number}"# this will change later down the line
        self.random_card_password = random.choice(["pass321","pass789"])
        self.random_account_vaule = random.randint(0,1000)
        self.random_number_of_transcation = random.randint(0,1000)

    def input_process(self):
        if self.user_input == "edit":
            self.user_input_editing = input("What would you like to edit? (type options if unsure): ")
            if self.user_input_editing == ("nothing" or "no" or "n" or "exit"):
                pass
            elif self.user_input_editing == (""):
                print("Nothing was input, type edit again to change what you wanted")
            elif self.user_input_editing == ("name" or "Bank account name"):
                self.user_input_edit_name = input("What's the new name? : ")
                self.user.name = self.user_input_edit_name
                while True: #checking for errors
                    try:
                        self.user.name = str(self.user.name)
                        break
                    except:
                        if type(self.user.name) is not str:
                            raise TypeError("Field 'name' must be a string")
            elif self.user_input_editing == ("age" or "bank account age"):
                self.user_input_edit_age = input("What's the new age? : ")
                self.user.age = self.user_input_edit_age
                while True:
                    try:
                        self.user.age = int(self.user.age)
                    except:
                        if self.user.age < 0:
                            raise ValueError("Field 'age' must be a positive value")


        pass

    def user_setup(self):
        self.user = Bank_Account(input("What is your name? : "), input("What is your age? : "), input("What is your job? : "),
                                 input("What is your salary? (only amount) : "), input("How often do you get paid? (only time) : "))
        

        while True:
            if self.user.paying_interval in self.paying_intervals_to_numbers:
                # everything is being converted into yearly amounts
                pass
        

    def do_user_input(self):
        self.user_input = input("tesing a loop, type 'quit' to exit : ")
        self.input_process()

    def update(self):

        if self.user_input_counter == 0:
            self.do_random()
            self.user = Bank_Account("default name", self.random_age, self.random_job, self.random_salary, 
                                        self.random_paying_interval, self.random_card_number, self.random_card_password,
                                        self.random_account_vaule, self.random_number_of_transcation)
        elif self.user_input == "random":
            self.do_random()
        else:
            pass
            
        self.random_troll = Bank_Account(self.random_name, self.random_age, self.random_job, self.random_salary, 
                                        self.random_paying_interval, self.random_card_number, self.random_card_password,
                                        self.random_account_vaule, self.random_number_of_transcation)
        
        print(f"bank account name - {self.random_troll.name} and {self.user.name}")

        self.user_input_counter += 1

    def run(self):
        self.do_user_input()
        while True:
            if self.user_input == "quit":
                break
            else:
                self.update()
                self.do_user_input()
            

program = Program()

if __name__ == "__main__":
    program.run()

print(program.new)
print(program.random_troll)
print(f"Sum of all bank accounts are : ${program.new.account_vaule + program.random_troll.account_vaule}")
