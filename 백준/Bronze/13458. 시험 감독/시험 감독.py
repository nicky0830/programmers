import math
N = int(input())
A = list(map(int, input().split()))
B,C = map(int, input().split())
answer = []

for a in A:
    if a > B:
        answer.append(math.ceil((a-B)/C))
print(sum(answer)+N)
