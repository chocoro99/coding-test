import sys

n, k = map(int, sys.stdin.readline().split(" "))
count = 0
number = 0
y = []
answer = []

for i in range(1, n + 1):
    y.append(i)

while 1:
    count += 1
    if len(answer) == n:
        break
    if number >= len(y):
        number = 0
    if count == k:
        count = 0
        answer.append(y[number])
        del y[number]
        number -= 1
    number += 1
answer = ", ".join(map(str, answer))
print("<" + answer.strip() + ">")
