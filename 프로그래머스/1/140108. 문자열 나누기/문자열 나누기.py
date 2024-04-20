def solution(s):
    answer = 0
    x_count=0
    else_count=0
    for n in s: 
        if x_count == 0:
            x = n
        if n == x:
            x_count += 1
        else:
            else_count +=1
        if x_count == else_count:
            answer += 1
            x_count=0
            else_count=0
    if x_count > 0 or else_count > 0:
        answer += 1
    return answer