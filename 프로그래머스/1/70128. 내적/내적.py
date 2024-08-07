def solution(a, b):
    answer = 0
    for i in range(len(a)):
        check = a[i]*b[i]
        answer += check
    return answer