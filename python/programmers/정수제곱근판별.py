def solution(n):
    answer = 0
    for i in range(1, n + 1):
        answer = i * i
        if answer == n:
            answer = (i + 1) * (i + 1)
            break
        if i == n:
            answer = -1
    return answer


print(solution(3))
