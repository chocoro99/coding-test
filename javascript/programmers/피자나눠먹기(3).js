function solution(slice, n) {
    if(slice >= n){
        return 1
    }
    else if(slice < n & n%slice == 0){
        return n/slice
    }
    else{
        return parseInt(n/slice)+1
    }
}