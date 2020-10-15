"""
File: my_drawing.py
Name: Joseph Liu
----------------------
It will shows a character called Zion.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine, GPolygon
from campy.graphics.gwindow import GWindow

window = GWindow(width=700, height=500, title='rick and morty')


def main():
    """
    I'm drawing a painful boy whose name is Zion,
    he was suffering from doing the programming homework and burst into tears.
    Poor Zion.
    """
    zion()


def zion():
    background = GRect(1000, 1000)
    background.filled = True
    window.add(background)
    codes()
    zion_ear()
    zion_head()
    zion_hair()
    zion_eyes()
    nose = GOval(65, 35, x=435, y=270)
    window.add(nose)
    zion_eyebrow()
    zion_mouth()
    zion_tears()
    zion_body()


def zion_ear():
    """
    zion's ears, each made by an oval.
    """
    # left ear
    left_ear = GOval(60, 120, x=260, y=170)
    left_ear.filled = True
    left_ear.fill_color = 'blue'
    window.add(left_ear)
    # right ear
    right_ear = GOval(60, 120, x=620, y=180)
    right_ear.filled = True
    right_ear.fill_color = 'blue'
    window.add(right_ear)


def zion_head():
    """
    zion's head, composed by two big ovals.
    """
    head1 = GOval(350, 250, x=300, y=50)
    head1.filled = True
    head1.fill_color = 'blue'
    head1.color = 'blue'
    window.add(head1)
    head2 = GOval(375, 300, x=280, y=175)
    head2.color = 'blue'
    head2.filled = True
    head2.fill_color = 'blue'
    window.add(head2)


def zion_hair():
    """
    zion's hair, made by a polygon.
    """
    hair = GPolygon()
    hair.add_vertex((310, 250))
    hair.add_vertex((290, 180))
    hair.add_vertex((330, 90))
    hair.add_vertex((350, 80))
    hair.add_vertex((370, 70))
    hair.add_vertex((390, 60))
    hair.add_vertex((410, 50))
    hair.add_vertex((475, 40))
    hair.add_vertex((540, 50))
    hair.add_vertex((560, 60))
    hair.add_vertex((580, 70))
    hair.add_vertex((600, 80))
    hair.add_vertex((625, 90))
    hair.add_vertex((660, 190))
    hair.add_vertex((630, 250))
    hair.add_vertex((590, 120))
    hair.add_vertex((570, 150))
    hair.add_vertex((550, 100))
    hair.add_vertex((510, 150))
    hair.add_vertex((470, 100))
    hair.add_vertex((430, 150))
    hair.add_vertex((400, 110))
    hair.add_vertex((370, 150))
    hair.add_vertex((340, 110))
    hair.filled = True
    hair.fill_color = 'darkslategray'
    window.add(hair)


def zion_eyes():
    """
    zion's eyes, made by several ovals and two lines in each eyes.
    """
    # left eye
    left_eye1 = GOval(70, 70, x=365, y=205)
    window.add(left_eye1)
    left_eye1.filled = True
    left_eye1.fill_color = 'skyblue'
    left_eye2 = GOval(20, 40, x=390, y=220)
    window.add(left_eye2)
    left_eye3 = GOval(3, 6, x=398, y=238)
    window.add(left_eye3)
    left_eye3.filled = True
    left_eye3.fill_color = 'black'
    left_eye4 = GLine(382, 209, 381, 270)
    window.add(left_eye4)
    left_eye5 = GLine(418, 209, 418, 270)
    window.add(left_eye5)
    # right eye
    right_eye1 = GOval(70, 70, x=500, y=205)
    window.add(right_eye1)
    right_eye1.filled = True
    right_eye1.fill_color = 'skyblue'
    right_eye2 = GOval(20, 40, x=525, y=220)
    window.add(right_eye2)
    right_eye3 = GOval(3, 6, x=533, y=238)
    window.add(right_eye3)
    right_eye3.filled = True
    right_eye3.fill_color = 'black'
    right_eye4 = GLine(516, 209, 516, 270)
    window.add(right_eye4)
    right_eye5 = GLine(552, 209, 552, 270)
    window.add(right_eye5)


def zion_mouth():
    """
    a mouth made by oval, and a tongue within it, which also made by ovals.
    """
    # mouth
    mouth = GOval(170, 80, x=385, y=325)
    window.add(mouth)
    mouth.filled = True
    mouth.fill_color = 'navy'
    # tongue, consist of two piece of ovals
    tongue1 = GOval(100, 40, x=435, y=360)
    tongue1.filled = True
    tongue1.color='darkcyan'
    tongue1.fill_color = 'darkcyan'
    window.add(tongue1)
    tongue2 = GOval(105, 40, x=415, y=360)
    tongue2.filled = True
    tongue2.color='darkcyan'
    tongue2.fill_color = 'darkcyan'
    window.add(tongue2)


def zion_eyebrow():
    """
    zion's eyebrows, two polygons.
    """
    # left eyebrow
    left_eyebrow = GPolygon()
    left_eyebrow.add_vertex((380, 155))
    left_eyebrow.add_vertex((400, 160))
    left_eyebrow.add_vertex((440, 210))
    left_eyebrow.add_vertex((430, 200))
    left_eyebrow.add_vertex((400, 165))
    left_eyebrow.filled = True
    left_eyebrow.fill_color = 'black'
    window.add(left_eyebrow)
    # right eyebrow
    right_eyebrow = GPolygon()
    right_eyebrow.add_vertex((550, 155))
    right_eyebrow.add_vertex((530, 160))
    right_eyebrow.add_vertex((490, 210))
    right_eyebrow.add_vertex((500, 200))
    right_eyebrow.add_vertex((530, 165))
    right_eyebrow.filled = True
    right_eyebrow.fill_color = 'black'
    window.add(right_eyebrow)


def zion_tears():
    """
    zion's tears, consist of 6 ovals.
    """
    # four long tears
    tears1 = GOval(5, 100, x= 380,y=280)
    window.add(tears1)
    tears1.color = 'lightcyan'
    tears1.filled= True
    tears1.fill_color='lightcyan'
    tears2 = GOval(5, 100, x=560, y=260)
    window.add(tears2)
    tears2.color = 'lightcyan'
    tears2.filled = True
    tears2.fill_color = 'lightcyan'
    tears3 = GOval(5, 80, x=375, y=350)
    window.add(tears3)
    tears3.color = 'lightcyan'
    tears3.filled = True
    tears3.fill_color = 'lightcyan'
    tears4 = GOval(5, 80, x=565, y=330)
    window.add(tears4)
    tears4.color = 'lightcyan'
    tears4.filled = True
    tears4.fill_color = 'lightcyan'
    # two round tears
    tears5 = GOval(20, 10, x=370, y=265)
    window.add(tears5)
    tears5.color = 'lightcyan'
    tears5.filled = True
    tears5.fill_color = 'lightcyan'
    tears6 = GOval(20, 10, x=550, y=255)
    window.add(tears6)
    tears6.color = 'lightcyan'
    tears6.filled = True
    tears6.fill_color = 'lightcyan'


def zion_body():
    """
    zion's body, made by a polygon.
    """
    body = GPolygon()
    body.add_vertex((180, 500))
    body.add_vertex((190, 490))
    body.add_vertex((200, 481))
    body.add_vertex((210, 473))
    body.add_vertex((220, 466))
    body.add_vertex((230, 460))
    body.add_vertex((240, 455))
    body.add_vertex((250, 451))
    body.add_vertex((260, 448))
    body.add_vertex((270, 446))
    body.add_vertex((280, 445))
    body.add_vertex((700, 440))
    body.add_vertex((800, 500))
    body.filled = True
    body.fill_color = 'blue'
    window.add(body)


def codes():
    """
    several labels representing codes on the background.
    """
    codes1 = GLabel('def main( ):', x=40, y=105)
    codes1.font = '-60'
    codes1.color = 'white'
    window.add(codes1)
    codes1 = GLabel('algorithm', x=10, y=300)
    codes1.font = '-60'
    codes1.color = 'white'
    window.add(codes1)
    codes1 = GLabel('for i in range( ):', x=100, y=230)
    codes1.font = '-50'
    codes1.color = 'white'
    window.add(codes1)
    codes1 = GLabel('for j in range( )', x=552, y=33)
    codes1.font = '-20'
    codes1.color = 'white'
    window.add(codes1)
    codes1 = GLabel('print( )', x=38, y=500)
    codes1.font = '-30'
    codes1.color = 'white'
    window.add(codes1)
    codes1 = GLabel('return:', x=50, y=380)
    codes1.font = '-50'
    codes1.color = 'green'
    window.add(codes1)
    codes1 = GLabel('error:', x=90, y=180)
    codes1.font = '-40'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('Karel', x=560, y=90)
    codes1.font = '-60'
    codes1.color = 'white'
    window.add(codes1)
    codes1 = GLabel('move( )', x=343, y=131)
    codes1.font = '-50'
    codes1.color = 'white'
    window.add(codes1)
    codes1 = GLabel('put_beeper( )', x=559, y=409)
    codes1.font = '-50'
    codes1.color = 'white'
    window.add(codes1)
    codes1 = GLabel('unexpected indent', x=30, y=150)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('put_beeper( )', x=180, y=330)
    codes1.font = '-40'
    codes1.color = 'white'
    window.add(codes1)
    codes1 = GLabel('elif', x=390, y=30)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('else:', x=340, y=55)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('if', x=320, y=35)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('print', x=497, y=188)
    codes1.font = '-20'
    codes1.color = 'white'
    window.add(codes1)
    codes1 = GLabel('int', x=700, y=173)
    codes1.font = '-50'
    codes1.color = 'white'
    window.add(codes1)
    codes1 = GLabel('line 21', x=245, y=440)
    codes1.font = '-20'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('line 34', x=630, y=130)
    codes1.font = '-20'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('IndentationError:', x=528, y=290)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('SyntaxError:', x=88, y=460)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('TypeError:', x=150, y=400)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('invalid syntax', x=5, y=40)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('not', x=20, y=470)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('is', x=20, y=400)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('and', x=20, y=20)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('while', x=10, y=200)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('True', x=100, y=320)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel('False', x=450, y=30)
    codes1.font = '-30'
    codes1.color = 'red'
    window.add(codes1)
    codes1 = GLabel(':param:', x=200, y=30)
    codes1.font = '-30'
    codes1.color = 'green'
    window.add(codes1)
    codes1 = GLabel('img.get_pixel(x,y)', x=10, y=430)
    codes1.font = '-30'
    codes1.color = 'white'
    window.add(codes1)
    codes1 = GLabel('debugger', x=10, y=250)
    codes1.font = '-30'
    codes1.color = 'green'
    window.add(codes1)


if __name__ == '__main__':
    main()
