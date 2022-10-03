while True:
    a = input()
    if a == '0':
        break
    b = int(a[::-1])
    a = int(a)
    if a == b:
        print("yes")
    elif a != b:
        print("no")