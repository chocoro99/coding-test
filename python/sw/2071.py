t = int(input())

for i in range(1, t + 1):
    num = sum(map(int, input().split()))
    print("#" + str(i), format((num / 10), ".0f"))
