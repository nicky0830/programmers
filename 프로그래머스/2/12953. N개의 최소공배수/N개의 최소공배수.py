import math
def solution(arr):
    answer = arr[0]
    for a in arr[1:]:
        answer = int( answer * a / math.gcd(answer, a))
    return answer