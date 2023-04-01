class Rectangle:

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def setWidth(self, width):
        self._width = width

    def setHeight(self, height):
        self._height = height

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def area(self):
        return (self._height*self._width)

    def perimeter(self):
        return 2*(self._width+self._height)

    def __str__(self):
        return ('width is: '+str(self._width)+'\nheight is: '
                + str(self._height))


rectangle01 = Rectangle(width=20, height=30)
print(rectangle01)
print(rectangle01.getHeight())
print(rectangle01.getWidth())
print(rectangle01.area())
print(rectangle01.perimeter())
rectangle01.setHeight(height=10)
rectangle01.setWidth(width=12)
print(rectangle01.area())
print(rectangle01.perimeter())
print(rectangle01.__str__())
