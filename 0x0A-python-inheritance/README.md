# Project Title: 0x0A. Python - Inheritance

## Table of Contents
1. [Description](#description)
2. [Learning Objectives](#learning-objectives)
3. [Requirements](#requirements)
4. [Tasks](#tasks)
    - [Task 0: Lookup](#task-0-lookup)
    - [Task 1: My List](#task-1-my-list)
    - [Task 2: Exact Same Object](#task-2-exact-same-object)
    - [Task 3: Same Class or Inherit From](#task-3-same-class-or-inherit-from)
    - [Task 4: Only Sub Class Of](#task-4-only-sub-class-of)
    - [Task 5: Geometry Module](#task-5-geometry-module)
    - [Task 6: Improve Geometry](#task-6-improve-geometry)
    - [Task 7: Integer Validator](#task-7-integer-validator)
    - [Task 8: Rectangle](#task-8-rectangle)
    - [Task 9: Full Rectangle](#task-9-full-rectangle)
    - [Task 10: Square #1](#task-10-square-1)
    - [Task 11: Square #2](#task-11-square-2)
    - [Task 12: My Integer](#task-12-my-integer)
    - [Task 13: Can I?](#task-13-can-i)
5. [Copyright](#copyright)

## Description
This project focuses on understanding and implementing concepts related to Python programming, Object-Oriented Programming (OOP), and Inheritance. The tasks involve creating Python scripts, classes, and functions to meet specific learning objectives.

## Learning Objectives
Upon completion of this project, you should be able to:
- Explain why Python programming is awesome.
- Understand the concepts of superclass, base class, or parent class.
- Define and use subclasses.
- List attributes and methods of a class or instance.
- Inherit a class from another and handle multiple base classes.
- Override methods or attributes inherited from a base class.
- Utilize built-in functions like isinstance, issubclass, type, and super.
- Implement proper documentation for Python code.
- Handle exceptions and raise errors as needed.

## Requirements
### Python Scripts
- Allowed editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- Files should end with a new line
- The first line of all files should be `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should follow the PEP 8 style guide (use pycodestyle version 2.8.*)
- All files must be executable
- The length of files will be tested using wc
### Python Test Cases
- Allowed editors: vi, vim, emacs
- Test files should end with a new line
- All test files should be inside a folder named "tests"
- Test files should be text files with the extension .txt
- Tests should be executed using the command: `python3 -m doctest ./tests/*`
- Modules, classes, and functions should have proper documentation
- Documentation is not a single word; it should be a sentence explaining the purpose of the module, class, or method

## Tasks

### Task 0: Lookup
Write a function that returns the list of available attributes and methods of an object.

```python
def lookup(obj):
    """
    Returns a list object
    """
```

### Task 1: My List
Write a class `MyList` that inherits from `list`. Implement a public instance method `print_sorted(self)` that prints the list in ascending order.

```python
class MyList(list):
    """
    MyList class inherits from list
    """

    def print_sorted(self):
        """
        Prints the list in ascending order
        """
```

### Task 2: Exact Same Object
Write a function `is_same_class(obj, a_class)` that returns True if the object is exactly an instance of the specified class; otherwise False.

```python
def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise False
    """
```

### Task 3: Same Class or Inherit From
Write a function `is_kind_of_class(obj, a_class)` that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.

```python
def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False
    """
```

### Task 4: Only Sub Class Of
Write a function `inherits_from(obj, a_class)` that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.

```python
def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False
    """
```

### Task 5: Geometry Module
Write an empty class `BaseGeometry`.

```python
class BaseGeometry:
    """
    Empty class BaseGeometry
    """
```

### Task 6: Improve Geometry
Improve the `BaseGeometry` class by adding a public instance method `area(self)` that raises an Exception with the message "area() is not implemented."

```python
class BaseGeometry:
    """
    Improved BaseGeometry class with an area() method
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented"
        """
```

### Task 7: Integer Validator
Write a class `BaseGeometry` with a public instance method `integer_validator(self, name, value)` that validates the value as follows:
- Raises a TypeError exception if the value is not an integer.
- Raises a ValueError exception if the value is less than or equal to 0.

```python
class BaseGeometry:
    """
    BaseGeometry class with an integer_validator method
    """

    def integer_validator(self, name, value):
        """
        Validates the value:
        - Raises a TypeError exception if the value is not an integer.
        - Raises a ValueError exception if the value is less than or equal to 0.
        """
```

### Task 8: Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry`. Implement instantiation with width and height, where width and height must be private positive integers validated by `integer_validator`.

```python
class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiates a Rectangle with width and height
        """
```

### Task 9: Full Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` and includes instantiation with width and height, a validated area() method, and a custom str() method for a descriptive rectangle representation.

```python
class Rectangle(BaseGeometry):
    """
    Full Rectangle class inherits from BaseGeometry with custom

 methods
    """

    def __init__(self, width, height):
        """
        Instantiates a Rectangle with width and height
        """

    def __str__(self):
        """
        Returns a string representation of the rectangle
        """
```

### Task 10: Square #1
Write a class `Square` that inherits from `Rectangle` and implements instantiation with a size. Size must be a private positive integer validated by `integer_validator`.

```python
class Square(Rectangle):
    """
    Square class inherits from Rectangle
    """

    def __init__(self, size):
        """
        Instantiates a Square with a size
        """
```

### Task 11: Square #2
Write a class `Square` that inherits from `Rectangle` and includes instantiation with size, a validated area() method, and a custom str() method for a descriptive square representation.

```python
class Square(Rectangle):
    """
    Square class inherits from Rectangle with custom methods
    """

    def __init__(self, size):
        """
        Instantiates a Square with a size
        """

    def __str__(self):
        """
        Returns a string representation of the square
        """
```

### Task 12: My Integer (Advanced)
Write a class `MyInt` that inherits from `int` and inverts the == and != operators.

```python
class MyInt(int):
    """
    MyInt class inherits from int with inverted == and != operators
    """
```

### Task 13: Can I? (Advanced)
Write a function `add_attribute(obj, name, value)` that adds a new attribute to an object if it’s possible. Raise a TypeError exception if the object can't have a new attribute.

```python
def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible
    Raises a TypeError exception if the object can't have a new attribute
    """
```

## Copyright
© 2023 ALX, All rights reserved.
