'''
[기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기
https://codeup.kr/problem.php?id=6074

영문 소문자(a ~ z) 1개가 입력되었을 때,
a부터 그 문자까지의 알파벳을 순서대로 출력해보자.

입력 예시
f

출력 예시
a b c d e f
'''
a = ord(input())
b = ord('a')

while b<=a :
  print(chr(b), end=' ')
  b += 1