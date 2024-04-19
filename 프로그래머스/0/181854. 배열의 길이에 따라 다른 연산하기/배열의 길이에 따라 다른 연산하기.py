def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        answer = [
            a+n if i % 2 != 0 else a
            for i,a in enumerate(arr)
        ]
    else:
        answer = [
            a+n if i % 2 == 0 else a
            for i,a in enumerate(arr)         
        ]
    return answer
