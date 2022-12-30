function solution(genres, plays) {
  var answer = [];
  let rank = [];
  let song = {};

  for (let i = 0; i < genres.length; i++) {
    song[genres[i]] = [];
  }

  for (let i = 0; i < genres.length; i++) {
    song[genres[i]] = [...song[genres[i]], [plays[i], i]];
  }

  for (let i in song) {
    let sum = 0;
    song[i].sort((a, b) => {
      return b[0] - a[0];
    });
    for (let z = 0; z < song[i].length; z++) {
      sum += song[i][z][0];
    }
    rank.push([i, sum]);
  }
  rank.sort((a, b) => {
    return b[1] - a[1];
  });

  for (let i of rank) {
    if (song[i[0]].length >= 2) {
      for (let z = 0; z < 2; z++) {
        answer.push(song[i[0]][z][1]);
      }
    } else if (song[i[0]].length === 1) {
      answer.push(song[i[0]][0][1]);
    }
  }

  return answer;
}
