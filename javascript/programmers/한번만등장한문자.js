function solution(s) {
    let answer = [];
    let a = [];
    let arrayS = [...s];
    
    arrayS.sort()
    for(let i=0; i<arrayS.length; i++){
        if(a.includes(arrayS[i]) == false){
            a.push(arrayS[i]);
        }
    }
    for(let i=0; i<a.length; i++){
        let count = arrayS.filter(element => a[i] === element).length
        if(count == 1){
            answer.push(a[i])
        }
    }
    answer = answer.join("")
    return answer
}