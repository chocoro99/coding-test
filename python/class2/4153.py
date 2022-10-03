while 1:
    a = list(map(int, input().split(" ")))
    if " ".join(map(str, a)) == "0 0 0":
        break
    max_a = max(a)
    b = 0
    for i in a:
        if i != max_a:
            b = b + i**2
    if b == 0:
        print("wrong")
    elif (max_a**2) / b == 1:
        print("right")
    else:
        print("wrong")
