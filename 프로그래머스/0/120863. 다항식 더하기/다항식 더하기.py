def solution(polynomial):
    answer = ''
    arr = polynomial.split(' + ')
    x=0
    num=0
    for a in arr:
        if 'x' in a:
            x_num = a.split('x')[0]
            if not x_num:
                x += 1
            else:
                x += int(x_num)
        else:
            num += int(a)
    if x > 0:
        if x == 1:
            answer += 'x'
        else:
            answer += str(x) + 'x'
        if num > 0:
            answer += ' + ' + str(num)
    elif num > 0:
        answer += str(num)
    return answer