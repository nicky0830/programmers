from itertools import permutations

N,M = map(int, input().split())
arr = [str(i) for i in range(1,N+1)]
answer = list(permutations(arr, M))
answer.sort()

for x in answer:
    print(' '.join(list(x)))