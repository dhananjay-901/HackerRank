'''
given te names and grades for each student in a class of N students, store them in a nested list and print the names of any students having the second lowest grade.
note: if there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''
nos = int(input("number of students: "))
students = []
for i in range(nos):
    nm = []
    name  = str(input("name of students: "))
    marks = int(input("marks of students: "))
    nm.append(name)
    nm.append(marks)
    students.append(nm)
students.sort(key=lambda x: x[1])
mark = []
for i in students:
    a = mark.append(i[1])
b = set(mark)
c = list(b)
d = c[1]
for i in students:
    if d == i[1]:
        print(i[0])