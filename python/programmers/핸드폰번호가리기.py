def solution(phone_number):
    answer = ""
    l = len(phone_number) - 4
    number = phone_number[l : len(phone_number)]
    answer = "*" * l + number
    return answer


print(solution("0103333423232443554"))
