'''
[기초-종합] 언제까지 더해야 할까?
https://codeup.kr/problem.php?id=6079

1, 2, 3 ... 을 계속 더해 나갈 때,
그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
계속 더하는 프로그램을 작성해보자.

입력 예시
55

출력 예시
10
'''
a = int(input())
sum = 0
i = 1

while a >= sum :
    if a > sum :
        sum += i
    else :
        break
    if a > sum :
        i += 1

print(i)