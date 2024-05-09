def solution(ineq, eq, n, m):    
    if n == m:
        if eq == '!':
            return 0
        else:
            return 1
    if ineq == '<':
        if n > m:
            return 0
    if ineq == '>':
        if n < m:
            return 0
    return 1