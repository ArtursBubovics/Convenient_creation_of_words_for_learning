import re

def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Ошибка: Ввод не может быть пустым. Пожалуйста, попробуйте снова.")
        else:
            return user_input

def get_non_empty_and_symbol_input(prompt, pattern=None):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print('\n---------------------------------------------')
            print("Ошибка: Ввод не может быть пустым. Пожалуйста, попробуйте снова.")
            print('---------------------------------------------\n')
        elif pattern and not re.match(pattern, user_input):
            print('\n---------------------------------------------')
            print(f"Ошибка: Ввод содержит недопустимые символы. Пожалуйста, попробуйте снова.")
            print('---------------------------------------------\n')
        else:
            return user_input
        
def get_valid_number(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print('\n---------------------------------------------')
            print("Ошибка: Ввод не может быть пустым. Пожалуйста, попробуйте снова.")
            print('---------------------------------------------\n')
        elif not user_input.isdigit():
            print('\n---------------------------------------------')
            print("Ошибка: Ввод должен быть числом. Пожалуйста, попробуйте снова.")
            print('---------------------------------------------\n')
        else:
            return int(user_input)
        
def get_valid_choice(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print('\n---------------------------------------------')
            print("Ошибка: Ввод не может быть пустым. Пожалуйста, попробуйте снова.")
            print('---------------------------------------------\n')
        elif not re.match(r'^[+\-/]$', user_input):
            print('\n---------------------------------------------')
            print("Ошибка: Ввод должен быть одним из символов '+', '-', '/'. Пожалуйста, попробуйте снова.")
            print('---------------------------------------------\n')
        else:
            return user_input