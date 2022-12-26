function solution(number, k) {
  var answer = [];
  let index = 0;
  let max = 0;
  number = [...number];

  while (answer.length !== number.length - k) {
    answer[index] = "0";

    for (let i = max; i <= number.length - (number.length - k) + index; i++) {
      if (answer[index] < number[i]) {
        answer[index] = number[i];
        max = i + 1;
      }
      if (number[i] === "9") break;
    }
    index++;
  }
  answer = answer.join("");
  return answer;
}
