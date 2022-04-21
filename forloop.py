"""
This is the .py file for 'for loops'.
"""


if __name__ == '__main__':

    for i in range(0, 10):  # for loop and range
        print(i)

    set1 = {'a', 'b', 'c', 'c'}  # this is a set
    print("This is a set -")
    for i in set1:
        print(i)

    list1 = ['a', 'b', 'c', 'c']  # this is a list
    print("This is a list -")

    for i in list1:
        print(i)

    tuple1 = ('a', 'b', 'c', 'c')  # this is a tuple
    print("This is a tuple -")

    for i in tuple1:
        print(i)

    dict1 = {'a': 1, 'b': 1, 'c': 2}  # this is a dictionary
    print("This is a dictionary -")

    for key, value in dict1.items():
        print(key, value)
