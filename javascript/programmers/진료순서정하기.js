function solution(emergency) {
    var answer = [];
    let a = []
    
    for(let i=0; i<emergency.length; i++){
        a.push(emergency[i])}
    a = a.sort((a,b) => b-a)
    
    for(let z=0; z<emergency.length; z++){
        const x = a.indexOf(emergency[z])
        answer.push(x+1)
    }
        
    return answer
}