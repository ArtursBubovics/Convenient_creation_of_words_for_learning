import os
import pandas as pd
import tkinter as tk
from openpyxl import load_workbook
from action_selection import action_selection_func

def start_program():
    win = tk.Tk()
    win.title("Выбор действия")

    # Текстовая метка с вариантами действий
    label = tk.Label(win, text="Выберите действие:\n1 - создать сет в anki и заполнить словарь в excel\n2 - вывод рандомных слов из словарика\n3 - вывод рандомных значений слов из словарика")
    label.pack()

    # Поле для ввода выбранного действия
    entry = tk.Entry(win)
    entry.pack()

    # Функция обработки события нажатия кнопки
    def on_button_click():
        choose_action = entry.get()
        action_selection_func(int(choose_action), excel_file, df, workbook, worksheet)
        win.destroy()

    # Кнопка для подтверждения выбранного действия
    button = tk.Button(win, text="Выполнить", command=on_button_click)
    button.pack()

    win.mainloop()



# создать сетингс файл и там жержать нижную часть связвнную с Excel


saved_flag = False
# Загрузка данных из Excel
excel_file = os.path.abspath(r'C:\Users\papar\Desktop\Словарь(Англ).xlsx')
df = pd.read_excel(excel_file, engine='openpyxl')

# Открываем Excel-файл для чтения цвета ячейки
workbook = load_workbook(excel_file)
worksheet = workbook.active

start_program()
