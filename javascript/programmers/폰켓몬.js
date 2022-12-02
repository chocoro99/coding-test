function solution(nums) {
  var answer = 0;
  let arr = [];

  for (let i = 0; i < nums.length; i++) {
    if (!arr.includes(nums[i])) {
      arr.push(nums[i]);
    }
  }
  if (parseInt(nums.length / 2) >= arr.length) {
    answer = arr.length;
  } else answer = parseInt(nums.length / 2);
  return answer;
}
