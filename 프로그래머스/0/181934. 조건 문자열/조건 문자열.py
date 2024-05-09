def solution(ineq, eq, n, m):
    if eq == '!':
        eq = ''
    print(eval(f'{n} {ineq}{eq} {m}'))
    return int(eval(f'{n} {ineq}{eq} {m}'))