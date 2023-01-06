const inputs = require("fs")
  .readFileSync("./javascript/baekjoon/example.txt")
  .toString()
  .trim();

let one = inputs.split(0).filter((element) => {
  return element !== undefined && element !== null && element !== "";
});
let zero = inputs.split(1).filter((element) => {
  return element !== undefined && element !== null && element !== "";
});

if (one.length > zero.length) console.log(zero.length);
else console.log(one.length);
