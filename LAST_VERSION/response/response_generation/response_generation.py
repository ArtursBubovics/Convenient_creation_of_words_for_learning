import g4f
from g4f.Provider import You

FIRST_REQUES = 1

def response_generation(variant_value, generated_sentences, search_word, search_word_translate):
# Формирование запроса к GPT
    if variant_value == FIRST_REQUES:
        request = f'Напиши только: одно простое предложение на англ где будет слово \033[92m{search_word}\033[0m со смыслом \033[92m{search_word_translate}\033[0m. Добавь к предложению на английском значек * с двух сторон, к русскому предложению не добавляй!'

    else:
        request = f'Напиши только: одно простое предложение на англ где будет слово \033[92m{search_word}\033[0m со смыслом \033[92m{search_word_translate}\033[0m! Добавь к предложению на английском значек * с двух сторон, к русскому предложению не добавляй! Не используй одно из этих предложений {generated_sentences}, напиши другое!'
    
    print(request)
    print('Немного подождите...')

    try:
        # Получение ответа от GPT
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            provider=g4f.Provider.You,
            messages=[{"role": "user", "content": request}]
        )
        return response

    except Exception as e:
        print(f"Произошла ошибка при выполнении запроса к GPT: {e}")

