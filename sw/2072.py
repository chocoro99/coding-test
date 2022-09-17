t = int(input())

for i in range(1, t + 1):
    num = 0
    num_list = list(map(int, input().split(" ")))
    for z in num_list:
        if z % 2 != 0:
            num += z
    print("#" + str(i), num)
