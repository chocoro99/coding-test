function solution(numbers) {
    let answer = 0;
    let maxA = 0;
    let maxB = 0;
    for(let i of numbers){
        if(i > maxA){
            maxB = maxA;
            maxA = i;
        }
        else if(i > maxB){
            maxB = i
        }
    }
    answer = maxA*maxB
    return answer;
}