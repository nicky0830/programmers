from collections import Counter
def solution(want, number, discount):
    answer=0
    z = dict(zip(want, number))
    for i in range(len(discount)-9):
        if z == Counter(discount[i:i+10]):
            answer += 1
    return answer