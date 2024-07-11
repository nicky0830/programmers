n = int(input())
arr = [0] * (n+1)

for i in range(n+1):
    if i == 1 or i == 0:
        arr[i] = 1
    else:
        arr[i] = arr[i-1] + arr[i-2] * 2
print(arr[n]%10007)