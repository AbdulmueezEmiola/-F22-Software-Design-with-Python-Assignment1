from contextlib import redirect_stdout
from io import StringIO
from time import perf_counter
from inspect import signature, getsource
from lib import handle_indent
from task4 import decorator_4


class Decorator3:
    """
    The decorator for decorating a function

    Args:
        func (function): The function to be decorated

    Attributes:
        count (int): The number of times the function has been executed

    """
    time = {}

    def __init__(self, func):
        self.func = func
        self.count = 0

    @decorator_4
    def __call__(self, *args, **kwargs):
        """
        The decorated function. In addition to executing the function,
        It also prints the following to the file "decorator_3.txt"
            1) the amount of times a function was executed
            2) the time of execution for each execution
            3) the name of the function
            4) the type of the function
            5) the docstring of the function
            6) the signature of the function
            7) the source of the function
            8) and any output during the execution of the function
        :param args: list of positional arguments
        required by the decorated function
        :param kwargs: list of keyword arguments
        required by the decorated function
        :return: None
        """
        result = None
        start_time = perf_counter()
        with redirect_stdout(StringIO()) as output:
            result = self.func(*args, **kwargs)
        end_time = perf_counter()

        Decorator3.time[self.func.__name__] = end_time - start_time
        self.count += 1

        details_store = {
            'name': self.func.__name__,
            'type': type(self.func),
            'sign': signature(self.func),
            'args': 'positional {} \nkey=worded {}'.format(args, kwargs),
            'doc': self.func.__doc__.strip(),
            'source': getsource(self.func),
            'output': output.getvalue()
        }

        with open('assets/decorator_3.txt', 'a') as file:
            with redirect_stdout(file):
                print("{0} call {1} executed in {2:.4f}".format(details_store['name'], self.count, end_time - start_time))
                for key, value in details_store.items():
                    print(handle_indent('{:10} {}'.format(key.title() + ":", value)))
                print()
        return result

    @staticmethod
    def get_rank():
        """
        Sorts all the decorated functions based
        on their time of execution
        :return: the sorted dictionary
        """
        return sorted(Decorator3.time.items(), key=lambda a: a[1])
