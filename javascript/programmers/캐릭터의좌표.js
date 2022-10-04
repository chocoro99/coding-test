function solution(keyinput, board) {
    var answer = [];
    let x = 0;
    let y = 0;
    
    for(let i=0; i<keyinput.length; i++){
        if(keyinput[i] == "right" & x+1 <= (board[0]-1)/2){
            x += 1
        }
        if(keyinput[i] == "left" & x-1 >= -((board[0]-1)/2)){
            x -= 1
        }
        if(keyinput[i] == "up" & y+1 <= (board[1]-1)/2){
            y += 1
        }
        if(keyinput[i] == "down" & y-1 >= -((board[1]-1)/2)){
            y -= 1
        }            
    }
    answer.push(x,y)
    return answer;
}