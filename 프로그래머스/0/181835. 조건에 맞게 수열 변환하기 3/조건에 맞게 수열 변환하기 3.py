def solution(arr, k):
    answer = []
    if k % 2 ==0:
        return list(map(lambda x: x+k, arr))
    else: 
        return list(map(lambda x: x*k, arr))