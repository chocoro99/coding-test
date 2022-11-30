function solution(priorities, location) {
  var answer = 0;
  let arr = [...priorities];
  arr.sort((a, b) => {
    return b - a;
  });

  while (true) {
    if (priorities[0] === arr[0] && location === 0) {
      answer++;
      break;
    } else if (priorities[0] === arr[0]) {
      priorities.shift();
      arr.shift();
      location--;
      answer++;
    } else {
      priorities.push(priorities[0]);
      priorities.shift();
      location--;
    }
    if (location < 0) location = priorities.length - 1;
  }
  return answer;
}
