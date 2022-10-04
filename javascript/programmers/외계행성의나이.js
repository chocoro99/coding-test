function solution(age) {
    const number = ["a","b","c","d","e","f","g","h","i","j"]
    let ageL = [...String(age)]
    var answer = [];
    for(let i of ageL){
        answer.push(number[i])
    }
    answer = answer.join("")
    return answer;
}