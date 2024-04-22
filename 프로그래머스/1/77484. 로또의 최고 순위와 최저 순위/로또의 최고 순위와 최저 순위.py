def solution(lottos, win_nums):
    answer = []
    count = 0
    zeros = 0
    for l in lottos:
        if l in win_nums:
            count += 1
        if l == 0:
            zeros += 1
    return list(map(lambda x: 6 if(7 - x > 6) else 7-x ,[zeros+count, count]))