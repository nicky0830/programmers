n = int(input())
answer = [[0 for _ in range(3)] for _ in range(n+1)]

for j in range(1, n+1):
    arr = list(map(int, input().split()))
    answer[j][0] = arr[0] + min(answer[j-1][1], answer[j-1][2])
    answer[j][1] = arr[1] + min(answer[j-1][0], answer[j-1][2])
    answer[j][2] = arr[2] + min(answer[j-1][0], answer[j-1][1])

print(min(answer[n]))