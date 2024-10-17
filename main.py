import os
import pandas as pd
import xlwings as xw
from action_selection import action_selection_func

# Загрузка данных из Excel
sheet_name = 'Dictionary'

# Открываем Excel-файл для чтения цвета ячейки
app = xw.App(visible=True)
wb = app.books.open(r'C:\Users\papar\Desktop\Dictionary_English.xlsx', update_links=False, read_only=False)
ws = wb.sheets[sheet_name]

print('\nChoose a program of action from the following options: ')
print('''
1 - create a set in anki and populate the dictionary in excel
2 - print random words from the dictionary
3 - print values of random words from the dictionary
''')

choose_action = input('What action you want the program to do: ')

action_selection_func(int(choose_action), wb, ws)

# app.quit()