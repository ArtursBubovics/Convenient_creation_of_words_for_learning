import os
import pandas as pd
import xlwings as xw
from action_selection import action_selection_func

# Загрузка данных из Excel
sheet_name = 'Dictionary'
file_path  = r'C:\Users\papar\Desktop\Dictionary_English.xlsx'

# Открываем Excel-файл для чтения цвета ячейки
app = xw.App(visible=True, add_book=False)

workbook_open = None
for wb in app.books:
    if wb.fullname == file_path:
        workbook_open = wb
        break


if workbook_open:
    wb = workbook_open
else:
    wb = app.books.open(file_path, update_links=False, read_only=False)

ws = wb.sheets[sheet_name]

print('\nChoose a program of action from the following options: ')
print('''
1 - create a set in anki and populate the dictionary in excel (without ai)
2 - create a set in anki and populate the dictionary in excel (with ai)
3 - print random words from the dictionary
4 - print values of random words from the dictionary
''')

choose_action = input('What action you want the program to do: ')

action_selection_func(int(choose_action), wb, ws)

# app.quit()