import math
m,n = map(int, input().split())
def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, math.ceil(math.sqrt(num))+1):
            if num != i and num % i == 0:
                return False
        return True
for x in range(m, n+1):
    if isPrime(x):
        print(x)