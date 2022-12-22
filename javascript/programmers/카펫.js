function solution(brown, yellow) {
  var answer = [];
  let yellows = [];

  for (let i = 1; i <= Math.ceil(Math.sqrt(yellow)); i++) {
    if (yellow % i === 0) {
      yellows.push([yellow / i, i]);
    }
  }

  for (let i of yellows) {
    if ((i[0] + 2) * (i[1] + 2) === brown + yellow) {
      answer.push(i[0] + 2, i[1] + 2);
      break;
    }
  }
  return answer;
}
