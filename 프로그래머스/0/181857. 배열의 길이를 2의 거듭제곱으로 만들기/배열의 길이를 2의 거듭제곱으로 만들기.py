import math
def solution(arr):
    answer = []
    square = math.log(len(arr), 2)
    num = math.floor(square)
    if square == num:
        return arr
    else:
        while square < num+1:
            arr.append(0)
            square = math.log(len(arr), 2)
    return arr