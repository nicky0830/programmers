import collections
def solution(k, tangerine):
    answer = 0
    count = collections.Counter(tangerine)
    for v in sorted(count.values(), reverse=True):
        k -= v
        answer += 1
        if k <= 0:
            return answer 
    return answer