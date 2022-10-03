'''
[기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2
https://codeup.kr/problem.php?id=6073

정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

입력 예시
5

출력 예시
4
3
2
1
0
'''
a = int(input())

for i in range(a):
    print(a-i-1)