import os
import pandas as pd
from openpyxl import load_workbook
from response import response_func


# response = g4f.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Что такое оно"}],
#     stream=True,
# )
# for message in response:
#     print(message, flush=True, end='')

saved_flag = False
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

        exit_flag = response_func(search_word, search_word_translate, df, index, worksheet)

        if exit_flag:
            saved_flag = True
            break  # Выход из внешнего цикла при установленном флаге
        else: 
            saved_flag = False

# Сохранение обновленных данных в Excel
if saved_flag:

    workbook.save(excel_file)
    print('\033[92mСохранено\033[0m')
else:
    print('\033[92mНичего не было сохранено\033[0m')