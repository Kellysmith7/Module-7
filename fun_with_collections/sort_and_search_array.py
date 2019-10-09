"""
Program: sort_and_search_array.py
Author: Kelly Smith
Last date updated: 10-8-19

Program to search and sort arrays
:param c: array to be sorted
:param f: array to search
:return The sorted array c and the searched value in array f or -1 if it is not found
"""
import array as arr


def sort_array(c):
    c = arr.array('d', [1.2, 6.3, 5.4])
    d = c.tolist()
    d.sort()
    e = arr.array('d', d)
    return e  # Included a return so the sorted array will be the array that is the output of the function


def search_array(f, value):
    f = arr.array('d', [8.2, 4.3, 6.4])
    try:
        return f.index(value)
    except ValueError:
        return -1



if __name__ == '__main__':
    c = arr.array('d', [1.2, 6.3, 5.4])
    f = arr.array('d', [8.2, 4.3, 6.4])
    print(sort_array(c))
    print(search_array(f, 6.3))


