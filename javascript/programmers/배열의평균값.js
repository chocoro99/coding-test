function solution(numbers) {
    let answer = 0
    for (let i of numbers){    
        answer += i       
    }
    answer = answer/(numbers.length)
    return answer;
}

console.log(solution([1,2,3,4,5,6,7,8,9,10]))