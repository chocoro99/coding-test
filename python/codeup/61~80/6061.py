'''
[기초-비트단위논리연산] 비트단위로 OR 하여 출력하기
https://codeup.kr/problem.php?id=6061

입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
비트단위(bitwise) 연산자 |(or, vertical bar, 버티컬바)를 사용하면 된다.

입력 예시
3 5

출력 예시
7
'''
a,b = input().split(" ")
a,b = int(a), int(b)
print(a|b)