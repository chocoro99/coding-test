function solution(participant, completion) {
  var answer = "";
  participant.sort();
  completion.sort();

  for (let i = 0; i < participant.length; i++) {
    if (i === participant.length - 1) {
      answer = participant[i];
      break;
    }
    if (participant[i] !== completion[i]) {
      answer = participant[i];
      break;
    }
  }
  return answer;
}
