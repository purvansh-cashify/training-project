"""
This is the .py file for 'loops'.
"""

import other

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

    ele = 1
    for ele in range(0, 100):
        if ele == 10:
            break  # break statement, ends loop
        elif ele == 8:
            pass  # pass statement, will pass through the loop without executing
        if ele == 6:
            continue  # continues to the next iteration of the loop

        print("ele is ", ele)
        ele += 1

    lst = [x + 1 for x in range(0, 10)]  # list comprehension

    print(lst)

    nested = []

    for i in range(0, 5):  # nested for loop
        for j in range(0, 5):
            nested.append([i, j])

    print(nested)

    for i in range(95, 100):  # for-else in for loop
        print(i)
    else:
        print("DONE")

    num = 0

    while num < 10:  # while loop

        print("Hello", num, "!")
        num += 1

    other.func()  # Using the same method in multiple files
