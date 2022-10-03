def solution(price, money, count):
    p = 0
    for i in range(1, count + 1):
        p += price * i
    if money - p >= 0:
        return 0
    else:
        return p - money


print(solution(3, 20, 4))
