from collections import Counter
N = int(input())
S = list(map(int, input().split()))
C = Counter(S)
stack = []
result = [-1] * N
for i in range(N):
    while stack and C[S[stack[-1]]] < C[S[i]]:
        result[stack[-1]] = S[i]
        stack.pop()
    stack.append(i)
print(*result)