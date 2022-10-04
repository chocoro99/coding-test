function solution(price) {
    let answer = price;
    if(price>=100000 & price < 300000){
        answer = parseInt(price - price*5/100)
    }
    else if(price >= 300000 & price < 500000){
        answer = parseInt(price - price*10/100)
    }
    else if(price >= 500000){
        answer = parseInt(price - price*20/100)
    }
    return answer;
}