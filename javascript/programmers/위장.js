function solution(clothes) {
  var answer = 1;
  const hash = {};

  for (let i of clothes) {
    if (!hash[i[1]]) hash[i[1]] = 0;
    hash[i[1]] += 1;
  }

  const keys = Object.keys(hash);
  for (let i of keys) {
    answer = answer * (hash[i] + 1);
  }
  answer -= 1;

  return answer;
}
