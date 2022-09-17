a,b = map(int, input().split(" "))
r = 0                               # 나머지
gcd = 0                             # 최대 공약수
lcm = a*b                           # 최소 공배수

while True:
    if a%b == 0:
        gcd = b
        break
    elif a%b !=0:
        r = a%b
        a = b
        b = r

lcm = format(lcm/gcd,".0f")
print(gcd,lcm, sep="\n")