import math
n = int(input())
arr = list(map(int, input().split()))
answer = 0
def isPrime(m):
    if m == 1:
        return False
    for a in range(2, math.ceil(math.sqrt(m))+1):
        if m!= a and m%a == 0:
            return False
    return True
for a in arr:
    if isPrime(a):
        answer += 1
print(answer)