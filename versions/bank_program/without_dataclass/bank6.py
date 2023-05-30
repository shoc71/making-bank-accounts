import hashlib
import os
import sys
import pygame
from pygame.locals import *

# Constants
SECRET_KEY_FILE = "secret.key"
ACCOUNTS_FILE = "accounts.txt"

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Banking System")

# Fonts
font_large = pygame.font.Font(None, 48)
font_medium = pygame.font.Font(None, 32)
font_small = pygame.font.Font(None, 24)

# Account class
class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

# Load accounts from file
def load_accounts():
    accounts = []
    try:
        with open(ACCOUNTS_FILE, "r") as file:
            data = file.readlines()
            for line in data:
                account_number, hashed_balance = line.strip().split(",")
                account = Account(account_number, hashed_balance)
                accounts.append(account)
    except FileNotFoundError:
        pass
    return accounts

# Save accounts to file
def save_accounts():
    with open(ACCOUNTS_FILE, "w") as file:
        for account in accounts:
            file.write(f"{account.account_number},{account.balance}\n")

# Transfer money between accounts
def transfer(sender_number, receiver_number, amount):
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
            return True
    return False

# Hash balance using SHA256
def hash_balance(balance):
    hasher = hashlib.sha256()
    hasher.update(str(balance).encode())
    return hasher.hexdigest()

# GUI functions
def display_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))   

def create_account():
    account_number = input_box("Enter account number: ")
    balance = float(input_box("Enter initial balance: "))
    hashed_balance = hash_balance(balance)
    account = Account(account_number, hashed_balance)
    accounts.append(account)
    save_accounts()

def transfer_money():
    sender_number = input_box("Enter sender account number: ")
    receiver_number = input_box("Enter receiver account number: ")
    amount = float(input_box("Enter amount to transfer: "))
    success = transfer(sender_number, receiver_number, amount)
    if success:
        display_message("Transfer successful.", GREEN)
    else:
        display_message("Transfer failed.", RED)

def display_account_balance():
    account_number = input_box("Enter account number: ")
    for account in accounts:
        if account.account_number == account_number:
            display_message(f"Account Number: {account.account_number}\nBalance: ${account.balance}", BLACK)
            return
    display_message("Account not found.", RED)

def input_box(prompt):
    input_rect = pygame.Rect(100, 400, 600, 50)
    color_active = GRAY
    color_inactive = WHITE
    color = color_inactive
    active = False
    text = ""

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                save_accounts()
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if active:
                    if event.key == K_RETURN:
                        return text
                    elif event.key == K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(WHITE)
        display_text(prompt, font_medium, BLACK, 100, 375)
        pygame.draw.rect(screen, color, input_rect, 2)
        display_text(text, font_medium, BLACK, input_rect.x + 5, input_rect.y + 5)
        input_rect.w = max(200, len(text) * 15)

        pygame.display.update()

def display_message(message, color):
    pygame.draw.rect(screen, color, (100, 500, 600, 50))
    display_text(message, font_medium, WHITE, 100, 515)
    pygame.display.update()

def main():
    global accounts, create_account_button, transfer_button, display_balance_button

    # Load accounts from file
    accounts = load_accounts()

    # Main game loop
    while True:
        screen.fill(WHITE)

        display_text("Banking System", font_large, BLACK, 200, 50)

        # Create account button
        create_account_button = pygame.draw.rect(screen, GRAY, (100, 150, 200, 50))
        display_text("Create Account", font_medium, WHITE, 110, 160)

        # Transfer button
        transfer_button = pygame.draw.rect(screen, GRAY, (100, 220, 200, 50))
        display_text("Transfer", font_medium, WHITE, 150, 230)

        # Display balance button
        display_balance_button = pygame.draw.rect(screen, GRAY, (100, 290, 200, 50))
        display_text("Display Balance", font_medium, WHITE, 120, 300)

        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                save_accounts()
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if create_account_button.collidepoint(*mouse_pos):
                    create_account()
                elif transfer_button.collidepoint(*mouse_pos):
                    transfer_money()
                elif display_balance_button.collidepoint(*mouse_pos):
                    display_account_balance()

        pygame.display.update()

if __name__ == "__main__":
    main()
