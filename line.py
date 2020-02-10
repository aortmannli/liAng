class Line:
    pic = None
    color = -1

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
            self.pic.set(x, y, self.color)
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
            self.pic.set(x, y, self.color)
            if (d < 0):
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B
