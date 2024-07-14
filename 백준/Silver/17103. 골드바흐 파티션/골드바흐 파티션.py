import sys

n = int(sys.stdin.readline())
cnt = [0] * 1000001
cnt[0] = 1
cnt[1] = 1

for i in range(2,1000001):
    if not cnt[i]:
        for j in range(2*i, 1000001, i):
            cnt[j] = 1
            
for _ in range(n):
    m = int(sys.stdin.readline())
    answer = 0
    for a in range(2, m//2+1):
        if cnt[a] == 0 and cnt[m-a]==0:
            answer +=1
    print(answer)