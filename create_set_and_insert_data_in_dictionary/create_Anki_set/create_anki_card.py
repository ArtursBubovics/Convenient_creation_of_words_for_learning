from create_set_and_insert_data_in_dictionary.Insert_data_in_Excel.Inset_data_in_excel import inset_data_in_excel
from create_set_and_insert_data_in_dictionary.create_Anki_set.create_card_in_anki.create_card_in_anki import create_card_in_anki
from AI.example_generation.example_generation_response import example_generation_response
from AI.meaning_generation.meaning_generation_response import meaning_generation_response
from AI.transcription_generation.transcription_generation_response import transcription_generation_response

def create_anki_card(excel_file, df, workbook, worksheet):
    final_front_sentences = []
    final_back_sentences = []
    
    language_code = "en-US"

    deck_name = input("Enter the name of the deck: ")
    num_cards = int(input("Enter the number of cards to create: "))

    for i in range(num_cards):
        print(f"\nCreating card {i + 1}/{num_cards}")

        search_word =  input("Введите изучаемое слово: ") # СДЕЛАТЬ ВЫБР ( ГЕНЕРАЦИЯ ИЛИ ВПИСАТЬ )
        meaning = input("Введите значение слова на русском: ") # СДЕЛАТЬ ВЫБР ( ГЕНЕРАЦИЯ ИЛИ ВПИСАТЬ )

        print('\n---------------------------------------------\n')

        meaningReturn = meaning_generation_response(search_word, meaning)

        print('\n---------------------------------------------\n')
        number_of_examples = input("Введите количество примеров: ")
        examplesReturn = example_generation_response(search_word, meaning, number_of_examples)
        final_front_sentences = examplesReturn[0]
        final_back_sentences = examplesReturn[1]

        print('\n---------------------------------------------\n')

        transcriptionReturn = transcription_generation_response(search_word)

        print('\n---------------------------------------------\n')

        print('Entered data:\n')
        print('\033[92m Meaning \033[0m: ' + meaningReturn + '\n')

        print('\033[92m Examples \033[0m:\n')
        print('    1. \033[92m front examples\033[0m: '+ str(final_front_sentences) + '\n')
        print('    2. \033[92m back examples\033[0m:' + str(final_back_sentences) +'\n')

        print('\033[92m Transcription \033[0m: ' + transcriptionReturn + '\n')


        create_card_in_anki(deck_name, meaningReturn, final_front_sentences, search_word, final_back_sentences, transcriptionReturn, language_code)

        inset_data_in_excel(excel_file, df, workbook, worksheet, search_word, transcriptionReturn, meaningReturn, final_back_sentences, meaning)