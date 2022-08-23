'''
[기초-값변환] 정수 입력받아 유니코드 문자로 변환하기
https://codeup.kr/problem.php?id=6031

10진 정수 1개를 입력받아
유니코드 문자로 출력해보자.

입력 예시
65

출력 예시
A
'''
a = input()
a = int(a)
print(chr(a))