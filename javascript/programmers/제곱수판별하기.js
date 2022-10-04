function solution(n) {
    let answer = 0;
    let i = 1
    while(i <= parseInt(n/2)){
        if(i*i == n){
            answer = 1;
            break
        }
        i += 1
    }
    if(answer == 0){
        return 2
    }
    else{
        return answer
    }
}