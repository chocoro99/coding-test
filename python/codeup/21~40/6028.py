'''
[기초-출력변환] 10진 정수 입력받아 16진수로 출력하기2
https://codeup.kr/problem.php?id=6028

10진수를 입력받아 16진수(hexadecimal) 대문자로 출력해보자.

입력 예시
255

출력 예시
FF
'''
a = input()
a = int(a)
print(('%x'%a).upper())