from create_set_and_insert_data_in_dictionary.Insert_data_in_Excel.Inset_data_in_excel import inset_data_in_excel
from create_set_and_insert_data_in_dictionary.create_Anki_set.create_card_in_anki.create_card_in_anki import create_card_in_anki
from AI.meaning_generation.meaning_generation_response import meaning_generation_response
from AI.transcription_generation.transcription_generation_response import transcription_generation_response
from create_set_and_insert_data_in_dictionary.create_Anki_set.example_enter_part.example_enter_part import example_enter_part
from create_set_and_insert_data_in_dictionary.create_Anki_set.words_generation_complexity.words_generation_complexity import words_generation_complexity_func
from input_validation import get_non_empty_input, get_non_empty_and_symbol_input, get_valid_number


def create_anki_card(wb, ws, use_ai):
    final_front_sentences = []
    final_back_sentences = []
    
    language_code = "en-US"

    deck_name = get_non_empty_input("Enter the name of the deck: ")
    num_cards = get_valid_number("Enter the number of cards to create: ")

    words_generation_complexity = None
    if(use_ai):
        words_generation_complexity = words_generation_complexity_func()


    for i in range(num_cards):
        print(f"\nCreating card {i + 1}/{num_cards}")

        search_word = get_non_empty_and_symbol_input("Enter the word you are studying: ", pattern = r"^[a-zA-Z0-9 ,;()\-!_?.`']+$")  # СДЕЛАТЬ ВЫБР ( ГЕНЕРАЦИЯ ИЛИ ВПИСАТЬ )

        words = ws.range("F1").expand('down').value

        for item in words:
            if search_word in item:
                print('\nWord find!')
                #показать строку
                row_data = ws.range("A1:K1").value
                print('Under is word sheets:\n')
                for index, row in enumerate(row_data, start=1):
                    print(f'{index}){ws.range("A{start}").value}\n')
                    print(f'{index}){ws.range("J{cell.row}").value}\n\n')
                    
                print('Do you want to stay keep?')
                
                if(input('Yes is (+) ; No is (-):') == '+'):
                    break
                else:
                    search_word = get_non_empty_and_symbol_input("Enter the word you are studying: ", pattern = r"^[a-zA-Z0-9 ,;()\-!_?.`']+$")  # СДЕЛАТЬ ВЫБР ( ГЕНЕРАЦИЯ ИЛИ ВПИСАТЬ )
                    break
        
        meaning = get_non_empty_and_symbol_input("Enter the meaning of the word in Russian: ", pattern = r"^[а-яА-Я0-9 ,;()\-!_?.`']+$")  # СДЕЛАТЬ ВЫБР ( ГЕНЕРАЦИЯ ИЛИ ВПИСАТЬ ) ( вписать на русском или на предложением )


        print('\n---------------------------------------------\n')

        usageRate = get_non_empty_and_symbol_input("Enter the usage rate of the word: ", pattern = r"^[a-zA-Z0-9 +-]+$")

        print('\n---------------------------------------------\n')

        partOfSpeech = get_non_empty_and_symbol_input("Enter the part of speech of the word: ", pattern = r"^[a-zA-Z_]+$")

        print('\n---------------------------------------------\n')

        if(use_ai):
            meaningReturn = meaning_generation_response(search_word, meaning, words_generation_complexity)
        else:
            meaningReturn = get_non_empty_and_symbol_input("Enter meaning: ", pattern = r"^[a-zA-Z0-9 ,;()\-!_?.`'@#$%^&*\[\]{}]+$")


        print('\n---------------------------------------------\n')
        number_of_examples = get_valid_number("Enter the number of examples: ")

        examplesReturn = example_enter_part(search_word, meaning, number_of_examples, use_ai, words_generation_complexity)

        final_front_sentences = examplesReturn[0]
        final_back_sentences = examplesReturn[1]

        print('\n---------------------------------------------\n')

        if(use_ai):
            transcriptionReturn = transcription_generation_response(search_word)
        else:
            transcriptionReturn = get_non_empty_and_symbol_input("Enter transcription: ") # добавить все символы


        print('\n---------------------------------------------\n')

        print('Entered data:\n')
        print('\033[92m Word \033[0m: ' + search_word + '\n')
        print('\033[92m Transcription \033[0m: ' + transcriptionReturn + '\n')
        print('\033[92m Translation RU \033[0m: ' + meaning + '\n')

        print('\033[92m Part Of Speech \033[0m: ' + search_word + '\n')
        print('\033[92m Usage Rate \033[0m: ' + usageRate + '\n')

        print('\033[92m Meaning \033[0m: ' + meaningReturn + '\n')

        print('\033[92m Examples \033[0m:\n')
        print('    1. \033[92m front examples\033[0m: '+ str(final_front_sentences) + '\n')
        print('    2. \033[92m back examples\033[0m:' + str(final_back_sentences) +'\n')

        print('\n---------------------------------------------\n')

        while True:
            print('You want to make a change?')

            if(get_non_empty_and_symbol_input("Enter (+) to change or (-) to continue: ", pattern = r"^[+-]$") == '+'): # тут проблема с симболом когда я ввожу - то он все рано продолжает работать и заходит в иф

                while True:
                    print('\n---------------------------------------------\n')
                    print('You can change any data. \n')
                    print('If you want to change the word, please enter 1\n')
                    print('If you want to change the Russian meaning, please enter 2\n')
                    print('If you want to change the word meaning, please enter 3\n')
                    print('If you want to change the transcription, please enter 4\n')
                    print('If you want to change the usage rate, please enter 5\n')
                    print('If you want to change the part of speech, please enter 6\n')
                    print('If you want to change the excamples, please enter 7\n')
                    print('If you want to EXIT, please enter 8\n')

                    match get_valid_number("Enter the number of the data you want to change: "): # проврека должна быть на float числа .....
                        case 1:
                            search_word = get_non_empty_and_symbol_input("Enter the word you are studying: ", pattern = r"^[a-zA-Z0-9 ,;()\-!_?.`']+$")  # СДЕЛАТЬ ВЫБР ( ГЕНЕРАЦИЯ ИЛИ ВПИСАТЬ )
                        case 2:
                            meaning = get_non_empty_and_symbol_input("Enter the meaning of the word in Russian: ", pattern = r"^[a-zA-Zа-яА-Я0-9 ,;()\-!_?.`']+$")
                        case 3:
                            meaningReturn = get_non_empty_and_symbol_input("Enter the meaning of the English word: ")
                        case 4:
                            transcriptionReturn = get_non_empty_and_symbol_input("Enter transcription: ")
                        case 5:
                            usageRate = get_non_empty_and_symbol_input("Enter the usage rate of the word: ", pattern = r"^[a-zA-Z0-9 +-]+$")
                        case 6:
                            partOfSpeech = get_non_empty_and_symbol_input("Enter the part of speech of the word: ", pattern = r"^[a-zA-Z_]+$")
                        case 7:
                            number_of_examples = get_valid_number("Enter the number of examples: ")
                            #добавить если пользватель хочет что то одно изменить
                            examplesReturn = example_enter_part(search_word, meaning, number_of_examples, use_ai, words_generation_complexity)
                            final_front_sentences = examplesReturn[0]
                            final_back_sentences = examplesReturn[1]
                        case 8:
                            print("Exiting the program.")
                            break
                        case _:
                            print("Invalid choice. Please try again.")
                            continue
                
                print('\n---------------------------------------------\n')
                print('Entered data:\n')
                print('\033[92m Word \033[0m: ' + search_word + '\n')
                print('\033[92m Transcription \033[0m: ' + transcriptionReturn + '\n')
                print('\033[92m Translation RU \033[0m: ' + meaning + '\n')

                print('\033[92m Part Of Speech \033[0m: ' + search_word + '\n')
                print('\033[92m Usage Rate \033[0m: ' + usageRate + '\n')

                print('\033[92m Meaning \033[0m: ' + meaningReturn + '\n')

                print('\033[92m Examples \033[0m:\n')
                print('    1. \033[92m front examples\033[0m: '+ str(final_front_sentences) + '\n')
                print('    2. \033[92m back examples\033[0m:' + str(final_back_sentences) +'\n')

                break
            break
        
        print('\n---------------------------------------------\n') 
          
        create_card_in_anki(deck_name, meaningReturn, final_front_sentences, search_word, meaning, final_back_sentences, transcriptionReturn, language_code)

        inset_data_in_excel(wb, ws, usageRate, partOfSpeech, search_word, transcriptionReturn, meaningReturn, final_back_sentences, meaning)