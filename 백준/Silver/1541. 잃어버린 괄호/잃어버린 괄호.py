n = input()
answer = 0
if '-' in n:
    arr = n.split('-')
    sum_arr = list(map(lambda x: sum(list(map(int, x.split('+')))), arr))
    answer = sum_arr[0]
    for s in sum_arr[1:]:
        answer -= s
else:
    answer = eval(n)
print(answer)