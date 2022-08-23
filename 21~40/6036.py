'''
[기초-산술연산] 단어 여러 번 출력하기
https://codeup.kr/problem.php?id=6036

단어와 반복 횟수를 입력받아 여러 번 출력해보자.

입력 예시
love 3

출력 예시
lovelovelove
'''
a,b = input().split(" ")
b = int(b)
print(a*b)