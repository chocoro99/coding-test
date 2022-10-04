function solution(array) {
    let answer = 0;
    
    for(let i of array){
        for(let z of String(i)){
            if(z.includes("7")){
                answer++;
            }
        }
    }
    return answer;
}