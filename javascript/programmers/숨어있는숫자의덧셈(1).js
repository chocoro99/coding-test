function solution(my_string) {
    let answer = 0;
    for(let i of [...my_string]){
        if(i > 0){
            answer += parseInt(i)
        }
    }
    return answer;
}