const inputs = require("fs")
  .readFileSync("./javascript/baekjoon/example.txt")
  .toString()
  .trim();

let right = 0;
let left = 0;

for (let i = 0; i < inputs.length / 2; i++) {
  right += parseInt(inputs[i]);
  left += parseInt(inputs[inputs.length / 2 + i]);
}

if (right === left) {
  console.log("LUCKY");
} else {
  console.log("READY");
}
