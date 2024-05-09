def solution(arr, queries):
    answer = []
    for q in queries:
        [s,e, k] = q
        check = list(filter(lambda x: x > k , arr[s:e+1]))
        if check:
            num = min(check)
        else:
            num = -1
        answer.append(num)
    return answer