import re;

def response(search_word, search_word_translate, df,index,worksheet):
    #
    response_generation(search_word, search_word_translate)


    # Вывод ответа
    print()  
    print(response)
    print() 

    # Предложение для сохранения
    user_input = input('Введите "+" для сохранения, "-" для повторного запроса, "/" для остановки работы и сохранения изменений: ')

    if user_input == '+':
        # Сохранение предложения в другом поле в Excel
        df.at[index, 'примеры в тексте'] = response.strip()
        
        print('\033[91mНе сохранено. Для сохранения нужно нажать на " / "\033[0m')

        print('---------------------')
        print()
        # Сохранение обновленных данных в Excel
        try:

            # Паттерн для поиска текста внутри *
            pattern = r'\*(.*?)\*'

            # Используем re.search для поиска первого соответствия
            match = re.search(pattern, response)

            # Если найдено соответствие, получаем текст внутри *
            if match:
                text_inside_asterisks = match.group(1)
                worksheet.cell(row=index + 2, column=df.columns.get_loc('примеры в тексте') + 1, value=text_inside_asterisks.strip())
                print("Данные успешно сохранены в Excel.")
            else:
                print("Соответствие не найдено.") 

        except Exception as e:
            print(f"Произошла ошибка при сохранении в Excel: {e}")
    elif user_input == '-':
        break  # Повторить запрос, пропустив текущую итерацию цикла