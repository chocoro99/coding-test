count = 0
max_n = 0

for i in range(1, 10):
    a = int(input())
    if a > max_n:
        max_n = a
        count = i
print(max_n,count, sep="\n")        