def solution(clothes):
    answer = 1
    dic = {c[1]: [] for c in clothes}
    for c in clothes:
        dic[c[1]].append(c[0])
    for k,v in dic.items():
        answer *= (len(v) + 1)
    return answer - 1