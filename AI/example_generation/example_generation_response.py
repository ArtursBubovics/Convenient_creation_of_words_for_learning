

from AI.example_generation.example_generation.example_generation import example_generation


def example_generation_response(search_word, meaning):
    generated_variants = []
    suitable_generated_variants = []

    NUMBER_OF_EXAMPLES = 2

    while True:

        if not generated_variants:
            response = example_generation(1,generated_variants, search_word, meaning)
        else:
           response = example_generation(2,generated_variants, search_word, meaning)
        
        print()
        print(response)
        print() 

        user_input = input('Введите "+" для сохранения, "-" для повторного запроса, "/" для остановки работы и сохранения изменений: ')

        if(user_input == '+'):
            if(len(suitable_generated_variants) == NUMBER_OF_EXAMPLES - 1):
                generated_variants.append(response)
                return generated_variants
            
            generated_variants.append(response)
            suitable_generated_variants.append(response)
            continue

        if(user_input == '-'):
            generated_variants.append(response)
            continue

