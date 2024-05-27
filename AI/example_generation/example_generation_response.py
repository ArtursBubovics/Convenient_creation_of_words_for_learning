

from AI.example_generation.example_generation.example_generation import example_generation
from input_validation import get_valid_choice


def example_generation_response(search_word, meaning, NUMBER_OF_EXAMPLES):
    generated_variants = []
    suitable_generated_variants = [[],[]]

    while True:
        if(len(suitable_generated_variants[0] ) != NUMBER_OF_EXAMPLES):
            if not generated_variants:
                response = example_generation(1,generated_variants, search_word, meaning)
            else:
                response = example_generation(2,generated_variants, search_word, meaning)
            
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
                continue
        else:
            return suitable_generated_variants
