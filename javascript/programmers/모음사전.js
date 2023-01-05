function solution(word) {
  let answer = 0;
  for (let i = 0; i < word.length; i++) {
    if (word[i] === "A") answer++;
    else if (word[i] === "E") answer += parseInt(3905 / 5 ** (i + 1)) + 1;
    else if (word[i] === "I") answer += parseInt(3905 / 5 ** (i + 1)) * 2 + 1;
    else if (word[i] === "O") answer += parseInt(3905 / 5 ** (i + 1)) * 3 + 1;
    else if (word[i] === "U") answer += parseInt(3905 / 5 ** (i + 1)) * 4 + 1;
  }
  return answer;
}
