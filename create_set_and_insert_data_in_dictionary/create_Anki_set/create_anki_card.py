from create_set_and_insert_data_in_dictionary.Insert_data_in_Excel.Inset_data_in_excel import inset_data_in_excel
from create_set_and_insert_data_in_dictionary.create_Anki_set.create_card_in_anki.create_card_in_anki import create_card_in_anki
from AI.example_generation.example_generation_response import example_generation_response
from AI.meaning_generation.meaning_generation_response import meaning_generation_response
from AI.transcription_generation.transcription_generation_response import transcription_generation_response
from create_set_and_insert_data_in_dictionary.create_Anki_set.words_generation_complexity.words_generation_complexity import words_generation_complexity_func
from input_validation import get_non_empty_input, get_non_empty_and_symbol_input, get_valid_number


def create_anki_card(df, wb, ws):
    final_front_sentences = []
    final_back_sentences = []
    
    language_code = "en-US"

    deck_name = get_non_empty_input("Enter the name of the deck: ")
    num_cards = get_valid_number("Enter the number of cards to create: ")
    words_generation_complexity = words_generation_complexity_func()


    for i in range(num_cards):
        print(f"\nCreating card {i + 1}/{num_cards}")

        search_word = get_non_empty_and_symbol_input("Enter the word you are studying: ", pattern=r"^[a-zA-Z0-9 ]+$")  # СДЕЛАТЬ ВЫБР ( ГЕНЕРАЦИЯ ИЛИ ВПИСАТЬ )
        meaning = get_non_empty_and_symbol_input("Enter the meaning of the word in Russian: ", pattern=r"^[а-яА-Я0-9 ]+$")  # СДЕЛАТЬ ВЫБР ( ГЕНЕРАЦИЯ ИЛИ ВПИСАТЬ ) ( вписать на русском или на предложением )


        print('\n---------------------------------------------\n')

        meaningReturn = meaning_generation_response(search_word, meaning, words_generation_complexity)

        print('\n---------------------------------------------\n')
        number_of_examples = get_valid_number("Enter the number of examples: ")
        examplesReturn = example_generation_response(search_word, meaning, number_of_examples, words_generation_complexity)
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

        print('\n---------------------------------------------\n')
        
        create_card_in_anki(deck_name, meaningReturn, final_front_sentences, search_word, final_back_sentences, transcriptionReturn, language_code)

        inset_data_in_excel(df, wb, ws, search_word, transcriptionReturn, meaningReturn, final_back_sentences, meaning)