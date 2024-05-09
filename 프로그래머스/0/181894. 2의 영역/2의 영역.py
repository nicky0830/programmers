def solution(arr):
    answer = []
    if 2 not in arr:
        return [-1]
    left = arr.index(2)
    right = arr[::-1].index(2)
#   0이면 -0이어서 틀림
    if not right:
        return arr[left:]
    return arr[left:-right]