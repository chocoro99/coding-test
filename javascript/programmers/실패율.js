function solution(N, stages) {
  var answer = [];
  let fail = [];

  stages.sort((a, b) => {
    return a - b;
  });
  for (let i = 0; i < N; i++) {
    let count = 0;
    for (let z of stages) {
      if (i + 1 >= z) {
        count++;
      }
    }
    fail.push([count / stages.length, i + 1]);
    stages.splice(0, count);
  }
  fail.sort((a, b) => {
    return b[0] - a[0];
  });

  for (let i of fail) {
    answer.push(i[1]);
  }

  return answer;
}
