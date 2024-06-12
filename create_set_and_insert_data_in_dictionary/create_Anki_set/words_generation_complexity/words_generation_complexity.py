from enum import Enum


def words_generation_complexity_func():

    complexity_map = {
        1: 'A1',
        2: 'A2',
        3: 'B1',
        4: 'B2',
        5: 'C1',
        6: 'C2',
    }

    print("""
    1 - A1
    2 - A2
    3 - B1
    4 - B2
    5 - C1
    6 - C2\n""")

    while True:

        try:
            words_generation_complexity = int(input("Enter the number of words generation complexity: "))

            if 1 <= words_generation_complexity <= 6:
                print(f"\nYou have selected complexity level: \033[92m{complexity_map[words_generation_complexity]}\033[0m \n")
                return complexity_map[words_generation_complexity]
            else:
                print("Неверный ввод. Пожалуйста, выберите уровень сложности из предложенного списка. \n")
        except ValueError:
            print("Неверный ввод. Введите число от 1 до 6.\n")