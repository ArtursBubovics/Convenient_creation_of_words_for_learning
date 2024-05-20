import g4f

FIRST_REQUES = 1

def meaning_generation(variant_value, generated_variants, search_word):
    # Формирование запроса к GPT
    if variant_value == FIRST_REQUES:
        request = f'\nWrite a simple meaning in English of the word \033[92m{search_word}\033[0m! Don`t use the word itself in explaining the word!'

    else:
        request = f'\nWrite a simple meaning in English of the word \033[92m{search_word}\033[0m! Don`t use the word itself in explaining the word! Don`t use one of these {generated_variants} sentences, write another!'
    
    print(request)
    print('Немного подождите...\n')

    try:
        # Получение ответа от GPT
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": request}]
        )

        return response

    except Exception as e:
        print(f"Произошла ошибка при выполнении запроса к GPT: {e}")