n = int(input())
answer = []
arr = [300,60,10]
for a in arr:
    x = n // a
    answer.append(str(x))
    n = n - a * x
if n > 0:
    print(-1)
else: 
    print(' '.join(answer))