import time
start_time = time.perf_counter()

import os
import pandas as pd
import xlwings as xw
from action_selection import action_selection_func
import psutil

# Загрузка данных из Excel
sheet_name = 'Dictionary'
file_path = os.path.normpath(r'C:\Users\papar\Desktop\Dictionary_English.xlsx')

# Открываем Excel-файл для чтения цвета ячейки
app = xw.App(visible=False, add_book=False)


# Проверим, открыт ли процесс Excel
def is_excel_file_open(file_path):
    for process in psutil.process_iter(['name', 'open_files']):
        if process.info['name'] == 'EXCEL.EXE':
            if process.info['open_files']:
                for file in process.info['open_files']:
                    if os.path.normpath(file.path) == os.path.normpath(file_path):
                        return True
    return False

# Закрываем уже открытый файл
def close_excel_file(file_path):
    for process in psutil.process_iter(['name', 'open_files']):
        if process.info['name'] == 'EXCEL.EXE':
            if process.info['open_files']:
                for file in process.info['open_files']:
                    if os.path.normpath(file.path) == os.path.normpath(file_path):
                        # Завершаем процесс
                        process.terminate()
                        print(f"Файл '{file_path}' закрыт.")
                        return True
    return False


# Проверяем, открыт ли файл
workbook_open = None
for wb in app.books:
    if os.path.normpath(wb.fullname) == os.path.normpath(file_path):
        workbook_open = wb
        break

# Если файл не был открыт, откроем его
if not workbook_open:
    if not is_excel_file_open(file_path):
        wb = app.books.open(file_path, update_links=False, read_only=False)
        print("Файл открыт скриптом.")
    else:
        # Закрываем файл, если он открыт в другом экземпляре
        if close_excel_file(file_path):
            wb = app.books.open(file_path, update_links=False, read_only=False)
            print("Файл был закрыт и теперь открыт скриптом.")
else:
    print("Файл уже открыт в этом экземпляре.")




ws = wb.sheets[sheet_name]

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"\nПрограмма загрузилась за {elapsed_time:.2f} секунд.\n")


print('\nChoose a program of action from the following options: ')
print('''
1 - create a set in anki and populate the dictionary in excel (without ai)
2 - create a set in anki and populate the dictionary in excel (with ai)
3 - print random words from the dictionary
4 - print values of random words from the dictionary
''')

choose_action = input('What action you want the program to do: ')

action_selection_func(int(choose_action), wb, ws)

wb.close()
app.quit()