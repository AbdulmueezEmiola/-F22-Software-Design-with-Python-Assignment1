from time import perf_counter
from contextlib import redirect_stdout
from io import StringIO
from task4 import decorator_4


def decorator_1(func):
    """
    A decorator for printing out the amount of times
    a function was executed and the time of execution for each
    :param func: The function to be decorated
    :return wrapper: the reference to the wrapped function
    """
    counter = 0

    @decorator_4
    def wrapper(*args, **kwargs):
        """
        A decorated function.
        Prints out the number of times the function
        was executed and the time taken for each execution.
        Redirects the output of the function to an IO
        :param args: list of positional arguments
        required by the decorated function
        :param kwargs: list of keyword arguments
        required by the decorated function
        :return: None
        """
        nonlocal counter
        counter += 1
        start_time = perf_counter()
        with redirect_stdout(StringIO()):
            func(*args, **kwargs)
        end_time = perf_counter()
        print("{0} call {1} executed in {2:.4f}".format(func.__name__, counter, end_time - start_time))

    return wrapper
