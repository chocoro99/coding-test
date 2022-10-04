function solution(cipher, code) {
    let answer = ''
    
    for(let i=code-1; i<cipher.length; i+=code){
        answer = answer + cipher[i]
    }
    return answer;
}