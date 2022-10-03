import sys

n = int(sys.stdin.readline())
q = []
for i in range(n):
    o = sys.stdin.readline().strip().split(" ")
    if o[0] == "push":
        q.append(o[1])

    elif o[0] == "pop":
        if len(q) > 0:
            print(q[0])
            del q[0]
        else:
            print("-1")
    elif o[0] == "size":
        print(len(q))
    elif o[0] == "empty":
        if len(q) == 0:
            print("1")
        else:
            print("0")
    elif o[0] == "front":
        if len(q) == 0:
            print("-1")
        else:
            print(q[0])
    elif o[0] == "back":
        if len(q) == 0:
            print("-1")
        else:
            print(q[len(q) - 1])
