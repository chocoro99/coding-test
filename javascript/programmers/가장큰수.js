function solution(numbers) {
  let answer = "";
  let num = 0;

  numbers.sort((a, b) => {
    numA = parseInt(String(a) + String(b));
    numB = parseInt(String(b) + String(a));
    return numB - numA;
  });
  for (let i = 0; i < numbers.length; i++) {
    num += numbers[i];
  }
  if (num === 0) answer = "0";
  else answer = numbers.join("");
  return answer;
}
