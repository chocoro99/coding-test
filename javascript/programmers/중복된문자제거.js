function solution(my_string) {
    let myStr = [...my_string]
    let answer = []
    for(let i=0; i < my_string.length; i++){
        if(answer.includes(my_string[i])){
            myStr.splice(i,1)            
        }
        else{
            answer.push(my_string[i])
        }
    }
    answer = answer.join('')
    return answer;
}