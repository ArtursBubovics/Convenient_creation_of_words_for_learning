from AI.meaning_generation.meaning_generation.meaning_generation import meaning_generation
from input_validation import get_valid_choice


def meaning_generation_response(search_word, meaning, words_generation_complexity):
    generated_variants = []

    while True:

        if not generated_variants:
            response = meaning_generation(1,generated_variants, search_word, meaning, words_generation_complexity)
        else:
           response = meaning_generation(2,generated_variants, search_word, meaning, words_generation_complexity)
        
        print()
        print(response)
        print() 

        user_input = get_valid_choice('Введите "+" для сохранения, "-" для повторного запроса, "/" для остановки работы и сохранения изменений: ')

        if(user_input == '+'):
            return  "It's mean: " + input('Введите объяснение: ')

        if(user_input == '-'):
            generated_variants.append(response)
            continue

