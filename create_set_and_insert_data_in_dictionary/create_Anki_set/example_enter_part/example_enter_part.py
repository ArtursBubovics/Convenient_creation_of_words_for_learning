

from AI.example_generation.example_generation.example_generation import example_generation
from input_validation import get_valid_choice


def example_enter_part(search_word, meaning, NUMBER_OF_EXAMPLES, use_ai, words_generation_complexity):
    generated_variants = []
    suitable_generated_variants = [[],[]]

    while True:
        if(len(suitable_generated_variants[0] ) != NUMBER_OF_EXAMPLES):
            if(use_ai):
                print(f'\nWrite one simple sentence in English for the {words_generation_complexity} level where the word \033[92m{search_word}\033[0m is used with the meaning {meaning}. Don`t use Russian words in your sentences!')
                if not generated_variants:
                    response = example_generation(1,generated_variants, search_word, meaning, words_generation_complexity)
                else:
                    response = example_generation(2,generated_variants, search_word, meaning, words_generation_complexity)
                
                print()
                print(response)
                print() 

                user_input = get_valid_choice('Введите "+" для сохранения, "-" для повторного запроса, "/" для остановки работы и сохранения изменений: ')

                if(user_input == '+'):                
                    generated_variants.append(response)
                    if(NUMBER_OF_EXAMPLES > 1):
                        suitable_generated_variants[0].append(input(f'Введите {len(suitable_generated_variants[0]) + 1} пример для передней стороны: '))
                        suitable_generated_variants[1].append(input(f'Введите {len(suitable_generated_variants[1]) + 1} пример для задней стороны: '))
                    else:
                        suitable_generated_variants[0].append(input(f'Введите пример для передней стороны: '))
                        suitable_generated_variants[1].append(input(f'Введите пример для задней стороны: '))
                    continue

                if(user_input == '-'):
                    generated_variants.append(response)
                    print('\n' * 2)
                    continue
            else:
                suitable_generated_variants[0].append(input(f'Введите {len(suitable_generated_variants[0]) + 1} пример для передней стороны: '))
                suitable_generated_variants[1].append(input(f'Введите {len(suitable_generated_variants[1]) + 1} пример для задней стороны: '))
        else:
            return suitable_generated_variants
