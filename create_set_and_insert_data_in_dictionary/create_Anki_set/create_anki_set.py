
import requests

def create_anki_card_with_awesome_tts(deck_name, front, back, language_code):
    # Данные для создания карточки
    note = {
        "deckName": deck_name,
        "modelName": "Basic",
        "fields": {
            "Front": front,
            "Back": back
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

            # Запрос на добавление TTS через Awesome TTS
            request_data_add_tts = {
                "action": "updateNoteFields",
                "version": 6,
                "params": {
                    "note": {
                        "id": note_id,
                        "fields": {
                            "Front": f"{front} [sound:awesome_tts_{language_code}_{front}.mp3]"
                        }
                    }
                }
            }

            # Отправка POST-запроса на AnkiConnect для добавления TTS
            response_tts = requests.post("http://localhost:8765", json=request_data_add_tts)
            if response_tts.status_code == 200:
                result_tts = response_tts.json()
                if result_tts['error'] is None:
                    print("TTS added successfully to card ID:", note_id)
                else:
                    print("Error adding TTS:", result_tts['error'])
            else:
                print("Failed to connect to AnkiConnect for TTS")
        else:
            print("Error:", result['error'])
    else:
        print("Failed to connect to AnkiConnect")

# Пример использования
deck_name = "Default"
front = "What is the capital of France?"
back = "Paris"
language_code = "en_US"  # Укажите код языка для TTS

create_anki_card_with_awesome_tts(deck_name, front, back, language_code)