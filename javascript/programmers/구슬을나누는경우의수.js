function solution(balls, share) {
    var answer = BigInt(1);
    let a = BigInt(1);
    let b = BigInt(1);
    for(let i=1; i<=balls; i++){
        answer*=BigInt(i)
    }
    for(let z=1; z<=(balls-share); z++){
        a*=BigInt(z)
    }
    for(let h=1; h<=share; h++){
        b*=BigInt(h)
    }
    answer = answer/(a*b)
    return BigInt(answer);
}
