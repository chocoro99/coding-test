function solution(my_string, letter) {
    var answer = [...my_string];
    for(let i=0; i <= answer.length; i++){
        if(answer[i] == letter){
            answer.splice(i,1)
            i --
        }
    }
    answer = answer.join('')
    return answer;
}