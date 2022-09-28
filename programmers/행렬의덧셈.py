def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        l = []
        for z in range(len(arr1[0])):
            a = arr1[i][z] + arr2[i][z]
            l.append(a)
        answer.append(l)
    return answer


print(solution([[1, 2], [3, 4]], [[2, 3], [4, 5]]))
