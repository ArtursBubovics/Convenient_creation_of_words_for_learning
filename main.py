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

print('\nChoose a program of action from the following options: ')
print('''
1 - create a set in anki and populate the dictionary in excel
2 - print random words from the dictionary
3 - print values of random words from the dictionary
''')

choose_action = input('What action you want the program to do: ')

action_selection_func(int(choose_action), df, wb, ws)

# app.quit() closes all excels files