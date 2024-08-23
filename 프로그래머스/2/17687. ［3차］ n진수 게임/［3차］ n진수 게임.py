def solution(n, t, m, p):
    notation = '0123456789ABCDEF'
    def change(num, n):
        answer = ''
        while num > 0:
            answer += str(notation[num % n])
            num = num // n
        return answer[::-1]
    
    c = change(16, 2)
    answer = '0'
    start = 1
    result = ''
    while len(answer) <= t*m:
        answer += change(start, n)
        start += 1
    for i in range(t):
        result += answer[p-1]
        p += m
    return result
