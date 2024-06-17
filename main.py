import os
import pandas as pd
import xlwings as xw
from action_selection import action_selection_func

# создать сетингс файл и там жержать нижную часть связвнную с Excel

saved_flag = False
# Загрузка данных из Excel
sheet_name = 'Dictionary'

# Открываем Excel-файл для чтения цвета ячейки
app = xw.App(visible=False)
wb = xw.Book(r'C:\Users\papar\Desktop\Dictionary.xlsx')
ws = wb.sheets[sheet_name]
df = ws.range('A1').options(pd.DataFrame, header=1, index=False, expand='table').value

print('Выберите из предложенных вариантов программу действий: ')
print('''
1 - создать сет в anki и заполнить словарь в excel
2 - вывод рандомных слов из словарика
3 - вывод рандомных значений слов из словарика
''')

choose_action = input('Какое действие Вы хотите, чтобы программа сделала: ')

action_selection_func(int(choose_action), df, wb, ws)

# app.quit() closes all excels files