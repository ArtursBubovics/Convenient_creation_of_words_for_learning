from AI.transcription_generation.transcription_generation.transcription_generation import transcription_generation
from input_validation import get_valid_choice

def transcription_generation_response(search_word):
    generated_variants = []

    while True:
        print(f'\nWrite US and UK transcription of the word \033[92m{search_word}\033[0m using IPA system')
        if not generated_variants:
            response = transcription_generation(1,generated_variants, search_word)
        else:
           response = transcription_generation(2,generated_variants, search_word)
        
        print()
        print(response)
        print() 

        user_input = get_valid_choice('Введите "+" для сохранения, "-" для повторного запроса, "/" для остановки работы и сохранения изменений: ')

        if(user_input == '+'):
            return input('Введите транскрипцию: ')

        if(user_input == '-'):
            generated_variants.append(response)
            print('\n' * 2)
            continue

