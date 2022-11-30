function solution(progresses, speeds) {
  var answer = [];
  let day = [];
  let count = 0;
  let max = 0;

  for (let i = 0; i < speeds.length; i++) {
    let z = 100 - progresses[i];
    if (z % speeds[i] !== 0) day.push(parseInt(z / speeds[i]) + 1);
    else day.push(z / speeds[i]);
  }

  max = day[0];

  for (let i = 0; i < day.length; i++) {
    if (day[i] > max) {
      max = day[i];
      answer.push(count);
      count = 0;
    }

    count++;
    if (day.length - 1 === i) {
      answer.push(count);
    }
  }

  return answer;
}
