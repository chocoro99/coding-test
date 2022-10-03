import sys

n = int(sys.stdin.readline().strip())
person_l = []
for i in range(n):
    person_l.append(sys.stdin.readline().strip().split(" "))
    person_l[i][0] = int(person_l[i][0])

person_l = sorted(person_l, key=lambda x: x[0])
for i in person_l:
    print(i[0], i[1])
