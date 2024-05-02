def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    common = set(lost) & set(reserve)
    lost = list(set(lost) - common)
    for r in list(set(reserve) - common):
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    return n - len(lost)