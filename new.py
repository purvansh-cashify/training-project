"""
This is the main .py file which will run directly
"""

import sys
from other import func  # importing one file from another

sys.path.append('/home/purvansh/PycharmProjects/training-project/proj-1')


def new_func(x, y):
    print(x)
    print(type(x), type(y))
    print(y)


def return_five():
    return 5


def myfunc(*args):
    for i in args:
        print(i)


def kwarg_func(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


def greeting(name: str) -> str:  # specifying using typing
    return 'Hello ' + name


if __name__ == '__main__':
    print("Methods - \n")

    new_func(y=str("Hello World!"), x=str("HI"))  # specifying data type of argument

    print(greeting("Purvansh"))

    func()

    print(return_five())

    print(type(return_five()))

    myfunc([1, 2, 3, 4])

    myfunc([1, 2, 3, 4, 5, 6])

    kwarg_func(**{'a': 1, 'b': 1, 'c': 1})

    kwarg_func(**{'a': 1, 'b': 1, 'c': 1, 'd': 2})
