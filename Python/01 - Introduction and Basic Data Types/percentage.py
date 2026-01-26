'''The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.'''

nos = int(input())
data = []
for i in range(nos):
    n = str(input())
    a = n.split()
    data.append(a)
avg = 0
newlist = []
name = str(input(""))
for i in data:
    if name == i[0]:
        i.pop(0)
        for j in i: 
            a = float(j)
            newlist.append(a)
        for k in newlist:
            avg+=k
        c = (avg/len(newlist))
        d = f"{c:.2f}"
        print(d)