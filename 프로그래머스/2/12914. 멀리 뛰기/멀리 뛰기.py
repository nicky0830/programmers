def solution(n):
    answer = 0
    arr =[0 for i in range(n+1)]
    for i in range(1,n+1):
        if i == 1 or i == 2:
            arr[i] = i
        else:
            arr[i] = arr[i-1]+arr[i-2]
    return arr[n]%1234567