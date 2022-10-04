function solution(s) {
    let arrayS = s.split(" ")
    let answer = []
    let a = 0
    
    for(let i=0; i<arrayS.length; i++){
        if(arrayS[i]!="Z"){
            answer.push(parseInt(arrayS[i]))
        }
        if(arrayS[i]=="Z" & answer.length > 0){
            answer.pop()
        }
    }
    for(let i=0; i <answer.length; i++){
        a+=answer[i]
    }
    return a;
}