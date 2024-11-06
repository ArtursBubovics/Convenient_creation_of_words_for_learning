import random
from create_set_and_insert_data_in_dictionary.create_Anki_set.create_anki_card import create_anki_card
from create_set_and_insert_data_in_dictionary.create_Anki_set.create_images.display_images import display_images
from create_set_and_insert_data_in_dictionary.create_Anki_set.create_images.search_images import search_images
from UI.show_images import show_images
from random_word_generation_from_dictionary.random_word_generation_from_dictionary import random_word_generation_from_dictionary


CREATE_SET_ANKI_AND_COMPLETE_THE_DICTIONARY_WITHOUT_AI = 1
CREATE_SET_ANKI_AND_COMPLETE_THE_DICTIONARY_WITH_AI = 2
WORDS_RANDOM_GENERATION = 3
PROPOSAL_RANDOM_GENERATION = 4

NUMBER_OF_EXAMPLES = 2

# WANT_TO_FINISH = 1

def action_selection_func(action, wb, ws):

    if(action == CREATE_SET_ANKI_AND_COMPLETE_THE_DICTIONARY_WITHOUT_AI):
        create_anki_card(wb, ws, use_ai=False)
    
    if(action == CREATE_SET_ANKI_AND_COMPLETE_THE_DICTIONARY_WITH_AI):
        
        create_anki_card(wb, ws, use_ai=True)




            # image_urls = search_images(word)
            

            # if image_urls:
            #     print("Найденные изображения:")
            #     # show_images(image_urls)
            #     display_images(image_urls)
                
            #     choice = int(input("Введите номер изображения, которое вам понравилось: "))
                
            #     if 1 <= choice <= len(image_urls):
            #         selected_image_url = image_urls[choice - 1]
            #         # create_anki_set(deck_name, word, meaning, selected_image_url)
            #     else:
            #         print("Неправильный выбор номера изображения.")
            # else:
            #     print("Изображения не найдены.")
    
    if(action == WORDS_RANDOM_GENERATION):
        
        random_word_generation_from_dictionary(wb, ws)
        ...

    if(action == PROPOSAL_RANDOM_GENERATION):
        ...
    

    # if(choose_action == PROPOSAL_GENERATION):
    #     # Сохранение обновленных данных в Excel
    #     if saved_flag:

    #         workbook.save(excel_file)
    #         print('\033[92mИзменения сохранены\033[0m')
    #     else:
    #         print('\033[92mНичего не было сохранено\033[0m')

    # elif(choose_action == WORDS_GENERATION):
    #     print('Как вы хотите, чтобы была генерация: ')
    #     print('''
    #     1 - Только английские слова;
    #     2 - Только русские слова;
    #     3 - Анлийские слова, потом русские;
    #     4 - Русские слова, потом английские;
    #     ''')
    #     word_generation_selection = int(input('Ваш выбр: '))
    #     while(True):
    #         random_index = random.choice(green_cells)

    #         print()

    #         # if(word_generation_selection == WORDS_GENERATION_ONLY_ENG_WORDS):
    #         #     # Получаем значение из колонки 'words' для соответствующей строки (random_index)
    #         #     print(f"\033[92m{df.at[random_index, 'words']}\033[0m")
    #         # elif(word_generation_selection == WORDS_GENERATION_ONLY_RUS_WORDS):
    #         #     print(f"\033[92m{df.at[random_index, 'перевод']}\033[0m")
    #         # elif(word_generation_selection == WORDS_GENERATION_ENG_WORDS_THEN_RUS):
    #         #     ...
    #         # elif(word_generation_selection == WORDS_GENERATION_RUS_WORDS_THEN_ENG):
    #         #     ...
    #         if(int(input('Хотите ли вы закончить работу программы? 1 - Да, 2 - Нет: ')) == WANT_TO_FINISH):
    #             break
