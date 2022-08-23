'''
[기초-입출력] 연월일 입력받아 순서 바꿔 출력하기
https://codeup.kr/problem.php?id=6019

"연도.월.일"을 입력받아 "일-월-연도" 순서로 바꿔 출력해보자.

입력 예시
2020.3.4

출력 예시
4-3-2020
'''
a,b,c = input().split('.')
a,b,c = int(a), int(b), int(c)
print(c,b,a, sep=('-'))