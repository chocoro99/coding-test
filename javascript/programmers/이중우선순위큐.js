function solution(operations) {
  var answer = [];
  let arryOperation = operations.map((e) => {
    return e.split(" ");
  });

  for (let i of arryOperation) {
    if (i[0] === "I") answer.push(parseInt(i[1]));
    else if (i[0] === "D" && answer.length !== 0) {
      if (i[1] === "1") {
        answer.splice(answer.indexOf(Math.max(...answer)), 1);
      } else {
        answer.splice(answer.indexOf(Math.min(...answer)), 1);
      }
    }
  }

  if (answer.length === 0) {
    answer = [0, 0];
  } else answer = [Math.max(...answer), Math.min(...answer)];
  return answer;
}
