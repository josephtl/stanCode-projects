"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage


def main():
    """
    These codes combined two images, and turn the figure into gray scale.
    After it launched, we could see a suspect taking a photo shoot.
    """
    figure = SimpleImage('image_contest/figure.jpg')
    background = SimpleImage('image_contest/background.jpg')
    result = combine(background, figure)
    result.show()


def combine(background_img, figure_img):
    """
    :param background_img: (SimpleImage), the background image.
    :param figure_img: (SimpleImage), a figure stand in front of a green screen
    :return: (SimpleImage), Combining both images, the background_img will replace all the green part on figure_img,
                            the figure will also turn in to gray scale
    """
    background_img.make_as_big_as(figure_img)
    for y in range(figure_img.height):
        for x in range(figure_img.width):
            background = background_img.get_pixel(x, y)
            figure = figure_img.get_pixel(x, y)
            bigger = max(figure.red, figure.blue)
            avg = (figure.red + figure.green + figure.blue)/3
            if figure.green > bigger + 35:
                figure.red = background.red - 30
                figure.green = background.green - 30
                figure.blue = background.blue - 30
            else:
                figure.red = avg + 55
                figure.green = avg + 55
                figure.blue = avg + 55
    return figure_img


if __name__ == '__main__':
    main()
