def solution(s):
    answer = ''
    start = True
    for x in s:
        if x == ' ':
            start = True
            answer += x
        else:
            if start:
                answer += x.upper()
            else:
                answer += x.lower()
            start = False
    return answer