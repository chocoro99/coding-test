function solution(my_string) {
    let str = [...my_string]
    var answer = []
    for(let i of str){
        if(i>-1){
            answer.push(parseInt(i))
        }
    }
    answer.sort()
    return answer;
}