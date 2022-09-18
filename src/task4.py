from contextlib import redirect_stdout
from lib import handle_indent
from datetime import datetime
import traceback


def decorator_4(func):
    """
    Serves as an exception catcher.
    It catches all the exceptions that occur while running
    a decorated function. It pipes the error to a log file.
    :param func: The decorator function to be wrapped.
    :return wrapper: The newly wrapped function
    """
    def wrapper(*args, **kwargs):
        """
        The decorated function.
        It saves the following to the error_log.txt file
            1) The timestamp of the error
            2) The type of the error
            3) The error message of any
            4) The trace
        :param args: list of positional arguments
        required by the decorated function
        :param kwargs: list of keyword arguments
        required by the decorated function
        :return: None
        """
        try:
            func(*args, **kwargs)
        except BaseException as error:
            with open('error_log.txt', 'a') as file:
                with redirect_stdout(file):
                    print(handle_indent('{:10} {}'.format("Date:", datetime.now())))
                    print(handle_indent('{:10} {}'.format("Type:", type(error))))
                    print(handle_indent('{:10} {}'.format("Message:", error)))
                    print(handle_indent('{:10} {}'.format("Trace:", traceback.format_exc())))
                    print()
    return wrapper
