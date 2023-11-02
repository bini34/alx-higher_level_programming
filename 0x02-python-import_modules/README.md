# Project 0x02: Python - Import & Modules

## Introduction

Welcome to Project 0x02: Python - Import & Modules. In this project, you will explore the world of Python programming, specifically focusing on the use of import statements and modules. You will learn how to import functions from other files, create your own modules, and work with command line arguments. This project will help you understand the power and flexibility of Python and its modules.

## Project Details

- **Author**: Guillaume
- **Weight**: 1
- **Project Start**: Nov 2, 2023 6:00 AM
- **Project End**: Nov 3, 2023 6:00 AM
- **Checker Release**: Nov 2, 2023 12:00 PM
- **Auto Review**: Will be launched at the deadline

## Learning Objectives

Upon completing this project, you should be able to:

**General**

- Understand why Python programming is awesome.
- Import functions from another file.
- Use imported functions.
- Create a module.
- Use the built-in function `dir()`.
- Prevent code in your script from being executed when imported.
- Use command line arguments with your Python programs.

## Copyright & Plagiarism

**Copyright Notice**: You are reminded that all work submitted for this project must be your own. Plagiarism is strictly forbidden, and any form of plagiarism will result in removal from the program.

## Requirements

**General**

- Allowed editors: vi, vim, emacs.
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Your code should use pycodestyle (version 2.8.*) for style checking.
- All your files must be executable.
- The length of your files will be tested using `wc`.

## Tasks

1. **Import a Simple Function from a Simple File**
   - Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.
   - You have to use the print function with string format to display integers.
   - You have to assign the value `1` to a variable called `a` and the value `2` to a variable called `b`, using two different lines.
   - Your program should print: `<a value> + <b value> = <add(a, b) value>` followed by a new line.
   - You can only use the word `add_0` once in your code.
   - You are not allowed to use `*` for importing or `__import__`.
   - Your code should not be executed when imported.

2. **My First Toolbox!**
   - Write a program that imports functions from the file `calculator_1.py`, performs some mathematical operations, and prints the results.
   - Do not use the `print` function more than 4 times.
   - Assign the value `10` to a variable `a` and the value `5` to a variable `b`, using two different lines.
   - Your program should call each of the imported functions and print the results in the specified format.
   - The word `calculator_1` should be used only once in your file.
   - You are not allowed to use `*` for importing or `__import__`.
   - Your code should not be executed when imported.

3. **How to Make a Script Dynamic!**
   - Write a program that prints the number of and the list of its arguments.
   - The output format should include the number of arguments, followed by "argument" or "arguments," followed by a new line.
   - If there is at least one argument, each argument should be printed on a new line, with its position (starting at 1), followed by a colon, followed by the argument value.
   - Your code should not be executed when imported.
   - The number of arguments can be retrieved using `len(argv`.

4. **Infinite Addition**
   - Write a program that prints the result of the addition of all arguments.
   - The output should be the result of the addition of all arguments, followed by a new line.
   - You can cast arguments into integers using `int()`.
   - Your code should not be executed when imported.
   - Your program should handle big numbers.

5. **Who Are You?**
   - Write a program that prints all the names defined by the compiled module `hidden_4.pyc`.
   - Print one name per line, in alphabetical order.
   - Print only names that do not start with "__".
   - Your code should not be executed when imported.
   - Ensure that you are running your code in Python 3.8.x (the `hidden_4.pyc` has been compiled with this version).

6. **Everything Can Be Imported**
   - Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.
   - You are not allowed to use `*` for importing or `__import__`.
   - Your code should not be executed when imported.

7. **Build My Own Calculator!**
   - Write a program that imports all functions from the file `calculator_1.py` and handles basic operations.
   - Usage: `./100-my_calculator.py a operator b`
   - If the number of arguments is not 3, your program should print an error message and exit with value 1.
   - The operator can be "+", "-", "*", or "/".
   - If the operator is not one of the above, print an error message and exit with value 1.
   - You can cast `a` and `b` into integers using `int()`.
   - Print the result in the specified format.
   - Your code should not be executed when imported.

8. **Easy Print**
   - Write a program that prints `#pythoniscool`, followed by a new line, in the standard output.
   - Your program should be a maximum of 2 lines long.
   - You are not allowed to use `print`, `eval`, `open`, or `import sys` in your file.

9. **ByteCode -> Python #3**
   - Write the Python function `def magic_calculation(a, b):` that performs the same operations as the provided Python bytecode.

10. **Fast Alphabet**
    - Write a program that prints the alphabet in uppercase, followed by a new line.
    - Your program should be a maximum of 3 lines long.
    - You are not allowed to use loops, conditional statements, `str.join()`, string literals, or system calls.

## Conclusion

This project will help you strengthen your understanding of Python's import system, modules, and command-line argument handling. By completing these tasks, you will become more proficient in using Python for various programming challenges and projects. Good luck and enjoy this journey into the world of Python programming!
