function solution(sizes) {
  var answer = 0;
  let maxArr = [];
  let minArr = [];

  for (let i = 0; i < sizes.length; i++) {
    if (sizes[i][0] > sizes[i][1]) {
      maxArr.push(sizes[i][0]);
      minArr.push(sizes[i][1]);
    } else {
      maxArr.push(sizes[i][1]);
      minArr.push(sizes[i][0]);
    }
  }
  answer = Math.max(...maxArr) * Math.max(...minArr);
  return answer;
}
