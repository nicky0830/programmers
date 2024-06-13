def solution(board, h, w):
    count = 0
    dh =  [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    n = len(board)
    for i in range(4):
        h_check = h+dh[i]
        w_check = w+dw[i]
        if h_check >= 0 and h_check < n and w_check >= 0 and w_check < n:
            if board[h_check][w_check] == board[h][w]:
                count += 1
    return count