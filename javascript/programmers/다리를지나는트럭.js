function solution(bridge_length, weight, truck_weights) {
  var answer = 0;
  let trucksWeight = 0;
  let count = 0;
  let index = 0;
  let time = [];

  while (truck_weights.length !== count) {
    if (answer === time[0]) {
      time.shift();
      trucksWeight -= truck_weights[count];
      count++;
    }
    if (weight - trucksWeight >= truck_weights[index]) {
      trucksWeight += truck_weights[index];
      time.push(bridge_length + answer);
      index++;
    }
    answer++;
  }
  return answer;
}
