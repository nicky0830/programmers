import collections
def solution(want, number, discount):
    answer = 0
    z = dict(zip(want, number))
    c = collections.Counter(discount)
    start = 0
    while start <= len(discount) - 10:
        new_z = z.copy()
        for d in discount[start:start+10]:
            if d in new_z and new_z[d] > 0:
                new_z[d] -= 1
        last = list(filter(lambda x: x != 0, new_z.values()))
        if len(last) == 0:
            answer += 1
        start += 1
    return answer