function solution(num_list) {
    let answer = [];
    let odd = 0;
    let even = 0;
    
    for(let i of num_list){
        if(i%2 == 0){
            even ++;
        }
        else{
            odd ++;
        }
    }
    answer.push(even)
    answer.push(odd)
    return answer;
}