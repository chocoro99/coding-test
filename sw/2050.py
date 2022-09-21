a = input()
a = a.lower()

for i in a:
    i = ord(i) - 96
    print(i, end=" ")
