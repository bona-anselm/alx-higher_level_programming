#!/usr/bin/python3
"""
    The class square does not have any module import
"""


class Square:
    """
        This class defines a square
    """

    def __init__(self, size = None):
        """
            Used to initialize attributes of the instances 
            class Square

            :param size: size of the square
        """
        self.__size = size

    def set_size(self, size):
        """
            Sets the value for size

            :param size: size of the square

            :returns: Nothing
        """
        self.__size = size

    def get_size(self):
        """
            Gets the size of the square

            :returns: size of square
            :rtype: Square
        """
        return self.__size
