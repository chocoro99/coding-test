function solution(array) {
    let answer = [];
    let max = 0;
    let maxIndex = 0
    for(let i=0; i < array.length; i++){
        if(array[i] > max){
            max = array[i]
            maxIndex = i
        }
    }
    answer.push(max)
    answer.push(maxIndex)
    return answer;
}