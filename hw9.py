class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.lt = Point(x1, y1)
        self.rb = Point(x2, y2)

    def show(self):
        print(f"Left-Top: {self.lt}, Right-Bottom: {self.rb}")

    def getWidth(self):
        return abs(self.rb.x - self.lt.x)

    def getHeight(self):
        return abs(self.rb.y - self.lt.y)

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2 * (self.getWidth() + self.getHeight())


# 테스트 코드
if __name__ == "__main__":
    r1 = Rectangle(5, 5, 20, 10)
    a = r1.getArea()
    p = r1.getPerimeter()
    r1.show()
    print(f'\n넓이는 {a}, 둘레는 {p}')
