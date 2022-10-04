function solution(A, B) {
    var answer = 0;
    let count = 0;
    let arrA = [...A]
    for(let i=0; i<arrA.length; i++){
        if(arrA.join("") == B){
            answer = count
            break
        }
        arrA.unshift(arrA[arrA.length-1])
        arrA.pop()        
        count ++        
    }
    if(count == A.length){
        answer = -1
    }
    return answer;
}