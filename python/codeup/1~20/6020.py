'''
[기초-입출력] 주민번호 입력받아 형태 바꿔 출력하기
https://codeup.kr/problem.php?id=6020

주민번호를 입력받아 형태를 바꿔 출력해보자.

입력 예시
000907-1121112

출력 예시
0009071121112
'''
a,b = input().split('-')
print(a,b, sep='')