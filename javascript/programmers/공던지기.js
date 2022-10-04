function solution(numbers, k) {
    var answer = 0;
    if(numbers.length%2 == 0){
        for(let i=0; i<numbers.length; i++){
            if(numbers[i]%2 == 0){
                numbers.splice(i,1)
            }
        }
        answer = numbers[(k-1)%numbers.length]
    }
    else{
        for(let i=0; i<parseInt(numbers.length/2+1); i++){
            if(numbers[i]%2 == 0){  
                numbers.push(numbers[i])
                numbers.splice(i,1)
            }
        }
        answer = numbers[(k-1)%numbers.length]
    }
    return answer;
}