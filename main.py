import os
import pandas as pd
from openpyxl import load_workbook
from action_selection import action_selection_func

saved_flag = False
# Загрузка данных из Excel
excel_file = os.path.abspath(r'C:\Users\papar\Desktop\Engl_words.xlsx')
df = pd.read_excel(excel_file, engine='openpyxl')

# Открываем Excel-файл для чтения цвета ячейки
workbook = load_workbook(excel_file)
worksheet = workbook.active

print('Выберите из предложенных вариантов программу действий: ')
print('''
1 - Сгенерировать предлежение с использованием изучаемых слов;   
2 - Выбрать рандомное слов из изучаемых;
''')

choose_action = input('Какое действие Вы хотите, чтобы программа сделала: ')

action_selection_func(int(choose_action), excel_file, df, workbook, worksheet)
