def solution(s):
    answer = 0
    next = False
    s = s.split(' ')
    for i in range(len(s)-1,-1,-1):
        if s[i] == 'Z':
            next = True
        else:
            if not next:
                answer += int(s[i])
            next = False
    return answer