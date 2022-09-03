"""
    Image Resizer
"""

from PIL import Image


def resize_image(size1, size2):
    image = Image.open('python.jpg')

    print(f'Current size: {image.size}')

    resized_image = image.resize((size1, size2))

    resized_image.save('python_resized.jpg')


size1 = eval(input('Enter width: '))
size2 = eval(input('Enter length: '))

resize_image(size1, size2)
