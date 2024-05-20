import requests
from PIL import Image
from io import BytesIO
import magic

def display_images(image_urls):
    valid_image_urls = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    for idx, url in enumerate(image_urls, 1):
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Проверка на HTTP ошибки
            mime = magic.Magic(mime=True)
            mime_type = mime.from_buffer(response.content)
            
            if mime_type.startswith('image/'):
                if 'svg' in mime_type:
                    print(f"SVG image at {url} cannot be displayed directly in PIL.")
                    valid_image_urls.append(url)
                else:
                    img = Image.open(BytesIO(response.content))
                    img.show(title=f'Image {idx}')
                    valid_image_urls.append(url)
            else:
                print(f"URL {url} не является изображением. MIME type: {mime_type}")
        except (requests.exceptions.RequestException, IOError) as e:
            print(f"Не удалось загрузить изображение {idx} по URL: {url}. Ошибка: {e}")
    
    return valid_image_urls