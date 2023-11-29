# Project 0x09. Python - Everything is object

## Background Context

Now that we understand that everything is an object and have a little bit of knowledge, let’s pause and look a little bit closer at how Python works with different types of objects.

BTW, have you ever modified a variable without knowing it or wanting to? I mean:

```python
>>> a = 1
>>> b = a
>>> a = 2
>>> b
1
```

OK. But what about this?

```python
>>> l = [1, 2, 3]
>>> m = l
>>> l[0] = 'x'
>>> m
['x', 2, 3]
```

This project is a little bit different than the usual projects. The first part is only questions about Python’s specificity like “What would be the result of…”. You should read all documentation first (as usual :)), then take the time to think and brainstorm with your peers about what you think and why. Try to do this without coding anything for a few hours.

Trying examples in the Python interpreter will give you most of the answers without having to think about it. Don’t go this route. First read, then think, then brainstorm together. Only then you can test in the interpreter.

It’s important that you truly understand the reasons behind the answers to all those tasks so that you can apply the same logic to other variables and other variable types.

Note that during interviews for Python positions, you will most likely have to answer to these types of questions.

All your answers should be only one line in a file. No space before or after the answer.

## Resources
Read or watch:
- [9.10. Objects and values](https://docs.python.org/3.8/reference/datamodel.html#objects-values)
- [9.11. Aliasing](https://docs.python.org/3.8/reference/datamodel.html#objects-values)
- [Immutable vs mutable types](https://docs.python.org/3.8/reference/datamodel.html#objects-values)
- [Mutation (Only this chapter)](https://docs.python.org/3.8/reference/datamodel.html#objects-values)
- [9.12. Cloning lists](https://docs.python.org/3.8/reference/datamodel.html#objects-values)
- [Python tuples: immutable but potentially changing](https://docs.python.org/3.8/reference/datamodel.html#objects-values)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between an immutable object and a mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

## Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet the above learning objectives. You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work. You are not allowed to publish any content of this project. Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a newline character
- The first line of all your script files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

### .txt Answer Files
- Only one line
- No Shebang
- All your files should end with a newline character

## Tasks

### 0. Who am I?
**File:** `0-answer.txt`

What function would you use to get the type of an object?

Write the name of the function in the file, without ().

### 1. Where are you?
**File:** `1-answer.txt`

How do you get the variable identifier (which is the memory address in the CPython implementation)?

Write the name of the function in the file, without ().

### 2. Right count
**File:** `2-answer.txt`

In the following code, do `a` and `b` point to the same object? Answer with Yes or No.

```python
>>> a = 89
>>> b = 100
```

### 3. Right count =
**File:** `3-answer.txt`

In the following code, do `a` and `b` point to the same object? Answer with Yes or No.

```python
>>> a = 89
>>> b = 89
```

### 4. Right count =
**File:** `4-answer.txt`

In the following code, do `a` and `b` point to the same object? Answer with Yes or No.

```python
>>> a = 89
>>> b = a
```
### 5. Right count =+
**File:** `5-answer.txt`

In the following code, do `a` and `b` point to the same object? Answer with Yes or No.

```python
>>> a = 89
>>> b = a + 1
```

### 6. Is equal
**File:** `6-answer.txt`

What do these 3 lines print?

```python
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
```

### 7. Is the same
**File:** `7-answer.txt`

What do these 3 lines print?

```python
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
```

### 8. Is really equal
**File:** `8-answer.txt`

What do these 3 lines print?

```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
```

### 9. Is really the same
**File:** `9-answer.txt`

What do these 3 lines print?

```python
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
```

### 10. And with a list, is it equal
**File:** `10-answer.txt`

What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
```

### 11. And with a list, is it the same
**File:** `11-answer.txt`

What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
```

### 12. And with a list, is it really equal
**File:** `12-answer.txt`

What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
```

### 13. And with a list, is it really the same
**File:** `13-answer.txt`

What do these 3 lines print?

```python
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
```

### 14. List append
**File:** `14-answer.txt`

What does this script print?

```python
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
```

### 15. List add
**File:** `15-answer.txt`

What does this script print?

```python
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
```

### 16. Integer incrementation
**File:** `16-answer.txt`

What does this script print?

```python
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
```

### 17. List incrementation
**File:** `17-answer.txt`

What does this script print?

```python
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
```

### 18. List assignation
**File:** `18-answer.txt`

What does this script print?

```python
def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
```

### 19. Copy a list object
**File:** `19-copy_list.py`

Write a function `def copy_list(l):` that returns a copy of a list.

```python
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)
```

### 20. Tuple or not?
**File:** `20-answer.txt`

```python
a = ()
```

Is `a` a tuple? Answer with Yes or No.

### 21. Tuple or not?
**File:** `21-answer.txt`

```python
a = (1, 2)
```

Is `a` a tuple? Answer with Yes or No.

### 22. Tuple or not?
**File:** `22-answer.txt`

```python
a = (1)
```

Is `a` a tuple? Answer with Yes or No.

### 23. Tuple or not?
**File:** `23-answer.txt`

```python
a = (1, )
```

Is `a` a tuple? Answer with Yes or No.

### 24. Who I am?
**File:** `24-answer.txt`

```python
a = (1)
b = (1)
a is b
```

### 25. Tuple or not
**File:** `25-answer.txt`

```python
a = (1, 2)
b = (1, 2)
a is b
```
### 26. Empty is not empty
**File:** `26-answer.txt`

```python
a = ()
b = ()
a is b
```

### 27. Still the same?
**File:** `27-answer.txt`

```python
>>> id(a)
139926795932424
>>> a
[1, 2, 3, 4]
>>> a = a + [5]
>>> id(a)
```

Will the last line of this script print `139926795932424`? Answer with Yes or No.

### 28. Same or not?
**File:** `28-answer.txt`

```python
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
```

Will the last line of this script print `139926795932424`? Answer with Yes or No.

### 29. #pythonic
**File:** `100-magic_string.py`

Write a function `magic_string()` that returns a string “BestSchool” n times the number of the iteration.

```python
#!/usr/bin/python3
magic_string = __import__('100-magic_string').magic_string

for i in range(10):
    print(magic_string())
```

### 30. Low memory cost
**File:** `101-locked_class.py`

Write a class `LockedClass` with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called `first_name`.

```python
#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
try:
    lc.last_name = "Snow"
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))
```

### 31. int 1/3
**Files:** `103-line1.txt`

```python
a = 1
```

How many `int` objects are created by the execution of the first line of the script?

**Files:** `103-line2.txt`

```python
b = 1
```

How many `int` objects are created by the execution of the second line of the script?

Continue the same structure for the next two parts.

### 32. int 2/3
**Files:** `104-line1.txt`, `104-line2.txt`, `104-line3.txt`, `104-line4.txt`, `104-line5.txt`

```python
a = 1024
b = 1024
del a
del b
c = 1024
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:

- How many `int` objects are created by the execution of the first line of the script?
- How many `int` objects are created by the execution of the second line of the script?
- After the execution of line 3, is the `int` object pointed by `a` deleted? Answer with Yes or No.
- After the execution of line 4, is the `int` object pointed by `b` deleted? Answer with Yes or No.
- How many `int` objects are created by the execution of the last line of the script?

### 33. int 3/3
**File:** `105-line1.txt`

```python
print("I")
print("Love")
print("Python")
```

Assuming we are using a CPython implementation of Python3 with default options/configuration:

- Before the execution of line 2 (`print("Love")`), how many `int` objects have been created and are still in memory?

### 34. Clear strings
**Files:** `106-line1.txt`, `106-line2.txt`, `106-line3.txt`, `106-line4.txt`, `106-line5.txt`

```python
a = "SCHL"
b = "SCHL"
del a
del b
c = "SCHL"
```

