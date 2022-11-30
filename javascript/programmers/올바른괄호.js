function solution(s) {
  var answer = true;
  let index = 0;
  let count = 0;

  while (index < s.length) {
    if (s[index] === "(") count++;
    else count--;
    if (count < 0) {
      break;
    }
    index++;
  }
  if (count === 0) answer = true;
  else answer = false;

  return answer;
}
