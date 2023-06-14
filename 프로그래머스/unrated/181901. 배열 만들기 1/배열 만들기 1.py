def solution(n, k):
    answer = []
    check = 1
    while check*k <= n: 
        answer.append(check * k)
        check +=1
    return answer