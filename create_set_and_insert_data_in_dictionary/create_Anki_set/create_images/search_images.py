import requests
import tkinter as tk
from PIL import Image, ImageTk

def search_images(query, num=5):
    search_url = "https://www.googleapis.com/customsearch/v1"
    image_urls = set()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    for start in range(1, num + 1, 10):
        params = {
            "q": query,
            "cx": '80e9308b5e3a34198',
            "key": 'AIzaSyBMFqihg1pOubMsBCX-59m1rg51P2eQSfo',
            "searchType": "image",
            "num": min(num - len(image_urls), 10),
            "start": start
        }
        response = requests.get(search_url, params=params, headers=headers)
        response.raise_for_status()
        results = response.json()
        image_urls.update(item["link"] for item in results.get("items", []))

        if "items" not in results:
            break

    return image_urls