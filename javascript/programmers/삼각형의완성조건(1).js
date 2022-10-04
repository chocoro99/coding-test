function solution(sides) {
    let sumNum = 0;
    let maxA = 0;
    let maxIndex = 0
    
    for(let i=0; i < 3; i++){
        if(sides[i] > maxA){
            maxA = sides[i]
            maxIndex = i
        }
    }
    for(let i=0; i < 3; i++){
        if(i != maxIndex){
            sumNum += sides[i]
        }
    }
    if(sumNum > maxA){
        return 1
    }
    else{
        return 2
    }
}