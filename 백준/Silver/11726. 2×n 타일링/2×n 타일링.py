n = int(input())
arr = [0] * (n+1)

for i in range(n+1):
    if i == 1 or i == 2:
        arr[i] = i
    else:
        arr[i] = arr[i-1] + arr[i-2]
print(arr[n]%10007)