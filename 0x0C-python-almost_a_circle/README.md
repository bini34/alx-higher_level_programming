
# 0x0C. Python - Almost a circle

## Project Description

This project is part of the Higher-Level Programming curriculum and focuses on reinforcing Python concepts. The primary goal is to implement a set of classes and functionalities that cover various aspects of Python programming, including object-oriented programming (OOP), file handling, serialization/deserialization, unit testing, and more.

## Table of Contents

- [Background Context](#background-context)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Tasks](#tasks)
- [How to Use](#how-to-use)
- [License](#license)

## Background Context

The project is centered around the AirBnB project, which is a significant part of the Higher-Level Programming curriculum. Completing this project will prepare you for more advanced challenges and real-world applications.

## Learning Objectives

Upon completion of this project, you should be able to:

- Explain the concept of unit testing and implement it in a large project
- Serialize and deserialize a class
- Read and write to a JSON file
- Understand and use *args and **kwargs
- Handle named arguments in a function
- Validate attributes using setters
- Implement inheritance and understand OOP principles

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- Interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files end with a new line
- The first line of all files is `#!/usr/bin/python3`
- A README.md file at the root of the project folder is mandatory
- Code should use pycodestyle (version 2.8.*)
- All files must be executable
- Length of files will be tested using `wc`
- Modules, classes, and functions should be documented

### Python Unit Tests

- Allowed editors: vi, vim, emacs
- All test files inside a folder named `tests`
- Use the `unittest` module
- Test files and folders should start with `test_`
- Run tests using `python3 -m unittest discover tests`

## Tasks

### 0. If it's not tested, it doesn't work
- All files, classes, and methods must be unit tested and PEP 8 validated

### 1. Base class
- Create a folder named `models` with an empty file `__init__.py` inside to make it a Python package
- Create a class named `Base` with private class attribute `__nb_objects` initialized to 0
- Implement a class constructor that increments `__nb_objects` and assigns the new value to the public instance attribute `id`

...

### 19. File to instances
- Add a class method `load_from_file(cls)` to Base that returns a list of instances
- The filename must be `<Class name>.json` (e.g., Rectangle.json)
- If the file doesn’t exist, return an empty list
- Otherwise, return a list of instances

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/bini34/alx-higher_level_programming.git
```

2. Navigate to the project directory:

```bash
cd alx-higher_level_programming/0x0C-python-almost_a_circle
```

3. Run the tests:

```bash
python3 -m unittest discover tests
```


## License

This project is licensed under the terms of the MIT license.

---
