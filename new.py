import sys

sys.path.append('/home/purvansh/PycharmProjects/training-project/proj-1')

from other import func


def new_func(x, y):
    print(x)
    print(type(x), type(y))
    print(y)


def return_five():
    return 5


if __name__ == '__main__':
    new_func(y="Hello World!", x="HI")

    func()

    return_five()

    print(type(return_five()))
