import requests
from gtts import gTTS
import uuid
import os
import base64
import time
import subprocess

MEDIA_FOLDER = r'C:\Users\papar\AppData\Roaming\Anki2\1-й пользователь\collection.media'

def is_anki_running():
    try:
        response = requests.post("http://localhost:8765", json={"action": "version", "version": 6})
        if response.status_code == 200:
            return True
    except requests.exceptions.ConnectionError:
        return False

def start_anki():
    anki_path = r'C:\Users\papar\AppData\Local\Programs\Anki\anki.exe'
    if os.path.exists(anki_path):
        subprocess.Popen(['cmd', '/c', 'start', '', anki_path], shell=True)
        
        # Проверяем состояние Anki каждые 2 секунды, максимум 30 секунд
        for _ in range(15):
            if is_anki_running():
                print("Anki started successfully.")
                return
            time.sleep(2)
        
        print("Failed to start Anki within the timeout period.")
    else:
        print(f"Anki not found at {anki_path}")

def create_card_in_anki(deck_name, front_meaning, front_sentences, back_word, back_examples, transcription, language_code):

    if not is_anki_running():
        print("Anki is not running. Starting Anki...")
        start_anki()

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
        file_path = os.path.join(MEDIA_FOLDER, file_name)
        tts = gTTS(text=text, lang=language_code, tld='us')
        tts.save(file_path)
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
    files_to_upload = [{"filename": file_name, "path": os.path.join(MEDIA_FOLDER, file_name)} for file_name in audio_paths.values()]
    
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