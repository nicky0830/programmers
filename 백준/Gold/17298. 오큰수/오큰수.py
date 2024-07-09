N = int(input())
S = list(map(int, input().split()))
stack = []
result = [-1]*N
for i in range(N):
    while stack and S[stack[-1]] < S[i]:
        result[stack[-1]] = S[i]
        stack.pop()
    stack.append(i)
print(*result)