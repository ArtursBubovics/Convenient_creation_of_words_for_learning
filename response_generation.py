import g4f

def response_generation(search_word, search_word_translate):
# Формирование запроса к GPT
    request = f'Напиши только: одно простое предложение на англ где будет слово \033[92m{search_word}\033[0m со смыслом \033[92m{search_word_translate}\033[0m. Добавь к предложению на английском значек * с двух сторон, к русскому предложению не добавляй!'
    print(request)
    print('Немного подождите...')

    try:
        # Получение ответа от GPT
        response = g4f.ChatCompletion.create(
            model=g4f.models.gpt_4,
            messages=[{"role": "user", "content": request}]
        )

        return response

    except Exception as e:
        print(f"Произошла ошибка при выполнении запроса к GPT: {e}")

