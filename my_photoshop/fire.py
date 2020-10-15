"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original colored image
    :return: (SimpleImage), a gray scaled image with several red spots, representing firing parts.
    """
    img = SimpleImage('images/greenland-fire.png')
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) / 3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel. blue = avg
    return img


def main():
    """
    The codes would convert the original image into a gray scale image, plus pointing out the firing place by red sign.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
