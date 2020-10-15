"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: (SimpleImage), the background image.
    :param figure_img: (SimpleImage), an actress stand in front of a green screen
    :return: (SimpleImage), Combining both images, the background_img will replace
                            all the green part on figure_img.
    """
    for y in range(figure_img.height):
        for x in range(figure_img.width):
            background = background_img.get_pixel(x, y)
            figure = figure_img.get_pixel(x, y)
            bigger = max(figure.red, figure.blue)
            if figure.green > bigger * 2:
                figure.red = background.red
                figure.green = background.green
                figure.blue = background.blue
    return figure_img


def main():
    """
    This program would combine two images, with background image replacing the green part of figure image.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
