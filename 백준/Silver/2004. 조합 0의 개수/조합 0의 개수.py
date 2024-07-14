n,m = map(int, input().split())
r = n-m
five_cnt, two_cnt = 0,0
five_n, five_m, five_r = n, m, r
two_n, two_m, two_r = n, m, r

while True:
    if five_n == 0 and five_m == 0 and five_r == 0:
        break
    five_n, five_m, five_r = five_n//5, five_m//5, five_r//5
    five_cnt = five_cnt + five_n - five_m - five_r
while True:
    if two_n == 0 and two_m == 0 and two_r == 0:
        break
    two_n, two_m, two_r = two_n//2, two_m//2, two_r//2
    two_cnt = two_cnt + two_n - two_m - two_r
print(min(five_cnt, two_cnt))