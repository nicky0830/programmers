def solution(elements):
    answer = 0
    ll = len(elements)
    s = set()
    for i in range(0, ll):
        ssum = elements[i]
        s.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            s.add(ssum)
    return len(s)