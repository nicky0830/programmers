def solution(prices):
    answer = [0] * len(prices) 
    for i, p in enumerate(prices):
        for j in range(i+1 , len(prices)):
            if p <= prices[j]:
                answer[i] += 1
            #price drops 
            else: 
                answer[i] = j - i
                break 
    return answer