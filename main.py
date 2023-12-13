import g4f
import os
import re;

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

# response = g4f.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Что такое оно"}],
#     stream=True,
# )
# for message in response:
#     print(message, flush=True, end='')

# Загрузка данных из Excel
excel_file = os.path.abspath(r'C:\Users\papar\Desktop\Engl_words.xlsx')
df = pd.read_excel(excel_file, engine='openpyxl')

# Открываем Excel-файл для чтения цвета ячейки
workbook = load_workbook(excel_file)
worksheet = workbook.active

# Проход по каждой строке в Excel
for index, row in df.iterrows():
    

  # Проверка цвета заливки ячейки в колонке 'В картачках'
    cell_color = worksheet.cell(row=index+2, column=df.columns.get_loc('В картачках') + 1).fill.start_color.rgb

    # Если цвет заливки не белый, пропустить обработку строки
    if cell_color == '00000000':
    # Получение значения из нужного поля в Excel
        search_word = row['words']
        search_word_translate = row['перевод']

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
        except Exception as e:
            print(f"Произошла ошибка при выполнении запроса к GPT: {e}")
            continue  # Пропустить текущую итерацию цикла, если запрос не выполнен успешно

        # Вывод ответа
        print()  
        print(response)
        print() 

        # Предложение для сохранения
        user_input = input('Введите "+" для сохранения, "-" для повторного запроса, "/" для остановки работы и сохранения изменений: ')

        if user_input == '+':
            # Сохранение предложения в другом поле в Excel
            df.at[index, 'примеры в тексте'] = response.strip()
            
            print('\033[91mНе сохранено. Для сохранения нужно нажать на " / "\033[0m')

            print('---------------------')
            print()
            # Сохранение обновленных данных в Excel
            try:

                # Паттерн для поиска текста внутри *
                pattern = r'\*(.*?)\*'

                # Используем re.search для поиска первого соответствия
                match = re.search(pattern, response)

                # Если найдено соответствие, получаем текст внутри *
                if match:
                    text_inside_asterisks = match.group(1)
                    worksheet.cell(row=index + 2, column=df.columns.get_loc('примеры в тексте') + 1, value=text_inside_asterisks.strip())
                    print("Данные успешно сохранены в Excel.")
                else:
                    print("Соответствие не найдено.") 

            except Exception as e:
                print(f"Произошла ошибка при сохранении в Excel: {e}")
        elif user_input == '-':
            break  # Повторить запрос, пропустив текущую итерацию цикла


# Сохранение обновленных данных в Excel
workbook.save(excel_file)
print('\033[91m{search_word}\033[0m')