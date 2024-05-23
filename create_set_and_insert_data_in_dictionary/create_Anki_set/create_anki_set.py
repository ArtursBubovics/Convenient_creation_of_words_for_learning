import requests
from gtts import gTTS
import uuid
import os
import base64

def create_anki_card(deck_name, front_meaning, front_sentences, back_word, back_examples, transcription, language_code):

    if not deck_exists(deck_name):
        create_deck(deck_name)

    audio_paths = create_audio_files(front_meaning, front_sentences, back_word, back_examples, language_code)
    upload_audio_files(audio_paths)

    # Форматирование передней стороны карточки
    front_field = f"{front_meaning}<br/>[sound:{audio_paths['front_meaning']}]<br/><br/>"
    front_field += "<br/><br/>".join([f"{i}) {sentence}<br/>" for i, sentence in enumerate(front_sentences, 1)])

    # Форматирование задней стороны карточки
    back_field = f"{back_word}<br/>[sound:{audio_paths['back_word']}]<br/><br/>{transcription}<br/><br/>"
    back_field += "<br/><br/>".join([f"{i}) {example}<br/>[sound:{audio_paths[f'back_example_{i}']}]" for i, example in enumerate(back_examples, 1)])

    # Данные для создания карточки
    note = {
        "deckName": deck_name,
        "modelName": "Простая",
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


def deck_exists(deck_name):
    # Запрос к AnkiConnect для получения списка существующих колод
    request_data = {
        "action": "deckNames",
        "version": 6
    }
    response = requests.post("http://localhost:8765", json=request_data)
    
    if response.status_code == 200:
        result = response.json()
        if result['error'] is None:
            deck_names = result['result']
            return deck_name in deck_names
        else:
            print("Error:", result['error'])
    else:
        print("Failed to connect to AnkiConnect")
    return False


def create_deck(deck_name):
    # Запрос к AnkiConnect для создания новой колоды
    request_data = {
        "action": "createDeck",
        "version": 6,
        "params": {
            "deck": deck_name
        }
    }
    response = requests.post("http://localhost:8765", json=request_data)
    
    if response.status_code == 200:
        result = response.json()
        if result['error'] is not None:
            print("Error:", result['error'])
    else:
        print("Failed to connect to AnkiConnect")



def create_audio_files(front_meaning, front_sentences, back_word, back_examples, language_code):
    audio_paths = {}
    
    def save_audio(text, prefix):
        file_name = f"{prefix}_{uuid.uuid4().hex}.mp3"
        tts = gTTS(text=text, lang=language_code)
        tts.save(file_name)
        return file_name
    
    # Create audio for front_meaning
    audio_paths["front_meaning"] = save_audio(front_meaning, f"awesome_tts_{language_code}_front_meaning")

    # Create audio for front_sentences
    for i, sentence in enumerate(front_sentences, 1):
        audio_paths[f"front_sentence_{i}"] = save_audio(sentence, f"awesome_tts_{language_code}_front_sentence_{i}")

    # Create audio for back_word
    audio_paths["back_word"] = save_audio(back_word, f"awesome_tts_{language_code}_back_word")

    # Create audio for back_examples
    for i, example in enumerate(back_examples, 1):
        audio_paths[f"back_example_{i}"] = save_audio(example, f"awesome_tts_{language_code}_back_example_{i}")

    return audio_paths

def upload_audio_files(audio_paths):
    # Список файлов для загрузки
    files_to_upload = [{"filename": os.path.basename(path), "path": path} for path in audio_paths.values()]
    
    # Формирование запроса для загрузки файлов
    request_data = {
        "action": "storeMediaFile",
        "version": 6,
        "params": {
            "filename": "",
            "data": ""
        }
    }
    
    for file in files_to_upload:
        request_data["params"]["filename"] = file["filename"]
        with open(file["path"], "rb") as f:
            file_data = base64.b64encode(f.read()).decode('utf-8')
            request_data["params"]["data"] = file_data
        response = requests.post("http://localhost:8765", json=request_data)
        if response.status_code == 200:
            result = response.json()
            if result['error'] is not None:
                print("Error uploading file:", result['error'])
            else:
                print(f"File {file['filename']} uploaded successfully")
        else:
            print(f"Failed to upload file: {file['filename']}")