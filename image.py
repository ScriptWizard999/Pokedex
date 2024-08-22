from PIL import Image
import os

def show_pokemon_image(name):
    image_path=f"image\Pokemon imagefile/{name.lower()}.png"
    if os.path.exists(image_path):
        img = Image.open(image_path)
        img.show()
    else:
        print(f"No image found for {name}")