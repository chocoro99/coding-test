function solution(array, n) {
    let answer = 200;
    let a = 200
    for(let i of array){
        if(Math.abs(n-i)<a){
            a = Math.abs(n-i)
            answer = i
        }
        if(Math.abs(n-i)==a){
            if(i < answer){
                answer = i
            }
        }
    }
    
    return answer;
}