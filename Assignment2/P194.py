# Q.50
import math
grades = []


def semesterGrades():
    mid = eval(input(f'Enter midterm grade: '))
    final = eval(input(f'Enter final grade: '))
    avg = math.ceil((mid+final)/2)
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


print(f'Semester grade {semesterGrades()}.')
