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
                print("Invalid entry. Please select a difficulty level from the list provided. \n")
        except ValueError:
            print("Invalid input. Enter a number from 1 to 6.\n")