#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
    def size(self):
    """
    This class represents a square and inherits from the Rectangle class.

    Attributes:
    - size (int): The size of the square.

    Methods:
    - __init__(self, size, x=0, y=0, id=None): Initializes
    a new Square instance.
    - size (property): Getter for the size attribute.
    - size (setter): Setter for the size attribute,
    also setting width and height.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int): The size of the square.
        - x (int, optional): The x-coordinate of the square. Default is 0.
        - y (int, optional): The y-coordinate of the square. Default is 0.
        - id (int, optional): The ID of the square. Default is None.

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the square, updating both width and height.

        Parameters:
        - value (int): The new size value.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.

        """
        self.width = value
        self.height = value
