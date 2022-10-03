function solution(my_string, n) {
    let answer = [...my_string]
    for(let i=0; i < answer.length; i++){
        answer[i] = answer[i].repeat(n)
    }
    answer = answer.join('')
    return answer;
}
console.log(solution("hello",3))