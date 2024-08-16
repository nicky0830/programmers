def solution(citations):
    answer = 0
    for h in range(max(citations), -1, -1):
        count = 0
        for c in citations:
            if c >= h:
                count +=1
        if count >= h:
            answer = h
            break
    return answer