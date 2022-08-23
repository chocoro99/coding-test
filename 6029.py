'''
[기초-값변환] 16진 정수 입력받아 8진수로 출력하기
https://codeup.kr/problem.php?id=6029

16진수를 입력받아 8진수(octal)로 출력해보자.

입력 예시
f

출력 예시
17
'''
a = input()
a = int(a, 16)
print("%o"%a)