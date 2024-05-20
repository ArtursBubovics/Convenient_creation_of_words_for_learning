import requests

def create_anki_set(deck_name, front, back, image_url=None):
    note = {
        "deckName": deck_name,
        "modelName": "Basic",
        "fields": {
            "Front": front,
            "Back": back
        },
        "tags": [],
        "options": {
            "allowDuplicate": False
        }
    }

    if image_url:
        note["fields"]["Back"] += f'<img src="{image_url}">'

    request_data_add_note = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": note
        }
    }

    response = requests.post("http://localhost:8765", json=request_data_add_note)
    
    if response.status_code == 200:
        result = response.json()
        if result['error'] is None:
            print("Card created successfully with ID:", result['result'])
            return result['result']
        else:
            print("Error creating card:", result['error'])
    else:
        print("Failed to connect to AnkiConnect")
    return None