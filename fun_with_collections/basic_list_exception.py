"""
Program: basic_list.py
Author: Kelly Smith
Last date updated: 10/05/2019

Programs to make lists
:param
:param
:return

"""


def get_input():
    try:
        input_number = int(input('Please enter a number for the list '))
        return input_number
    except ValueError:
        print('Please enter a valid number')


def make_list():
    list_one = []
    while len(list_one) < 3:
        input_number = get_input()
        if input_number is not None:
            if len(list_one) < 3:
                list_one.append(input_number)
            else:
                break
    return list_one


if __name__ == '__main__':
    print(make_list())
