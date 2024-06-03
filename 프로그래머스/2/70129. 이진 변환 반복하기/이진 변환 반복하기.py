def solution(s):
    answer = []
    times, count = 0,0
    while s != '1':
        times +=1
        count += s.count('0')
        s = bin(len(s) - s.count('0'))[2:]
    return [times, count]