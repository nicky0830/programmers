import heapq
n = int(input())
arr = []
for i in range(n):
    heapq.heappush(arr, int(input()))
count = 0
while len(arr) != 1:
    temp = heapq.heappop(arr) + heapq.heappop(arr)
    count += temp
    heapq.heappush(arr, temp)

print(count)