import math
from itertools import combinations
n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    count = arr[0]
    answer = 0
    for c in combinations(arr[1:],2):
        a,b = c
        answer += math.gcd(a,b)
    print(answer)