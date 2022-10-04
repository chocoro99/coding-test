function solution(my_string) {
    let answer = [...my_string.toLowerCase()];
    answer.sort()
    answer = answer.join('')
    return answer;
}