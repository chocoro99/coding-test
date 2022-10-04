function solution(n) {
    let answer = [];
    let i = 1
    
    while(true){
        if(n/i==1){
            break
        }
        i++
        if(n%i==0){
            if(answer.includes(i)==false){
                answer.push(i)
                n = n/i
                i =1
            }
            else{
                n = n/i
                i = 1
            }
        }
    }
    return answer;
}