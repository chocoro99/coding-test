function solution(my_string) {
    let a = [...my_string]
    let answer = []
    for(let i=0; i < a.length; i++) {
        if(a[i] == a[i].toUpperCase()){
            answer.push(a[i].toLowerCase())
        }
        else{
            answer.push(a[i].toUpperCase())
        }
    }
    answer = answer.join("")
    return answer;
}