from AI.transcription_generation.transcription_generation.transcription_generation import transcription_generation

def transcription_generation_response(search_word):
    generated_variants = []

    while True:

        if not generated_variants:
            response = transcription_generation(1,generated_variants, search_word)
        else:
           response = transcription_generation(2,generated_variants, search_word)
        
        print()
        print(response)
        print() 

        user_input = input('Введите "+" для сохранения, "-" для повторного запроса, "/" для остановки работы и сохранения изменений: ')

        if(user_input == '+'):
            return input('Введите транскрипцию: ')

        if(user_input == '-'):
            generated_variants.append(response)
            continue

