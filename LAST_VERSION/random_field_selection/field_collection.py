def field_collection():
    green_cells = []
    # Проход по каждой строке в Excel
    for index, row in df.iterrows():

        # # Проверка наличия значений в текущей строке и следующей строке
        if pd.isna(df.loc[index, 'words']) and pd.isna(df.loc[index, 'перевод']) and pd.isna(df.loc[index + 1, 'words']) and pd.isna(df.loc[index + 1, 'перевод']):
            # Ваш код, который выполнится только в случае, если оба поля в текущей и следующей строках равны NaN
            print("Дальше нету полей для ввода")
            break
        else:
            # Ваш код, который выполнится, если хотя бы одно из полей в текущей или следующей строках не равно NaN
            print("Поле {index} имеет не введенное значение")

        

        # Проверка цвета заливки ячейки в колонке 'В картачках'
        cell_color = worksheet.cell(row=index+2, column=df.columns.get_loc('Is in cards') + 1).fill.start_color.rgb


        if(choose_action == CREATE_SET_ANKI_AND_COMPLETE_THE_DICTIONARY):
            ...

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

                exit_flag = response_func(search_word, search_word_translate, df, index, worksheet) #!!!

                saved_flag = confirmation_save_changes_func(exit_flag) #!!!
                


        if(choose_action == WORDS_GENERATION):
            if cell_color == '00000000':
                green_cells.append(index)