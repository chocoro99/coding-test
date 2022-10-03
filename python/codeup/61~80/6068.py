'''
[기초-조건/선택실행구조] 점수 입력받아 평가 출력하기
https://codeup.kr/problem.php?id=6068

점수(정수, 0 ~ 100)를 입력받아 평가를 출력해보자.

평가 기준
점수 범위 : 평가
90 ~ 100 : A
70 ~ 89 : B
40 ~ 69 : C
0 ~ 39 : D
로 평가되어야 한다.

입력 예시
73

출력 예시
B
'''
a = int(input())

if a >= 90 and a <= 100 :
    print("A")
elif a >= 70 and a <= 89 :
    print("B")
elif a >= 40 and a <= 69 :
    print("C")
else :
    print("D")    