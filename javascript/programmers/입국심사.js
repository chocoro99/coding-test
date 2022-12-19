function solution(n, times) {
  var answer = 0;

  times.sort((a, b) => {
    return a - b;
  });
  let minTime = times[0];
  let maxTime = times[0] * n;

  while (true) {
    let count = 0;
    let mid = Math.floor((minTime + maxTime) / 2);

    for (let i of times) {
      count += Math.floor(mid / i);
    }

    if (count >= n) {
      maxTime = mid;
    } else if (count < n) {
      minTime = mid;
    }

    if (minTime == maxTime - 1) {
      answer = maxTime;
      break;
    }
  }

  return answer;
}
