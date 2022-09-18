from contextlib import redirect_stdout
from io import StringIO
from time import perf_counter
from inspect import signature, getsource, Parameter
from lib import handle_indent
from task4 import decorator_4


class Decorator3:
    """
    The decorator for decorating a function

    Args:
        func (function): The function to be decorated

    Attributes:
        count (int): The number of times the function has been executed
        time (int): The time taken by the last execution of the function
    """
    def __init__(self, func):
        self.func = func
        self.count = 0
        self.time = 0
        self.name = func.__name__

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
        start_time = perf_counter()
        with redirect_stdout(StringIO()) as output:
            self.func(*args, **kwargs)
        end_time = perf_counter()
        self.time = end_time - start_time
        self.count += 1
        func_signature = signature(self.func)
        keyword = {
            k: v.default for k, v in func_signature.parameters.items()
            if v.default is not Parameter.empty
        }
        positional = (None,) * (len(func_signature.parameters.items()) - len(keyword))
        details_store = {
            'name': self.name,
            'type': type(self.func),
            'sign': func_signature,
            'args': 'positional {} \nkey=worded {}'.format(positional, keyword),
            'doc': self.func.__doc__.strip(),
            'source': getsource(self.func),
            'output': output.getvalue()
        }
        with open('decorator_3.txt', 'a') as file:
            with redirect_stdout(file):
                print("{0} call {1} executed in {2:.4f}".format(details_store['name'], self.count, self.time))
                for key, value in details_store.items():
                    print(handle_indent('{:10} {}'.format(key + ":", value)))
                print()
