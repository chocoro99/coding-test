'''
[기초-비트시프트연산] 2의 거듭제곱 배로 곱해 출력하기
https://codeup.kr/problem.php?id=6047

정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
0 <= a <= 10, 0 <= b <= 10

입력 예시
1 3

출력 예시
8
'''
a,b = input().split(" ")
a,b = int(a), int(b)
print(a*(2**b))