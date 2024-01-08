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

    # # Проверка наличия значений в текущей строке и следующей строке
    # if pd.isna(df.loc[index, 'words']) and pd.isna(df.loc[index, 'перевод']) and pd.isna(df.loc[index + 1, 'words']) and pd.isna(df.loc[index + 1, 'перевод']):
    #     # Ваш код, который выполнится только в случае, если оба поля в текущей и следующей строках равны NaN
    #     print("Дальше нету полей для ввода")
    #     break
    # else:
    #     # Ваш код, который выполнится, если хотя бы одно из полей в текущей или следующей строках не равно NaN
    #     print("Поле {index} имеет не введенное значение")

    

  # Проверка цвета заливки ячейки в колонке 'В картачках'
    cell_color = worksheet.cell(row=index+2, column=df.columns.get_loc('В картачках') + 1).fill.start_color.rgb

    # Если цвет заливки не белый, пропустить обработку строки
    if cell_color == '00000000':

        # # Проверка на наличие NaN в полях
        # if pd.isna(row['words']) or pd.isna(row['перевод']):
        #     print(f"Пропуск строки {index + 2} из-за отсутствия значения в 'words' или 'перевод'")
        #     break


    # Получение значения из нужного поля в Excel
        search_word = row['words']
        search_word_translate = row['перевод']

        exit_flag = response_func(search_word, search_word_translate, df, index, worksheet)

        if exit_flag:
            saved_flag = True
            # сделать чтобы определяло есть ли в буфере что-то
            while True:
                save_changes = input("Хотите ли сохранить изменения, если нажмете (+) ДА, (-) НЕТ: ") 
                if(save_changes == '+'):
                    saved_flag = True
                    break
                elif(save_changes == '-'):
                    saved_flag = False
                    break
                else:
                    print("Нету такой команды! Нажмите + или -")

            break  # Выход из внешнего цикла при установленном флаге
        else:
            saved_flag = False


# Сохранение обновленных данных в Excel
if saved_flag:

    workbook.save(excel_file)
    print('\033[92mИзменения сохранены\033[0m')
else:
    print('\033[92mНичего не было сохранено\033[0m')