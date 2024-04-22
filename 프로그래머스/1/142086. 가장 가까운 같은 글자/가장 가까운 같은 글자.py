def solution(s):
    answer = []
    dic = {}
    for i,m in enumerate(s):
        if m in dic:
            answer.append(i - dic[m])
        else:
            answer.append(-1) 
        dic[m] = i
    return answer