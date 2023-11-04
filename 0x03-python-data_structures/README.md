# Python - Data Structures: Lists, Tuples

## Project Information

- **Project Name:** Python - Data Structures: Lists, Tuples
- **Author:** Guillaume
- **Project Weight:** 1
- **Project Start Date:** November 3, 2023, 6:00 AM
- **Project End Date:** November 7, 2023, 6:00 AM
- **Checker Release Date:** November 4, 2023, 6:00 AM

## Project Overview

Welcome to the Python - Data Structures: Lists, Tuples project! In this project, you will be working on Python data structures, specifically lists and tuples. You will learn how to manipulate these data structures and perform various tasks to improve your Python programming skills.

### Learning Objectives

By the end of this project, you are expected to be able to explain the following concepts to anyone without the need for external resources:

**General:**
- Why Python programming is awesome

**Lists:**
- What lists are and how to use them
- Differences and similarities between strings and lists
- Most common methods of lists and how to use them
- How to use lists as stacks and queues
- List comprehensions and how to use them

**Tuples:**
- What tuples are and how to use them
- When to use tuples versus lists
- What is a sequence
- Tuple packing and sequence unpacking
- The `del` statement and how to use it

**Copyright - Plagiarism:**
- You are responsible for coming up with solutions for the project tasks yourself.
- Copying and pasting someone else's work is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

- **Allowed Editors:** vi, vim, emacs
- **Interpreted/Compiled On:** Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- **Files:** All your files should end with a new line.
- **First Line of All Files:** The first line of all your files should be exactly `#!/usr/bin/python3`.
- **README.md:** A README.md file at the root of the project folder is mandatory.
- **Code Style:** Your code should use the pycodestyle (version 2.8.*).
- **File Executability:** All your files must be executable.
- **File Length:** The length of your files will be tested using the `wc` command.

### C

- **Allowed Editors:** vi, vim, emacs
- **Interpreted/Compiled On:** Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- **Files:** All your files should end with a new line.
- **Code Style:** Your code should use the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`.
- **Global Variables:** You are not allowed to use global variables.
- **Functions per File:** No more than 5 functions per file.
- **Header Files:** The prototypes of all your functions should be included in your header file called `lists.h`.
- **Header File Push:** Don’t forget to push your header file.
- **Header File Guards:** All your header files should be include guarded.

## Task List

1. **Print a List of Integers**
   - Write a function that prints all integers of a list.
   - Prototype: `def print_list_integer(my_list=[]):`
   - Format: One integer per line.
   - You are not allowed to import any module.
   - You can assume that the list only contains integers.
   - You are not allowed to cast integers into strings.
   - Use `str.format()` to print integers.

2. **Secure Access to an Element in a List**
   - Write a function that retrieves an element from a list like in C.
   - Prototype: `def element_at(my_list, idx):`
   - If idx is negative, the function should return `None`.
   - If idx is out of range (greater than the number of elements in `my_list`), the function should return `None`.
   - You are not allowed to import any module.
   - You are not allowed to use try/except.

3. **Replace Element**
   - Write a function that replaces an element of a list at a specific position like in C.
   - Prototype: `def replace_in_list(my_list, idx, element):`
   - If idx is negative, the function should not modify anything and should return the original list.
   - If idx is out of range (greater than the number of elements in `my_list`), the function should not modify anything and should return the original list.
   - You are not allowed to import any module.
   - You are not allowed to use try/except.

4. **Print a List of Integers... in Reverse!**
   - Write a function that prints all integers of a list in reverse order.
   - Prototype: `def print_reversed_list_integer(my_list=[]):`
   - Format: One integer per line.
   - You are not allowed to import any module.
   - You can assume that the list only contains integers.
   - You are not allowed to cast integers into strings.
   - Use `str.format()` to print integers.

5. **Replace in a Copy**
   - Write a function that replaces an element in a list at a specific position without modifying the original list, similar to C.
   - Prototype: `def new_in_list(my_list, idx, element):`
   - If idx is negative, the function should return a copy of the original list.
   - If idx is out of range (greater than the number of elements in `my_list`), the function should return a copy of the original list.
   - You are not allowed to import any module.
   - You are not allowed to use try/except.

6. **Can You C Me Now?**
   - Write a function that removes all characters 'c' and 'C' from a string.
   - Prototype: `def no_c(my_string):`
   - The function should return the new string.
   - You are not allowed to import any module.
   - You are not allowed to use `str.replace()`.

7. **Lists of Lists = Matrix**
   - Write a function that prints a matrix of integers.
   - Prototype: `def print_matrix_integer(matrix=[[]]):`
   - Format: See example.
   - You are not allowed to import any module.
   - You can assume that the list only contains integers.
   - You are not allowed to cast integers into strings.
   - Use `str.format()` to print integers.

8. **Tuples Addition**
   - Write a function that adds 2 tuples.
   - Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
   - Returns a tuple with 2 integers:
     - The first element should be the addition of the first element of each argument.
     - The second element should be the addition of the second element of each argument.
   - You are not allowed to import any module.
   - You can assume that the two tuples will only contain integers.
   - If a tuple is smaller than 2, use the value 0 for each missing integer.
   - If a tuple is bigger than 2, use only the first 
