function solution(keyinput, board) {
    const [row,col] = [Math.floor(board[0]/2), Math.floor(board[1]/2)]
    let [r,c] = [0,0]
    for (let key of keyinput) {
        if (key == 'left' && r > -row) r -=1
        if (key == 'right' && r < row) r += 1
        if (key == 'up' && c < col) c += 1
        if (key== 'down' && c > -col) c -= 1
     }
    return [r,c];
}