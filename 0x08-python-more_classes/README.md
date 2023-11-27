# Project Title: More Classes and Objects in Python

## Introduction
This project focuses on advanced tasks related to Python programming, specifically on the topic of Object-Oriented Programming (OOP). The tasks involve creating a class named `Rectangle` and implementing various features such as properties, methods, class attributes, static methods, and class methods. The final task introduces a program to solve the N queens puzzle.

## Project Structure
The project is organized into several tasks, each contained in its respective file within the `0x08-python-more_classes` directory. The tasks are as follows:

1. **0. Simple Rectangle**
   - File: `0-rectangle.py`
   - Description: Defines an empty class `Rectangle`.

2. **1. Real definition of a rectangle**
   - File: `1-rectangle.py`
   - Description: Extends the `Rectangle` class to include private attributes `width` and `height` with corresponding properties and setters.

3. **2. Area and Perimeter**
   - File: `2-rectangle.py`
   - Description: Adds public methods `area` and `perimeter` to calculate the area and perimeter of the rectangle.

4. **3. String representation**
   - File: `3-rectangle.py`
   - Description: Enhances the `Rectangle` class to include a string representation using `print()` and `str()`.

5. **4. Eval is magic**
   - File: `4-rectangle.py`
   - Description: Implements the `__repr__` method to allow recreating instances using `eval()`.

6. **5. Detect instance deletion**
   - File: `5-rectangle.py`
   - Description: Adds a message to be displayed when an instance of `Rectangle` is deleted.

7. **6. How many instances**
   - File: `6-rectangle.py`
   - Description: Adds a class attribute `number_of_instances` to keep track of the number of instances.

8. **7. Change representation**
   - File: `7-rectangle.py`
   - Description: Adds a class attribute `print_symbol` to change the representation character of the rectangle.

9. **8. Compare rectangles**
   - File: `8-rectangle.py`
   - Description: Adds a static method `bigger_or_equal` to compare two rectangles based on area.

10. **9. A square is a rectangle**
    - File: `9-rectangle.py`
    - Description: Adds a class method `square` to create a new `Rectangle` instance with equal width and height.

11. **10. N queens**
    - File: `101-nqueens.py`
    - Description: Implements a program to solve the N queens puzzle using backtracking.

## Usage and Requirements
- All files should be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5.
- The first line of each file should be `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.
- The code should follow the PEP 8 style guide, checked using `pycodestyle` (version 2.8.*).
- All files must be executable.
- The length of files will be tested using `wc`.

## Learning Objectives
By completing this project, the learner is expected to understand the following concepts in Python and OOP:

- Basics of Python programming and why it's awesome.
- Object-Oriented Programming (OOP) principles.
- Classes and instances in Python.
- Attributes (public, protected, private) and methods.
- Special methods such as `__init__`, `__str__`, and `__repr__`.
- Class attributes, class methods, and static methods.
- Dynamically creating new attributes for instances.
- String representation and formatting.
- Handling instance deletion and tracking the number of instances.

## Copyright and Plagiarism
- Content of the project is strictly confidential and should not be published.
- Plagiarism is strictly forbidden and will result in removal from the program.


## Author
- **Author:** Guillaume
- **Contact:** [GitHub Profile](https://github.com/guiferviz)

Copyright © 2023 ALX, All rights reserved.
