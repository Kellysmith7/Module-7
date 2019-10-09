"""
Program: file_tuple.py
Author: Kelly Smith
Last date update: 10-6-19

Program to open a file and add information
"""


def write_to_file(student_tuple):
    f = open('./student_info.txt', 'a')
    f.writelines(str(student_tuple))
    f.close()


def get_student_info(**kwargs):
    score = ''
    score_list = []
    for kw in kwargs:
        print(kw, ":", kwargs[kw])
        while score != 'q':
            score = input('Please enter your test score or q to quit ')
            if score != 'q':
                score_list.append(score)
        write_to_file((score_list, kwargs))


def read_from_file():
    f = open('./student_info.txt', "r")
    content = f.readlines()
    print(content)
    f.close()


if __name__ == '__main__':
    get_student_info(Name='Kelly')
    get_student_info(Name='BOB')
    get_student_info(Name='Joe')
    get_student_info(Name='Jim')
    read_from_file()
