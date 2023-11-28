# Project Name

## Python Test-Driven Development

Welcome to the Python Test-Driven Development project! This project focuses on advanced tasks related to test-driven development in Python. It covers various topics, including writing functions, creating unit tests, and working with matrices. The project is designed to enhance your understanding of Python programming and test-driven development principles.

## Project Overview

### Tasks

1. **Integers Addition**
   - Write a function that adds two integers.
   - Ensure proper casting and error handling.
   - Use test cases to validate the implementation.

2. **Divide a Matrix**
   - Write a function that divides all elements of a matrix.
   - Implement error checks for matrix validation.
   - Ensure proper division and rounding to 2 decimal places.

3. **Say My Name**
   - Write a function that prints a formatted name string.
   - Implement error checks for string inputs.

4. **Print Square**
   - Write a function that prints a square with the character '#'.
   - Implement error checks for size validation.

5. **Text Indentation**
   - Write a function that prints a text with 2 new lines after specific characters.
   - Implement error checks for string inputs.

6. **Max Integer - Unittest**
   - Write unit tests for the `max_integer` function.
   - Use the `unittest` module for testing.

7. **Matrix Multiplication**
   - Write a function that multiplies two matrices.
   - Implement extensive validation for matrix inputs.
   - Handle various error scenarios.

8. **Lazy Matrix Multiplication**
   - Write a function that multiplies two matrices using NumPy.
   - Implement error checks similar to the previous task.

9. **CPython #3: Python Strings**
   - Create a function in C that prints Python strings.
   - Ensure proper handling of different string types and display relevant information.

### Project Structure

- **Directory Structure:**
  - `0x07-python-test_driven_development/`
    - `0-add_integer.py`
    - `1-divide_matrix.py`
    - `2-matrix_divided.py`
    - `3-say_my_name.py`
    - `4-print_square.py`
    - `5-text_indentation.py`
    - `6-max_integer.py`
    - `tests/`
      - `0-add_integer.txt`
      - `1-divide_matrix.txt`
      - `2-matrix_divided.txt`
      - `3-say_my_name.txt`
      - `4-print_square.txt`
      - `5-text_indentation.txt`
      - `6-max_integer_test.py`
      - `100-matrix_mul.py`
      - `101-lazy_matrix_mul.py`
      - `102-python.c`
    - `README.md`

### Development Guidelines

- Follow the provided specifications for each task.
- Use the specified editors for Python scripts.
- Ensure compliance with code style using `pycodestyle`.
- Include proper documentation for modules and functions.
- Create a `README.md` file at the root of the project folder.

## Getting Started

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project folder:

   ```bash
   cd 0x07-python-test_driven_development
   ```

3. Start working on the tasks, and have fun!

## How to Run Tests

- To run the tests for a specific task, use the following command:

  ```bash
  python3 -m doctest -v ./tests/<filename>.txt
  ```

- For unit tests, use the following command:

  ```bash
  python3 -m unittest tests.<filename>_test
  ```

## Additional Notes

- Pay attention to error messages and ensure proper error handling.
- Collaborate on test cases to cover all possible scenarios.
- Remember the importance of test-driven development principles.

---

**Note:** This project is part of the ALX Higher Level Programming curriculum. All rights reserved.
