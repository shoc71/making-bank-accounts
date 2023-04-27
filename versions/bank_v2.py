import random

class Program:

    def __init__(self):
        self.running = True
        self.random_card_numbers = []

    def do_input(self):
        print("Deposit | Withdraw | Transfer")
        self.user_input = input("What service would you like to perform : ")
        if self.user_input == "quit":
            self.running = False

    def do_random(self, *args):
        self.nums = random.randint(1000,9999)
        self.random_card_numbers.append(f"XXXX_XXXX_XXXX_{self.nums}")
        print(self.random_card_numbers)

    def update(self):

        pass

    def run(self):
        while self.running:
            self.do_input()
            self.do_random()

program = Program()


if __name__ == "__main__":
    program.run()
