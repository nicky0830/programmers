def solution(start, end):
    answer = []
    while start <= end: 
        answer.append(start)
        start = start + 1
    return answer