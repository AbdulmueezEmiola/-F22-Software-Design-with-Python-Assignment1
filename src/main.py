import random
from task1 import decorator_1
from task2 import decorator_2
from task3 import Decorator3


@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)


@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


@decorator_2
def funh(bar1, bar2=""):
    """
    This function does something useful
    :param bar1: description
    :param bar2: description
    """
    print("some\nmultiline\noutput")


@Decorator3
def fun1(n):
    """
    function for creating a pascal's triangle
    :param n: the number of rows
    :return: None
    """
    lists = [[1]]
    for j in range(n):
        temp = [0]+lists[j]+[0]
        lists.append([value + temp[count+1] for count, value in enumerate(temp) if count < j+2])
    output = []
    for row in lists:
        output.append(' '.join([str(i) for i in row]))
    max_size = len(output[-1])
    for row in output:
        print(row.center(max_size))


@Decorator3
def fun2(a, b, c):
    """
    Quadratic equation solver ax**2 + bx+c =0
    :param a:
    :param b:
    :param c:
    :return: None
    """
    rhs = ((b**2 - 4*a*c)**0.5)/(2*a)
    print(-b + rhs, -b-rhs)


@Decorator3
def fun3(a, b):
    """
    Generating a hyperbola
    :param a: half the length of the major axis
    :param b: half the length of the minor axis
    :return: None
    """
    x = range(-10, 10)
    y = [((i ** 2 / a ** 2 - 1) * b ** 2) ** 0.5 for i in x]
    print(list(zip(x, y)))
    result = '\n'.join(list(map(lambda val: str(val)+" is a number", y)))
    print(result)

@Decorator3
def fun4(a, b):
    """
    Generating an ellipse
    :param a: half the length of the major axis
    :param b: half the length of the minor axis
    :return: None
    """
    x = range(-10, 10)
    y = [((1 - i ** 2 / a ** 2) * b ** 2) ** 0.5 for i in x]
    result = list(filter(lambda elem: elem is complex, y))
    print('Number of non complex is ', len(y) - len(result))
    print(list(zip(x, y)))


@decorator_1
def fun5():
    """
    Raises an error in order to test decorator 4(Error Checker decorator)
    :return None:
    """
    raise ValueError("There is an error")


@decorator_2
def fun6():
    """
    Raises an error in order to test decorator 4(Error Checker decorator)
    :return None:
    """
    raise ArithmeticError("There is an error")


@Decorator3
def fun7():
    """
    Raises an error in order to test decorator 4(Error Checker decorator)
    :return None:
    """
    raise ZeroDivisionError("There is an error")


if __name__ == "__main__":
    print('-'*20+" Executing Task 1 "+'-'*20)
    # Task 1
    func()
    funx()
    func()
    funx()
    func()

    print('\n'+'-'*20+" Executing Task 2 "+'-'*20)
    funh(None, bar2="")

    print('\n'+'-'*20+" Executing Task 3 "+'-'*20)
    # Task 3
    fun1(10)
    fun2(1, 0, 1)
    fun3(10, 5)
    fun4(10, 5)
    counter_store = {
        fun1.name: fun1.time,
        fun2.name: fun2.time,
        fun3.name: fun3.time,
        fun4.name: fun4.time
    }
    print("PROGRAM | RANK | TIME ELAPSED")
    for index, item in enumerate(sorted(counter_store.items(), key=lambda a: a[1])):
        print('{:<8.8} {:^6} {:>12}s'.format(item[0], index, item[1]))

    print('\n'+'-'*20+" Executing Task 4 "+'-'*20)
    fun5()
    fun6()
    fun7()
