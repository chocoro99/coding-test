function solution(k, dungeons) {
  var answer = 0;

  const count = (a, dungeon, p) => {
    for (let i = 0; i < dungeon.length; i++) {
      const energy = dungeon[i][0];
      const useEnergy = dungeon[i][1];
      if (energy > a || a < useEnergy) continue;
      const remainingDungeon = [
        ...dungeon.slice(0, i),
        ...dungeon.slice(i + 1),
      ];
      count(a - useEnergy, remainingDungeon, p + 1);
    }
    return (answer = Math.max(p, answer));
  };
  count(k, dungeons, 0);

  return answer;
}
