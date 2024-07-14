n, b = map(int, input().split())
s = ''
for i in range(b):
    if i < 10:
        s += str(i)
    else:
        s += chr(ord('A') + i-10)
answer = ''
while n > 0:
    answer = s[n%b] + answer
    n = n // b
print(answer)