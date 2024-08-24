def solution(dirs):
    row, col = 0, 0
    arr = []
    for d in dirs:
        start_r, start_c = row, col
        if d == "U" and row < 5:
            row +=1
        if d == "D" and row > -5:
            row -= 1
        if d == "R" and col < 5:
            col += 1
        if d == "L" and col > -5:
            col -= 1
        if (start_c, start_r, col, row) not in arr and (start_c, start_r) != (col,row) and (col, row, start_c, start_r) not in arr:
            arr.append((start_c, start_r, col, row))
    return len(arr)