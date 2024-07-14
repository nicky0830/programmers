n, b = input().split()
s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = 0
for i,x in enumerate(n[::-1]):
    answer += s.index(x) * int(b) ** i
print(answer)