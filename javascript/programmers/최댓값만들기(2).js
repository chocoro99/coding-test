function solution(numbers) {
    let answer = numbers;
    let p = 0
    let m = 0
    
    answer.sort((a,b) =>{
        if(a>b){return 1}
        if(a==b){return 0}
        if(a<b){return -1}
    })
    p = answer[0]*answer[1]
    m = answer[answer.length-1]*answer[answer.length-2]
    if(p>m){
        return p
    }
    else if(p < m){
        return m
    }
    else{
        return m
    }
}