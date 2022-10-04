function solution(n) {
    let answer = 1;
    let i = 1;
    while(true){
        i = i*answer
        if(i>n){
            answer--
            break
        }
        answer++
        
    }
    return answer;
}