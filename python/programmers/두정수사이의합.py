def solution(a, b):
    answer = 0
    for i in range(a if b > a else b, (b if b > a else a) + 1):
        answer += i
    return answer


print(solution(5, 3))
