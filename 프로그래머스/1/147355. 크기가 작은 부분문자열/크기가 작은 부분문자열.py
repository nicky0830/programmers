def solution(t, p):
    answer = 0
    l = len(p)
    start = 0
    end = start+l
    arr = []
    while end<=len(t):
        if int(t[start:end]) <= int(p):
            arr.append(t[start:end])
        start += 1
        end = start + l
    return len(arr)