"""
Program: average_score.py
Author: Kelly Smith
Last date updated: 10-6-19

Program to show the average scores of a student
:param Average score: average of a student's test scores
:param Name: student name
:param Course: course student is taking
:param GPA: student GPA
:return Average Score, Name, Course and GPA of a student
"""


def average_scores(*args, **kwargs):
    for kw in kwargs:
        print(kw, ":", kwargs[kw])
    print('Average Score is: ', sum(args) / len(args))


if __name__ == '__main__':
    print(average_scores(90, 85, 80, 85, Name='Kelly Smith', Course='Python', GPA=3.5))
    print(average_scores(95, 85, 90, 95, Name='Joe Smith', Course='Python', GPA=3.8))
    print(average_scores(80, 75, 80, 85, Name='Mary Smith', Course='Python', GPA=3.3))
