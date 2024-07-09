c,d = map(int, input().split())
def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b, a%b)

g = gcd(c, d)
l = c*d/g
print(g)
print(int(l))