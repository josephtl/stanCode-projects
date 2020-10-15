"""
File: blur.py
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:(SimpleImage), an emoji image.
    :return: A blurred emoji image.
    """
    blank = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            pixel_blank = blank.get_pixel(x, y)
            # upper left corner
            if x == 0 and y == 0:
                pixel_img_lower = img.get_pixel(x, y + 1)
                pixel_img_right = img.get_pixel(x + 1, y)
                pixel_blank.red = (pixel_img_lower.red + pixel_img_right.red)/2
                pixel_blank.green = (pixel_img_lower.green + pixel_img_right.green)/2
                pixel_blank.blue = (pixel_img_lower.blue + pixel_img_right.blue)/2
            # upper right corner
            elif x == img.width-1 and y == 0:
                pixel_img_lower = img.get_pixel(x, y + 1)
                pixel_img_left = img.get_pixel(x-1, y)
                pixel_blank.red = (pixel_img_lower.red + pixel_img_left.red) / 2
                pixel_blank.green = (pixel_img_lower.green + pixel_img_left.green) / 2
                pixel_blank.blue = (pixel_img_lower.blue + pixel_img_left.blue) / 2
            # lower left corner
            elif x == 0 and y == img.height-1:
                pixel_img_upper = img.get_pixel(x, y - 1)
                pixel_img_right = img.get_pixel(x + 1, y)
                pixel_blank.red = (pixel_img_upper.red + pixel_img_right.red) / 2
                pixel_blank.green = (pixel_img_upper.green + pixel_img_right.green) / 2
                pixel_blank.blue = (pixel_img_upper.blue + pixel_img_right.blue) /2
            # lower right corner
            elif x == img.width-1 and y == img.height-1:
                pixel_img_upper = img.get_pixel(x, y - 1)
                pixel_img_left = img.get_pixel(x - 1, y)
                pixel_blank.red = (pixel_img_upper.red + pixel_img_left.red) / 2
                pixel_blank.green = (pixel_img_upper.green + pixel_img_left.green) / 2
                pixel_blank.blue = (pixel_img_upper.blue + pixel_img_left.blue) / 2
            # left border
            elif x == 0 and 0 < y < img.height-1:
                pixel_img_upper = img.get_pixel(x, y - 1)
                pixel_img_lower = img.get_pixel(x, y + 1)
                pixel_img_right = img.get_pixel(x + 1, y)
                pixel_blank.red = (pixel_img_upper.red + pixel_img_lower.red + pixel_img_right.red)/3
                pixel_blank.green = (pixel_img_upper.green + pixel_img_lower.green + pixel_img_right.green)/3
                pixel_blank.blue = (pixel_img_upper.blue + pixel_img_lower.blue + pixel_img_right.blue)/3
            # upper border
            elif 0 < x < img.width-1 and (y == 0):
                pixel_img_lower = img.get_pixel(x, y + 1)
                pixel_img_left = img.get_pixel(x-1, y)
                pixel_img_right = img.get_pixel(x + 1, y)
                pixel_blank.red = (pixel_img_left.red + pixel_img_lower.red + pixel_img_right.red) / 3
                pixel_blank.green = (pixel_img_left.green + pixel_img_lower.green + pixel_img_right.green) / 3
                pixel_blank.blue = (pixel_img_left.blue + pixel_img_lower.blue + pixel_img_right.blue) / 3
            # lower border
            elif 0 < x < img.width-1 and y == img.height-1:
                pixel_img_upper = img.get_pixel(x, y - 1)
                pixel_img_left = img.get_pixel(x - 1, y)
                pixel_img_right = img.get_pixel(x + 1, y)
                pixel_blank.red = (pixel_img_left.red + pixel_img_upper.red + pixel_img_right.red) / 3
                pixel_blank.green = (pixel_img_left.green + pixel_img_upper.green + pixel_img_right.green) / 3
                pixel_blank.blue = (pixel_img_left.blue + pixel_img_upper.blue + pixel_img_right.blue) / 3
            # right border
            elif x == img.width-1 and 0 < y < img.height-1:
                pixel_img_upper = img.get_pixel(x, y - 1)
                pixel_img_left = img.get_pixel(x - 1, y)
                pixel_img_lower = img.get_pixel(x, y + 1)
                pixel_blank.red = (pixel_img_left.red + pixel_img_upper.red + pixel_img_lower.red) / 3
                pixel_blank.green = (pixel_img_left.green + pixel_img_upper.green + pixel_img_lower.green) / 3
                pixel_blank.blue = (pixel_img_left.blue + pixel_img_lower.blue + pixel_img_lower.blue) / 3
            # middle part
            else:
                pixel_img_upper = img.get_pixel(x, y - 1)
                pixel_img_lower = img.get_pixel(x, y + 1)
                pixel_img_left = img.get_pixel(x - 1, y)
                pixel_img_right = img.get_pixel(x + 1, y)
                pixel_img_upper_left = img.get_pixel(x-1, y-1)
                pixel_img_upper_right = img.get_pixel(x+1, y-1)
                pixel_img_lower_left = img.get_pixel(x-1, y+1)
                pixel_img_lower_right = img.get_pixel(x+1, y+1)
                pixel_blank.red = (pixel_img_upper.red + pixel_img_lower.red + pixel_img_left.red + pixel_img_right.red + pixel_img_upper_left.red + pixel_img_lower_left.red + pixel_img_upper_right.red + pixel_img_lower_right.red)/8
                pixel_blank.green = (pixel_img_upper.green + pixel_img_lower.green + pixel_img_left.green + pixel_img_right.green + pixel_img_upper_left.green + pixel_img_lower_left.green + pixel_img_upper_right.green + pixel_img_lower_right.green)/8
                pixel_blank.blue = (pixel_img_upper.blue + pixel_img_lower.blue + pixel_img_left.blue + pixel_img_right.blue + pixel_img_upper_left.blue + pixel_img_lower_left.blue + pixel_img_upper_right.blue + pixel_img_lower_right.blue)/8
    return blank


def main():
    """
    This program could blurred the original image to some extend.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
