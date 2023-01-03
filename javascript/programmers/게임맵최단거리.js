function solution(maps) {
  let answer = 1;
  let queue = [];
  let visited = maps;
  const dx = [1, -1, 0, 0];
  const dy = [0, 0, 1, -1];
  const x = maps.length;
  const y = maps[0].length;

  queue.push([0, 0]);
  visited[0][0] = 0;

  while (queue.length !== 0) {
    let length = queue.length;

    for (let i = 0; i < length; i++) {
      const n = queue[0][0];
      const m = queue[0][1];
      queue.shift();

      for (let z = 0; z < 4; z++) {
        const nx = n + dx[z];
        const ny = m + dy[z];
        if (nx >= 0 && nx < x && ny >= 0 && ny < y && visited[nx][ny] === 1) {
          if (nx === x - 1 && ny === y - 1) {
            answer++;
            return answer;
          }
          queue.push([nx, ny]);
          visited[nx][ny] = 0;
        }
      }
    }
    answer++;
  }
  return -1;
}
