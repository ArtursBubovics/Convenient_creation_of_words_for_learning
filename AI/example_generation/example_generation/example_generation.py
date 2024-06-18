import g4f
from g4f.Provider import You

FIRST_REQUES = 1

def example_generation(variant_value, generated_variants, search_word, meaning, words_generation_complexity):
    # Формирование запроса к GPT
    if variant_value == FIRST_REQUES:
        request = f'\nWrite one simple sentence in English for the {words_generation_complexity} level where the word \033[92m{search_word}\033[0m is used with the meaning {meaning}.. Don`t use Russian words in your sentences!'

    else:
        request = f'\nWrite just one simple example in English for the {words_generation_complexity} level where the word \033[92m{search_word}\033[0m will be used with the meaning {meaning}. Don`t use Russian words in your sentences! Don`t use one of these {generated_variants} sentences, write another!'
    
    print(request)
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