function solution(my_string) {
    let answer = 0;
    let strArr = my_string.split(/[a-z]/gi)
    let newArr = strArr.filter((element) => {
        return element !== '';
    });
    for(let i of newArr){
        answer+=parseInt(i)
    }
    return answer;
}