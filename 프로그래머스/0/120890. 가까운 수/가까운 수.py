import math
def solution(array, n):
    answer = []
    minNum = 100
    minEl = 0
    for a in array: 
        if minNum > abs(a-n): 
            minNum = abs(a-n)
            minEl = a
        elif minNum == abs(a-n): 
            minEl = min([minEl, a])
#     index는 처음 찾은 값
    return minEl