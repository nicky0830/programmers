def solution(today, terms, privacies):
    answer = []
    def to_days(date):
        [y, m, d]= list(map(int, date.split('.')))
        return d + m * 28 + y * 12 * 28
    add_months = {t[0]:int(t[2:]) for t in terms}
    print(add_months)
    for i,p in enumerate(privacies):
        if to_days(p[:-2]) + add_months[p[-1]]*28 <= to_days(today):
            answer.append(i+1)
    answer.sort()
    return answer