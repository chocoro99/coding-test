function solution(order) {
    let orderArray = [...String(order)];
    let answer = 0;
    
    for(let i of orderArray){
        if(i == "3" || i == "6" || i == "9"){
            answer++;
        }
    }
    return answer;
}