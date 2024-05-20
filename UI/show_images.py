import io
import requests
import tkinter as tk
from PIL import Image, ImageTk

def show_images(image_urls):
    win = tk.Tk()
    win.title("Image Viewer")

    for url in image_urls:
        response = requests.get(url)
        img_data = response.content
        img = Image.open(io.BytesIO(img_data))
        img = img.resize((300, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)

        label = tk.Label(win, image=photo)
        label.image = photo
        label.pack()

