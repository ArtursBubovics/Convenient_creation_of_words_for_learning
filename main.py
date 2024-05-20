import os
import pandas as pd
from openpyxl import load_workbook
from action_selection import action_selection_func



# создать сетингс файл и там жержать нижную часть связвнную с Excel


saved_flag = False
# Загрузка данных из Excel
excel_file = os.path.abspath(r'C:\Users\papar\Desktop\Словарь(Англ).xlsx')
df = pd.read_excel(excel_file, engine='openpyxl')

# Открываем Excel-файл для чтения цвета ячейки
workbook = load_workbook(excel_file)
worksheet = workbook.active

print('Выберите из предложенных вариантов программу действий: ')
print('''
1 - создать сет в anki и заполнить словарь в excel
2 - вывод рандомных слов из словарика
3 - вывод рандомных значений слов из словарика
''')

choose_action = input('Какое действие Вы хотите, чтобы программа сделала: ')

action_selection_func(int(choose_action), excel_file, df, workbook, worksheet)
