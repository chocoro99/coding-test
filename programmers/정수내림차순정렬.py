def solution(n):
    n_list = list(str(n))
    n_list = sorted(n_list, reverse=True)
    answer = "".join(n_list)
    return int(answer)


print(solution(118372))
