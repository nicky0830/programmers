n = int(input())
array = list(map(int, input().split()))

d = [0] * n
d[0] = array[0]
for i in range(1, n):
    d[i] = max(array[i], d[i-1]+array[i])
    # array[i]는 꼭 포함이 되어야 하니까
    # 시작인지 더해지는지 둘 중에 하나
print(max(d))