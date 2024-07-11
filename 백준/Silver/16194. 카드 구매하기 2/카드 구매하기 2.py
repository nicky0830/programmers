n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
sum_arr = [0] * (n+1)
sum_arr[0] = 0
for i in range(1, n+1):
    for j in range(0, i):
        new_sum = sum_arr[j] + arr[i-j]
        if sum_arr[i] == 0:
            sum_arr[i] = new_sum
        else:
            if sum_arr[i] > new_sum:
                sum_arr[i] = new_sum
print(sum_arr[n])