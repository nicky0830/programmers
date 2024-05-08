def solution(numLog):
    answer = ''
    last = numLog[0]
    for n in numLog[1:]:
        if n - last ==1:
            answer += 'w'
        if n -last == -1:
            answer += 's'
        if n - last == 10:
            answer += 'd'
        if n -last == -10:
            answer += 'a'
        last = n
    return answer