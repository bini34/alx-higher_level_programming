# Python - Hello, World

**Author:** Guillaume
**Weight:** 1
**Project Start:** Oct 30, 2023 6:00 AM
**Project End:** Oct 31, 2023 6:00 AM
**Checker Release:** Oct 30, 2023 12:00 PM
**Auto Review:** Will be launched at the deadline

### Concepts
For this project, we expect you to look at the concept of **Python programming**.

### Author’s Disclaimer
Welcome to the Python world!

The initial projects are more "C-oriented" - straightforward, no tricky syntax. If you've already worked with Python, don't worry, more exciting tasks are on the way. With Python, there are often multiple ways to do the same thing. Some tasks require only one implementation, while others allow for creativity. Similar to C, Python also has a style guide called PEP8 (now known as PyCode), which you should follow.

Enjoy your Python journey!

- Guillaume

### Resources
Please read or watch:

1. [The Python tutorial](https://docs.python.org/3/tutorial/) (Only the first three chapters)
2. [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
3. [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
4. [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) (Read up until “3.1.2. Strings” included)
5. [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/)
6. [Learn to Program](https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator)
7. [Pycodestyle – Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

### Learning Objectives
By the end of this project, you should be able to explain to anyone without the help of Google:

**General:**
- Why Python programming is awesome
- Who created Python
- Who is Guido van Rossum
- Where the name ‘Python’ comes from
- What is the Zen of Python
- How to use the Python interpreter
- How to print text and variables using print
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with pycodestyle

### Copyright - Plagiarism
You are tasked with coming up with solutions for the tasks to meet the learning objectives mentioned above. Copying and pasting someone else's work is not allowed. You are not allowed to publish any content from this project, and any form of plagiarism is strictly forbidden and will result in removal from the program.

### Requirements
**Python Scripts:**
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file at the root of the folder of this project is mandatory
- Your code should use pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

**Shell Scripts:**
- Allowed editors: vi, vim, emacs
- All your scripts will be tested on Ubuntu 20.04 LTS
- All your scripts should be exactly two lines long (`wc -l file` should print 2)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/bin/bash`
- All your files must be executable

**C Scripts:**
- Allowed editors: vi, vim, emacs
- All your files will be compiled on Ubuntu 20.04 LTS using gcc, using the options `-Wall -Werror -Wextra -pedantic -std=gnu89`
- All your files should end with a new line
- Your code should use the Betty style. It will be checked using `betty-style.pl` and `betty-doc.pl`
- You are not allowed to use global variables
- No more than 5 functions per file
- The prototypes of all your functions should be included in your header file called `lists.h`
- Don’t forget to push your header file
- All your header files should be include guarded

### More Info
**Zen:**
The Zen of Python, by Tim Peters

1. Beautiful is better than ugly.
2. Explicit is better than implicit.
3. Simple is better than complex.
4. Complex is better than complicated.
5. Flat is better than nested.
6. Sparse is better than dense.
7. Readability counts.
8. Special cases aren't special enough to break the rules.
9. Although practicality beats purity.
10. Errors should never pass silently.
11. Unless explicitly silenced.
12. In the face of ambiguity, refuse the temptation to guess.
13. There should be one-- and preferably only one --obvious way to do it.
14. Although that way may not be obvious at first unless you're Dutch.
15. Now is better than never.
16. Although never is often better than *right* now.
17. If the implementation is hard to explain, it's a bad idea.
18. If the implementation is easy to explain, it may be a good idea.
19. Namespaces are one honking great idea -- let's do more of those!

**Pycodestyle:**
Pycodestyle is now the new standard of Python style code

---

## Tasks
### 0. Run Python file (Mandatory)

**Shell Script: 0-run**

Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

### 1. Run inline (Mandatory)

**Shell Script: 1-run_inline**

Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

### 2. Hello, print (Mandatory)

**Python Script: 2-print.py**

Write a Python script that prints exactly "Programming is like building a multilingual puzzle," followed by a new line.

Use the `print` function.

### 3. Print integer (Mandatory)

**Python Script: 3-print_number.py**

Complete this source code in order to print the integer stored in the variable `number`, followed by "Battery street," followed by a new line.

The output of the script should be:
```
the number, followed by Battery street,
followed by a new line
```
You are not allowed to cast the variable `number` into a string.
Your code must be 3 lines long.
You have to use f-strings.

### 4. Print float (Mandatory)

**Python Script: 4-print_float.py**

Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.

The output of the program should be:
```


Float:, followed by the float with only 2 digits
followed by a new line
```
You are not allowed to cast `number` to a string.
You have to use f-strings.

### 5. Print string (Mandatory)

**Python Script: 5-print_string.py**

Complete this source code in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

The output of the program should be:
```
3 times the value of str
followed by a new line
followed by the 9 first characters of str
followed by a new line
```
You are not allowed to use any loops or conditional statements.
Your program should be a maximum of 5 lines long.

### 6. Play with strings (Mandatory)

**Python Script: 6-concat.py**

Complete this source code to print "Welcome to Holberton School!"

You are not allowed to use any loops or conditional statements.
You have to use the variables `str1` and `str2` in your new line of code.
Your program should be exactly 5 lines long.

### 7. Copy - Cut - Paste (Mandatory)

**Python Script: 7-edges.py**

Complete this source code.

You are not allowed to use any loops or conditional statements.
Your program should be exactly 8 lines long.
`word_first_3` should contain the first 3 letters of the variable `word`.
`word_last_2` should contain the last 2 letters of the variable `word`.
`middle_word` should contain the value of the variable `word` without the first and last letters.

### 8. Create a new sentence (Mandatory)

**Python Script: 8-concat_edges.py**

Complete this source code to print "object-oriented programming with Python," followed by a new line.

You are not allowed to use any loops or conditional statements.
Your program should be exactly 5 lines long.
You are not allowed to create new variables.
You are not allowed to use string literals.

### 9. Easter Egg (Mandatory)

**Python Script: 9-easter_egg.py**

Write a Python script that prints "The Zen of Python," by Tim Peters, followed by a new line.

Your script should be a maximum of 98 characters long (please check with `wc -m 9-easter_egg.py`).

### 10. Linked list cycle (Mandatory)

**C Function: check_cycle**

Write a function in C that checks if a singly linked list has a cycle in it.

**Prototype:**
```c
int check_cycle(listint_t *list);
```

**Return:**
- 0 if there is no cycle
- 1 if there is a cycle

**Requirements:**
- Only these functions are allowed: write, printf, putchar, puts, malloc, free

### 11. Hello, write (Advanced)

**Python Script: 100-write.py**

Write a Python script that prints exactly "and that piece of art is useful - Dora Korpar, 2015-10-19," followed by a new line.

Use the function `write` from the sys module.
You are not allowed to use `print`.
Your script should print to stderr.
Your script should exit with the status code 1.

### 12. Compile (Advanced)

**Shell Script: 101-compile**

Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE.
The output filename has to be $PYFILEc (e.g., export PYFILE=my_main.py => output filename: my_main.pyc).

### 13. ByteCode -> Python #1 (Advanced)

**Python Function: magic_calculation(a, b)**

Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:

```
  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
```

---

**Copyright © 2023 ALX, All rights reserved.**
