t = int(input())

for i in range(1, t + 1):
    m = input()
    p = m[::-1]
    if m == p:
        print("#" + str(i), "1")
    else:
        print("#" + str(i), "0")
