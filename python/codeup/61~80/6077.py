'''
[기초-종합] 짝수 합 구하기
https://codeup.kr/problem.php?id=6077

정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합을 구해보자.

입력 예시
5

출력 예시
6
'''
a = int(input())
sum = 0

for i in range(a+1):
    if i%2 == 0 :
        sum +=i
print(sum)