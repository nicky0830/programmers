import math
def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow**0.5)+1):
        if yellow % i == 0 and brown == (i+yellow/i+2)*2:
            return [yellow/i+2,i+2]
    return answer