from itertools import combinations
def solution(numbers, target):
    answer = 0
    minus = (sum(numbers) - target)/2
    f = list(filter(lambda x: x<= minus, numbers))
    for i in range(len(f)):
        c = list(combinations(f, i+1))
        for j in c:
            if sum(j) == minus:
                answer += 1
    return answer