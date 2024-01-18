import random
from response import response_func
from confirmation_save_changes import confirmation_save_changes_func

PROPOSAL_GENERATION = 1
WORDS_GENERATION = 2

WANT_TO_FINISH = 1

def action_selection_func(choose_action, excel_file, df, workbook, worksheet):
    green_cells = []

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


        if(choose_action == PROPOSAL_GENERATION):


        #можно сделать 2 ф для (1 генерац предл и 2 рандомные слова)

            # Если цвет заливки не белый, пропустить обработку строки
            if cell_color == '00000000':

                # # Проверка на наличие NaN в полях
                # if pd.isna(row['words']) or pd.isna(row['перевод']):
                #     print(f"Пропуск строки {index + 2} из-за отсутствия значения в 'words' или 'перевод'")
                #     break


            # Получение значения из нужного поля в Excel
                search_word = row['words']
                search_word_translate = row['перевод']

        #
                exit_flag = response_func(search_word, search_word_translate, df, index, worksheet) #!!!

                saved_flag = confirmation_save_changes_func(exit_flag) #!!!

        #
                


        elif(choose_action == WORDS_GENERATION):
            if cell_color == '00000000':
                green_cells.append(index)
    

    if(choose_action == PROPOSAL_GENERATION):
        # Сохранение обновленных данных в Excel
        if saved_flag:

            workbook.save(excel_file)
            print('\033[92mИзменения сохранены\033[0m')
        else:
            print('\033[92mНичего не было сохранено\033[0m')

    elif(choose_action == WORDS_GENERATION):
        while(True):
            random_index = random.choice(green_cells)

            print()
            # Получаем значение из колонки 'words' для соответствующей строки (random_index)
            print(df.at[random_index, 'words'])
            
            if(int(input('Хотите ли вы закночить работу программы? 1 - Да, 2 - Нет: ')) == WANT_TO_FINISH):
                break
