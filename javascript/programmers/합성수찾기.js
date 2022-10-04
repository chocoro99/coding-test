function solution(n) {
    let answer = 0;
    let count = 0;
    
    for(let i=1; i<=n; i++){
        count = 0
        for(let z=1; z<=i; z++){
            if(i%z==0){
                count++;
            }
            if(count>=3){
                answer++;
                break
            }
        }
    }
    return answer;
}