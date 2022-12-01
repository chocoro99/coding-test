function solution(numbers) {
  var answer = 0;
  let numbersArr = [...numbers];
  let array = [];
  let dupArray = [];

  const getPermutations = (arr, selectNum) => {
    const result = [];
    if (selectNum === 1) return arr.map((num) => [num]);

    arr.forEach((fix, index, array) => {
      const rest = [...array.slice(0, index), ...array.slice(index + 1)];
      const permutations = getPermutations(rest, selectNum - 1);
      const combine = permutations.map((permutation) => [fix, ...permutation]);
      result.push(...combine);
    });

    return result;
  };

  for (let i = 1; i <= numbersArr.length; i++) {
    array.push(...getPermutations(numbersArr, i));
  }

  for (let i = 0; i < array.length; i++) {
    const numArray = parseInt(array[i].join(""));

    if (!dupArray.includes(numArray) && numArray !== 0 && numArray !== 1) {
      dupArray.push(numArray);
    }
  }

  for (let i = 0; i < dupArray.length; i++) {
    let count = 0;
    for (let z = 2; z * z <= dupArray[i]; z++) {
      if (dupArray[i] % z === 0) count++;
    }
    if (count === 0) answer++;
  }

  return answer;
}
