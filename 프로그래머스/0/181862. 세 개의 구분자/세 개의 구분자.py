def solution(myStr):
    answer = []
    short = ''
    for m in myStr:
        if m not in 'abc':
            short += m
        elif short != '':
            answer.append(short)
            short = ''
    if short:
        answer.append(short)
    if len(answer) == 0:
        answer.append('EMPTY')
    return answer