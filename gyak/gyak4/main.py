import pickle
import os


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def __iadd__(self, other):
        self.students.append(other)
        return self

    def __str__(self):
        count = 0
        for student in self.students:
            count += student.mark
        for student in self.students:
            print(student)
        return f'Class average is {round(count / len(self.students), 2)}'


class Student:
    def __init__(self, name):
        self.name = name
        self.mark = 0

    def __str__(self):
        return f'{self.name}: {self.mark}'

    def __lt__(self, other):
        return self.mark < other.mark

    def __repr__(self):
        return f'Student({self.name},{self.mark})'

    def markUp(self):
        self.mark += 1

    def markDown(self):
        self.mark -= 1


c = Classroom()
if os.path.exists('classroom.pickle'):
    with open('classroom.pickle', 'rb') as f:
        c = pickle.load(f)

s1 = Student('A')
s2 = Student('B')
s3 = Student('C')
s3.markUp()
s3.markUp()

c += s1
c += s2
c += s3

for student in c.students:
    student.markUp()

print(c)
print(sorted(c.students, reverse=True))

with open('classroom.pickle', 'ab') as f:
    pickle.dump(c, f)
