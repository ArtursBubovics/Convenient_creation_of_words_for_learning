import requests
import json

def create_anki_card(deck_name, front_meaning, front_sentences, back_word, back_examples, transcription, language_code):
    # Форматирование передней стороны карточки
    front_field = f"{front_meaning} <br/>[sound:awesome_tts_{language_code}_front_meaning.mp3]<br/><br/>"
    front_field += "<br/><br/>".join([f"{sentence} <br/>[sound:awesome_tts_{language_code}_front_{i}.mp3]" for i, sentence in enumerate(front_sentences, 1)])

    # Форматирование задней стороны карточки
    back_field = f"{back_word} <br/>[sound:awesome_tts_{language_code}_back_word.mp3] <br/><br/>{transcription} <br/><br/>"
    back_field += "<br/><br/>".join([f"{example} <br/>[sound:awesome_tts_{language_code}_back_example_{i}.mp3]" for i, example in enumerate(back_examples, 1)])

    # Данные для создания карточки
    note = {
        "deckName": deck_name,
        "modelName": "Basic",
        "fields": {
            "Front": front_field,
            "Back": back_field
        },
        "tags": []
    }

    # Данные для запроса на добавление карточки
    request_data_add_note = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": note
        }
    }

    # Отправка POST-запроса на AnkiConnect для добавления карточки
    response = requests.post("http://localhost:8765", json=request_data_add_note)
    
    if response.status_code == 200:
        result = response.json()
        if result['error'] is None:
            note_id = result['result']
            print("Card created successfully with ID:", note_id)
        else:
            print("Error:", result['error'])
    else:
        print("Failed to connect to AnkiConnect")
