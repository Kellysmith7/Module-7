def sort_list():
    kelly_list = [2.3, 6, 8.5, 6.6, 9, 10.2, 1.5]
    kelly_list.sort()
    return kelly_list  # Included a return so the sorted function will be the output of the function


def search_list():
    smith_list = (['cat', 'dog', 'mouse', 'fish'])
    return smith_list.index('cat')


if __name__ == '__main__':
    print(sort_list())
    print(search_list())
