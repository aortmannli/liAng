from display import *
from draw import *

class Line:
    def __init__(self, pic, color):
        self.pic = pic
        self.color = color

    def oct1(self, x0, y0, x1, y1):
        if (x0 > x1):
            x0, y0, x1, y1 = x1, y1, x0, y0
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = 2 * A + B
        while (x <= x1):
            plot(self.pic, self.color, int(x), int(y))
            if (d > 0):
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A

    def oct2(self, x0, y0, x1, y1):
        if (y0 > y1):
            x0, y0, x1, y1 = x1, y1, x0, y0
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = A + 2 * B
        while (y <= y1):
            plot(self.pic, self.color, int(x), int(y))
            if (d < 0):
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B

    def oct7(self, x0, y0, x1, y1):
        if (y1 > y0):
            x0, y0, x1, y1 = x1, y1, x0, y0
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = A - 2 * B
        while (y >= y1):
            plot(self.pic, self.color, int(x), int(y))
            if (d > 0):
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B

    def oct8(self, x0, y0, x1, y1):
        if (x0 > x1):
            x0, y0, x1, y1 = x1, y1, x0, y0
        x = x0
        y = y0
        A = y1 - y0
        B = x0 - x1
        d = 2 * A - B
        while (x <= x1):
            plot(self.pic, self.color, int(x), int(y))
            if (d < 0):
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A

def draw_line(x0, y0, x1, y1, s, c):
    L = Line(s,c)
    try:
        m = (y1 - y0) / (x1 - x0)
    except ZeroDivisionError:
        m = 2
    if (1 <= m):
        L.oct2(x0, y0, x1, y1)
    elif (0 <= m < 1):
        L.oct1(x0, y0, x1, y1)
    elif (-1 <= m < 0):
        L.oct8(x0, y0, x1, y1)
    else:
        L.oct7(x0, y0, x1, y1)
            
