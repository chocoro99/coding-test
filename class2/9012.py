t = int(input())
open = 0
close = 0

for i in range(t):
    a = input()
    open = 0
    close = 0
    for z in range(len(a)):
        if a[z] == "(":
            open += 1
        elif a[z] == ")":
            close += 1
        if open == 0 and a[z] == ")":
            break
        elif close != 0 and a[z] == "(":
            break
        elif close > 0 and open > 0:
            open -= 1
            close -= 1
    if open == close:
        print("YES")
    else:
        print("NO")
