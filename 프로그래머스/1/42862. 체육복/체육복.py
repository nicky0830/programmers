def solution(n, lost, reserve):
    answer = 0
    common = set(reserve) & set(lost)
    reserve = sorted(list(set(reserve) - set(common)))
    lost = sorted(list(set(lost) - set(common)))
    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
        elif r+1 in lost:
            lost.remove(r+1)
    return n - len(lost)