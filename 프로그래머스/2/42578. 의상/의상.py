def solution(clothes):
    answer = 1
    dic = {}
    for [cloth,kind] in clothes:
        if kind in dic:
            dic[kind] += 1
        else:
            dic[kind] = 1
    for value in dic.values():
        answer *= (value + 1)
    return answer -1 