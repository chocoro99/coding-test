def solution(n, m):
    answer = []
    r, l = n, m
    if r > l:
        while 1:
            if r // l > 0 and r % l == 0:
                answer.append(l)
                break
            else:
                temp = r % l
                r = l
                l = temp
    elif r < l:
        while 1:
            if l // r > 0 and l % r == 0:
                answer.append(r)
                break
            else:
                temp = l % r
                l = r
                r = temp
    else:
        answer.append(r)
        answer.append(l)
        return answer
    answer.append((n * m) // answer[0])
    return answer


print(solution(2, 5))
