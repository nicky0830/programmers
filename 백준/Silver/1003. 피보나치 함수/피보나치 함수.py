from collections import defaultdict
dic = defaultdict(int)
dic[0] = 0
dic[1] = 1
count = {0:{0:1, 1:0}, 1:{0:0, 1:1}}
m = int(input())
for i in range(m):
    word = int(input())
    n = 2
    while n <= word:
        dic[n] = dic[n-1] + dic[n-2]
        count[n] = {
            0: count[n-1][0] + count[n-2][0],
            1: count[n-1][1] + count[n-2][1]
        }
        n += 1
    print(f'{count[word][0]} {count[word][1]}')