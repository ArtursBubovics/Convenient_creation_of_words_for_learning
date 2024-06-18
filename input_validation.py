import re

def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Error: Input cannot be empty. Please try again.")
        else:
            return user_input

def get_non_empty_and_symbol_input(prompt, pattern=None):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print('\n---------------------------------------------')
            print("Error: Input cannot be empty. Please try again.")
            print('---------------------------------------------\n')
        elif pattern and not re.match(pattern, user_input):
            print('\n---------------------------------------------')
            print(f"Error: The input contains invalid characters. Please try again.")
            print('---------------------------------------------\n')
        else:
            return user_input
        
def get_valid_number(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print('\n---------------------------------------------')
            print("Error: Input cannot be empty. Please try again.")
            print('---------------------------------------------\n')
        elif not user_input.isdigit():
            print('\n---------------------------------------------')
            print("Error: Input must be a number. Please try again.")
            print('---------------------------------------------\n')
        else:
            return int(user_input)
        
def get_valid_choice(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print('\n---------------------------------------------')
            print("Error: Input cannot be empty. Please try again.")
            print('---------------------------------------------\n')
        elif not re.match(r'^[+\-/]$', user_input):
            print('\n---------------------------------------------')
            print("Error: The input must be one of the characters '+', '-', '/'. Please try again.")
            print('---------------------------------------------\n')
        else:
            return user_input