'''
[기초-조건/선택실행구조] 정수 1개 입력받아 분류하기
https://codeup.kr/problem.php?id=6067

0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분해 분류해보자.
음수이면서 짝수이면, A
음수이면서 홀수이면, B
양수이면서 짝수이면, C
양수이면서 홀수이면, D
를 출력한다.

입력 예시
-2147483648

출력 예시
A
'''
a = int(input())

if a < 0 :
    if a % 2 == 0 :
        print("A")
    else :
        print("B")
elif a > 0 :
    if a % 2 == 0 :
        print("C")
    else :
        print("D")