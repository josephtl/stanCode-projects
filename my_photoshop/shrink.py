"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, a original poppy image.
    :return img: (SimpleImage), poppy image be shrank into 1/4 (1/2 * height and 1/2 * width).
    """
    original = SimpleImage('images/poppy.png')
    blank = SimpleImage.blank(original.width//2, original.height//2)
    for y in range(blank.height):
        for x in range(blank.width):
            pixel_orig1 = original.get_pixel(x * 2, y * 2)
            pixel_orig2 = original.get_pixel(x * 2 + 1, y * 2)
            pixel_orig3 = original.get_pixel(x * 2, y * 2 + 1)
            pixel_orig4 = original.get_pixel(x * 2 + 1, y * 2 + 1)
            pixel_blank = blank.get_pixel(x, y)
            pixel_blank.red = (pixel_orig1.red + pixel_orig2.red + pixel_orig3.red + pixel_orig4.red) / 4
            pixel_blank.green = (pixel_orig1.green + pixel_orig2.green + pixel_orig3.green + pixel_orig4.green) / 4
            pixel_blank.blue = (pixel_orig1.blue + pixel_orig2.blue + pixel_orig3.blue + pixel_orig4.blue) / 4
    return blank


def main():
    """
    These codes will shrink the original image into 1/4 size (1/2 * height and 1/2 * width).
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
