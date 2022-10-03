a = list(map(int, input().split(" ")))

ase = [1,2,3,4,5,6,7,8]
des = ase[:]
des.reverse()

if a == ase:
    print("ascending")
elif a == des:
    print("descending")
else:
    print("mixed")