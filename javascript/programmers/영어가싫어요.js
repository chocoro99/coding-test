function solution(numbers) {
    var answer = '';
    let a = ''
    let number = {zero:0, one:1, two:2, three:3, four:4, five:5, six:6, seven:7, eight:8, nine:9}
    for(let i=0; i<numbers.length; i++){
        a = a + numbers[i]
        if(number[a] || number[a] == 0){
            answer += String(number[a])
            a = ''
        }
    }
    return parseInt(answer);
}