const inputs = require("fs")
  .readFileSync("./javascript/baekjoon/example.txt")
  .toString()
  .trim()
  .split("\n");
const [n, home] = inputs;

const arr = [...home.split(" ")];
arr.sort((a, b) => {
  return a - b;
});

console.log(arr[parseInt((arr.length - 1) / 2)]);
