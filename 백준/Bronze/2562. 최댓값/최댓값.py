max_num = 0
max_idx = 0
for i in range(1, 10):
    x = int(input())
    if max_num < x:
        max_num = x
        max_idx = i
print(max_num)
print(max_idx)