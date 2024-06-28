n = list(map(int, input().split()))
last = 0
for x in n:
    last += x**2
print(last%10)