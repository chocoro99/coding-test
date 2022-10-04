function solution(hp) {
    let answer = 0;
    if((hp/5) > 0){
        answer += parseInt(hp/5)
        hp = hp%5
    }
    if((hp/3) > 0){
        answer += parseInt(hp/3)
        hp = hp%3
    }
    answer += hp
    return answer;
}