import math
N, S = map(int, input().split())
A_arr = list(map(lambda x: abs(int(x)-S), input().split()))
g = math.gcd(*A_arr)
print(g)
