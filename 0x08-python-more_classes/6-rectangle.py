#!/usr/bin/python3
"""Creates a class Rectangle"""


class Rectangle:
    """Defines a class Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be an integer")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be an integer")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        for i in range(self.area()):
            if i and not (i % self.__width):
                print()
            print("#", end='')
        return ''

    def __repr__(self):
        string_1 = "Rectangle(" + str(self.__width) + ","
        string_2 = str(self.__height) + ")"

        return string_1 + ' ' + string_2

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
