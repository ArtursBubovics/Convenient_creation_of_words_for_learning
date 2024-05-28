from create_set_and_insert_data_in_dictionary.Insert_data_in_Excel.Inset_data_in_excel import inset_data_in_excel
from create_set_and_insert_data_in_dictionary.create_Anki_set.create_card_in_anki.create_card_in_anki import create_card_in_anki
from AI.example_generation.example_generation_response import example_generation_response
from AI.meaning_generation.meaning_generation_response import meaning_generation_response
from AI.transcription_generation.transcription_generation_response import transcription_generation_response
from input_validation import get_non_empty_input, get_non_empty_and_symbol_input, get_valid_number


def create_anki_card(excel_file, df, workbook, worksheet):
    final_front_sentences = []
    final_back_sentences = []
    
    language_code = "en-US"

    deck_name = get_non_empty_input("Enter the name of the deck: ")
    num_cards = get_valid_number("Enter the number of cards to create: ")

    for i in range(num_cards):
        print(f"\nCreating card {i + 1}/{num_cards}")

        search_word = get_non_empty_and_symbol_input("Введите изучаемое слово: ", pattern=r"^[a-zA-Z0-9 ]+$")  # СДЕЛАТЬ ВЫБР ( ГЕНЕРАЦИЯ ИЛИ ВПИСАТЬ )
        meaning = get_non_empty_and_symbol_input("Введите значение слова на русском: ", pattern=r"^[а-яА-Я0-9 ]+$")  # СДЕЛАТЬ ВЫБР ( ГЕНЕРАЦИЯ ИЛИ ВПИСАТЬ ) ( вписать на русском или на предложением )


        print('\n---------------------------------------------\n')

        meaningReturn = meaning_generation_response(search_word, meaning)

        print('\n---------------------------------------------\n')
        number_of_examples = get_valid_number("Введите количество примеров: ")
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