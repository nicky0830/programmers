N = int(input())
R = list(map(int, input().split(' ')))
L = list(map(int, input().split(' ')))[:-1]
min_idx = len(L)
answer = 0
while min_idx > 0:
    min_L = min(L)
    min_idx = L.index(min_L)
    answer += min_L * sum(R[min_idx:])
    R = R[:min_idx]
    L = L[:min_idx]
print(answer)