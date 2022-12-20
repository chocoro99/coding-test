function solution(n, lost, reserve) {
  var answer = 0;
  answer = n - lost.length;

  for (let i = 0; i < lost.length; i++) {
    if (reserve.indexOf(lost[i]) !== -1) {
      reserve.splice(reserve.indexOf(lost[i]), 1);
      lost.splice(i, 1);
      i--;
      answer++;
    }
  }

  lost.sort((a, b) => {
    return a - b;
  });
  reserve.sort((a, b) => {
    return a - b;
  });

  for (let i = 0; i < lost.length; i++) {
    if (reserve.indexOf(lost[i] - 1) !== -1) {
      answer++;
      reserve.splice(reserve.indexOf(lost[i] - 1), 1);
    } else if (reserve.indexOf(lost[i] + 1) !== -1) {
      answer++;
      reserve.splice(reserve.indexOf(lost[i] + 1), 1);
    }
  }
  return answer;
}
