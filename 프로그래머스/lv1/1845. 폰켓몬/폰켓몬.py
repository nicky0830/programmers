def solution(nums):
    answer = 0
    dic = {}
    for n in nums:
        if n in dic: 
            dic[n] = dic[n]+1
        else: 
            dic[n] = 0
    if len(list(dic.keys())) >= len(nums)/2: 
        return len(nums)/2 
    else: 
        return len(list(dic.keys()))
        