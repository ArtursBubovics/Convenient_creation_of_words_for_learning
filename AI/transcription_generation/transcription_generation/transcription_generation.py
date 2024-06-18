import g4f
from g4f.Provider import You

FIRST_REQUES = 1

def transcription_generation(variant_value, generated_variants, search_word):
    # Формирование запроса к GPT
    if variant_value == FIRST_REQUES:
        request = f'\nWrite US and UK transcription of the word \033[92m{search_word}\033[0m'

    else:
        request = f'\nWrite US and UK transcription of the word \033[92m{search_word}\033[0m. Don`t use one of these {generated_variants} examples, write another!'


    if(variant_value != FIRST_REQUES):
  
        print('\n---------------------------------------------')
        print('\nHere are the past generations: ')
        for i, variant in enumerate(generated_variants, start=1):
            
            print(f"\n{i}. {variant}")

    print('\n---------------------------------------------')


    print('\nWait a little...')


    try:
        # Получение ответа от GPT
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            provider=g4f.Provider.You,
            messages=[{"role": "user", "content": request}]
        )
        return response

    except Exception as e:
        print(f"An error occurred while executing a GPT request: {e}")