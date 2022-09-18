---
tags: SSD
title: SSD Assignment 1
---

## Decorators in Action
**Due Date:** 20 September 2022
**Submission Format:** GitHub repository link.
**Python version:** Python 3.5 or greater
**Grading:** Each task has 5 points max

:::info
**NOTE** : 5 bonus points will be rewarded for code quality and reviewing your classmate's code. plagiarism results in a fail.
:::

Let's start by remembering the major characteristics of python programming language:
1. High-level language
2. Object-oriented language
3. Functional language
4. “Modular” language
5. Dynamically typed language
6. Interpreted language

In this assignment, we will try to exhaust all the characteristics of python. First, start with number 4 (“Modular” language). Each task should be implemented in a separate `.py` file and imported to the driver program in the `main.py` script. Example structure : 

```
├── src              <- directory for source files 
|    ├── main.py     <- driver program file 
|    ├── task1.py    <- task 1 implemented here 
|    ├── ...
|    └── task4.py    <- task 4 implemented here 
│                               
├── ....             <- bla bla bla
└── Readme.md
```

The `main.py` file contains at least 2 functions containing **lambda** expressions within, quadratic equation solver function and **pascal triangle** printer function (as in lab) for testing of your implementations.
**Avoid using recursive functions**

<!-- 2 functions implemented from the previous labs.  -->


## Task 1 

Create a function decorator that calculates function execution time and the number of times the decorated function was called (function call trace). Make sure that your implementation works for multiple functions. Below you can see an example of the overall python program expected behavior and implementation script:

```python
$ cat main.py
import random
from task1 import decorator_1

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n =  random.randint(10,751)
    for i in range(n):
        result += (i**2)
        
@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n =  random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val: 
            max_val = i
    
if __name__ == "__main__": 
    func()
    funx()
    func()
    funx()
    func()
```

```python
$ python main.py 
func call 1 executed in 0.0130 sec
funx call 1 executed in 0.4130 sec
func call 2 executed in 0.1130 sec
funx call 2 executed in 0.0031 sec
func call 3 executed in 0.0031 sec
```

## Task 2 
Extend your implementation so that the decorator could dump original source code of the function. Each function to be decorated should have a docstring. [What is a docstring?](https://www.python.org/dev/peps/pep-0257/). To inspect and manipulate function objects see [`inspect`](https://docs.python.org/3/library/inspect.html) module. Here is an example of the overall python program expected behavior and implementation script: 

```python 
$ cat main.py
from task2 import decorator_2

@decorator_2
def funh(bar1, bar2=""):
    """
    This function does something useful 
    :param bar1: description
    :param bar2: description
    """ 
    print("some\nmultiline\noutput")

if __name__ == "__main__": 
    funh(None, bar2="")

$ python main.py

funh call 1 executed in 0.0130 sec
Name:   funh
Type:   <class 'function'>
Sign:   (bar1, bar2='')
Args:   positional (None,) 
        key=worded {'bar2': ''}
        
Doc:    This function does somthing useful
        :param bar1: description
        :param bar2: description

Source: @decorator_2
        def foo(bar1, bar2=""):
        """
        This function does something useful 
        :param bar1: description
        :param bar2: description
        """ 
        print("some\nmultiline\noutput")

Output: some
        multiline
        output

```

## Task 3 
Implement the decorator behavior in tasks 1 & 2 using a class decorator. All the program output (from the decorator) should be dumped into a `.txt` file. Rank the 4 functions used to test the implementation and plot a rankings table. i.e
**Hint:** use a global variable

```python 
python main.py
PROGRAM | RANK | TIME ELAPSED
fun1        1     0.011488118s
fun3        2     0.020115991s
fun2        3     0.045907541s
fun4        4     0.045907541s
```
 
## Task 4 

Again, extend your program (function or class decorator) so that if a decorated function encounters an error it wouldn’t put it back into stdout. Instead, pipe the error stream into a log file together with a timestamp. Test both the class decorator and function decorator
**Hint:** Use [Try and Except](https://docs.python.org/3/tutorial/errors.html) statements

<!-- ## Task 5
Last task and the easiest.. Remember: Python is a Modular language. It's time to prove that python is a modular programming language. make your program modular.. Split the decorator function and class into a separate file (`reflect.py`) and import it to your `main.py` for usage. -->

## Useful Resources 
1. [Inspect module](https://docs.python.org/3/library/inspect.html)
2. [contextlib](https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout)
3. [Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
4. [Reading and Writing Files in Python](https://realpython.com/read-write-files-python/)
5. [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
6. [Python Exceptions](https://realpython.com/python-exceptions/)
7. [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)



