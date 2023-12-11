#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """
    This class represents a rectangle and inherits from the Base class.

    Attributes:
    - __width (int): The width of the rectangle.
    - __height (int): The height of the rectangle.
    - __x (int): The x-coordinate of the rectangle.
    - __y (int): The y-coordinate of the rectangle.

    Methods:
    - area(): Calculates and returns the area of the rectangle.
    - display(): Displays the rectangle using '#' characters.
    - __str__(): Returns a string representation of the rectangle.
    - update(*args, **kwargs): Updates the attributes of the rectangle.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        - x (int, optional): The x-coordinate of the rectangle. Default is 0.
        - y (int, optional): The y-coordinate of the rectangle. Default is 0.
        - id (int, optional): The ID of the rectangle. Default is None.

        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Parameters:
        - value (int): The new width value.

        Raises:
        - TypeError: If the value is not an integer.
        - ValueError: If the value is less than or equal to 0.

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Repeat similar documentation for height, x, and y properties and setters...

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        - int: The area of the rectangle.

        """
        return self.height * self.width

    def display(self):
        """
        Display the rectangle using '#' characters.

        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
        - str: A string representation of the rectangle.

        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Parameters:
        - *args: Positional arguments, where the first argument is the ID.
        - **kwargs: Keyword arguments for updating specific attributes.

        """
        if args:
            self.id = args[0]
        if "width" in kwargs:
            self.width = kwargs["width"]
        if "height" in kwargs:
            self.height = kwargs["height"]
        if "x" in kwargs:
            self.x = kwargs["x"]
        if "y" in kwargs:
            self.y = kwargs["y"]
