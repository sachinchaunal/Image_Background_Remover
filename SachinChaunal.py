# package required to run this code
# pip install requests rembg Pillow
# pip install --upgrade rembg


import requests
from rembg import remove, new_session
from PIL import Image
from io import BytesIO


def download_image(url):
    response = requests.get(url)
    response.raise_for_status()  
    image = Image.open(BytesIO(response.content))
    return image

def remove_background(input_image, output_image_path, model_name='u2net'):
    session = new_session(model_name)
    output_image = remove(input_image, session=session)
    output_image.save(output_image_path, format='PNG')

if __name__ == "__main__":
    image_url = 'https://i.pinimg.com/originals/ba/15/c0/ba15c084715c971446588c57a8d14e46.jpg'
    output_path = 'output_image.png'
    input_image = download_image(image_url)
    remove_background(input_image, output_path, model_name='u2net_human_seg')
    print("Background removal complete. Check the output image.")