def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        l = [i]
        for z in range(1, i // 2 + 1):
            if i % z == 0:
                l.append(z)
        if len(l) % 2 == 0:
            answer += i
        elif len(l) % 2 != 0:
            answer = answer - i

    return answer


print(solution(13, 14))
