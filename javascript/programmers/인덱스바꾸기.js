function solution(my_string, num1, num2) {
    let strArray = [...my_string]
    let temp = strArray[num2]
    let answer = ''
    strArray[num2] = strArray[num1]
    strArray[num1] = temp
    answer = strArray.join("")
    return answer;
}