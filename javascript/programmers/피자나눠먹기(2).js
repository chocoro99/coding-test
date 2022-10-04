function solution(n) {
    let answer = 0
    let m = 6
    let mn = n*m
    let temp = 0
    
    while(true){  
        temp = n
        n = m
        m = temp%m
        
        if(m==0){
            break
        }
    }
    answer = mn/n/6
    return answer
}