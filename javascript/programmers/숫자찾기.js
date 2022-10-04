function solution(num, k) {
    let numArray = [...String(num)]
    let answer = 0;
    
    for(let i=0; i < numArray.length; i++){
           if(numArray[i] == k){
               answer = i+1
               break
           }
    }
    if(answer == 0){
        return -1
    }
    else{
        return answer
    }
}