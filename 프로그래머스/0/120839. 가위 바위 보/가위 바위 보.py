def solution(rsp):
    answer = ''
    for r in rsp:
        if r == '2': 
            answer += '0'
        if r == '0':
            answer += '5'
        if r == '5':
            answer += '2'
#   2,0 0,5 5,2
    return answer