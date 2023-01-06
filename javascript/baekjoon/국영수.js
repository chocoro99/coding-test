const inputs = require("fs")
  .readFileSync("./javascript/baekjoon/example.txt")
  .toString()
  .trim()
  .split("\n");
const [n, ...info] = inputs;

let answer = [];
let arr = [];
info.map((e) => {
  arr.push(e.split(" "));
});

arr.sort((a, b) => {
  if (a[1] !== b[1]) return b[1] - a[1];
  else {
    if (a[2] !== b[2]) return a[2] - b[2];
    else {
      if (a[3] !== b[3]) return b[3] - a[3];
      else {
        if (a[0] > b[0]) return 1;
        else return -1;
      }
    }
  }
});

for (let i in arr) {
  answer.push(arr[i][0]);
}
console.log(answer.join("\n"));
