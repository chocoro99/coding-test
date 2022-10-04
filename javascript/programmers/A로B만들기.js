function solution(before, after) {
    let answer = 0;
    let beforeA = [...before]
    let afterA = [...after]
    let count = 0
    
    beforeA.sort()
    afterA.sort()
    for(let i=0; i<afterA.length; i++){
        if(beforeA[i] == afterA[i]){
            count++
        }
    }
    if(count == afterA.length){
        answer = 1
    }
    else{
        answer = 0
    }
        
    return answer
}