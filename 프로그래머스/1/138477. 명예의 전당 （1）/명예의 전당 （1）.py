from heapq import *

def solution(k, score):
    answer = []
    q = []

    for s in score:
        heappush(q, s)
        if len(q) > k:
            p = heappop(q)
            answer.append(min(q))
        else:
            answer.append(min(q))
    return answer
