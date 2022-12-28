function solution(people, limit) {
  var answer = 0;
  let a = 0;
  let b = people.length - 1;

  people.sort((a, b) => {
    return b - a;
  });

  while (a < b) {
    if (people[a] + people[b] > limit) {
      a++;
    } else {
      a++;
      b--;
    }
    answer++;
  }
  if (a === b) answer++;

  return answer;
}
