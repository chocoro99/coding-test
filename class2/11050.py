"""자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 
\(\binom{N}{K}\)를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 \(N\)과 \(K\)가 주어진다. (1 ≤ \(N\) ≤ 10, 0 ≤ \(K\) ≤ \(N\))

출력
n!
(n-k)!k!
예제 입력 1 
5 2
예제 출력 1 
10"""
import sys
import math

n, k = map(int, sys.stdin.readline().split(" "))
answer = 1
answer1 = 1
for i in range(k + 1, n + 1):
    answer *= i
for z in range(1, n - k + 1):
    answer1 *= z
print(math.trunc(answer / answer1))
