import requests

# Функция для запуска загрузки изображений через Batch Download Pictures From Google Images
def trigger_image_download(note_id, field_name="Back"):
    request_data_download_images = {
        "action": "guiBrowse",
        "version": 6,
        "params": {
            "query": f"nid:{note_id}",
            "commands": [
                {
                    "action": "batchDownloadPictures",
                    "params": {
                        "noteIds": [note_id],
                        "field": field_name,
                        "count": 1  # Количество изображений для загрузки
                    }
                }
            ]
        }
    }

    response = requests.post("http://localhost:8765", json=request_data_download_images)
    
    if response.status_code == 200:
        result = response.json()
        if result['error'] is None:
            print(f"Image download triggered successfully for note ID: {note_id}")
        else:
            print("Error triggering image download:", result['error'])
    else:
        print("Failed to connect to AnkiConnect")
