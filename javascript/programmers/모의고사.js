function solution(answers) {
  let arr = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];
  let count = [0, 0, 0];
  let max = 0;
  var answer = [];

  for (let i = 0; i < answers.length; i++) {
    if (answers[i] === arr[0][i % 5]) {
      count[0] += 1;
    }
    if (answers[i] === arr[1][i % 8]) {
      count[1] += 1;
    }
    if (answers[i] === arr[2][i % 10]) {
      count[2] += 1;
    }
  }

  for (let i = 0; i < count.length; i++) {
    if (count[i] > max) {
      max = count[i];
    }
  }

  for (let i = 0; i < count.length; i++) {
    if (count[i] === max) {
      answer.push(i + 1);
    }
  }
  return answer;
}
