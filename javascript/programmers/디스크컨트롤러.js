function solution(jobs) {
  var answer = 0;
  let now = 0;
  let start = 0;
  let arry = [...jobs];

  while (arry.length !== 0) {
    if (arry[0][0] < now) {
      arry.sort((a, b) => {
        if (a[0] < now && b[0] < now) {
          return a[1] - b[1];
        }
      });
      answer += now - arry[0][0];
    } else {
      arry.sort((a, b) => {
        if (a[0] === b[0]) return a[1] - b[1];
        else return a[0] - b[0];
      });
      now += arry[0][0] - now;
    }

    start = arry[0][0];
    now += arry[0][1];
    answer += arry[0][1];
    arry.shift();
  }
  answer = parseInt(answer / jobs.length);
  return answer;
}
