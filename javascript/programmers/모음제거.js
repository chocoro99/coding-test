function solution(my_string) {
    let a = ["a","e","i","o","u"];
    let answer = [...my_string];
    for(let i=0; i < answer.length; i++){
        if(a.includes(answer[i])){
            answer.splice(i,1);
            i--
        }
    }
    answer = answer.join('')
    return answer;
}