def solution(numbers):
    answer = 0
    number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in numbers:
        number_list.remove(i)
    for i in number_list:
        answer += i
    return answer


print(solution([1, 2, 3, 4, 5, 6, 7, 8]))
