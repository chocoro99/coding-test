"""
[기초-종합] 16진수 구구단 출력하기
https://codeup.kr/problem.php?id=6081

16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운
영일이는 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.

A, B, C, D, E, F 중 하나가 입력될 때,
1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자.
(단, A ~ F 까지만 입력된다.)

입력 예시
B

출력 예시
B*1=B
B*2=16
B*3=21
B*4=2C
B*5=37
B*6=42
B*7=4D
B*8=58
B*9=63
B*A=6E
B*B=79
B*C=84
B*D=8F
B*E=9A
B*F=A5
"""
a = int(input(), 16)

for i in range(1, 16):
    print("%X" % a + "*" + "%X" % i + "=" + "%X" % (a * i))
