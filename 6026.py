'''
[기초-값변환] 실수 2개 입력받아 합 계산하기
https://codeup.kr/problem.php?id=6026

실수 2개를 입력받아
합을 출력하는 프로그램을 작성해보자.

입력 예시
0.1
0.9

출력 예시
1.0
'''
a = input()
b = input()
a,b = float(a), float(b)
print(a+b)