def solution(arr, k):
    answer = []
    for a in arr:
        if k > 0:
            if a not in answer:
                answer.append(a)
                k -= 1
    if k>0:
        answer += [-1] * k
    return answer