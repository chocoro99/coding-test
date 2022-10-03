def solution(s):
    for i in s:
        i = ord(i)
        if i >= 48 and i <= 57 and (len(s) == 4 or len(s) == 6):
            answer = True
        else:
            answer = False
            break
    return answer


print(solution("012a345ss6789a"))
