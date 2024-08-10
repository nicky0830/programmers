from collections import deque
def solution(cacheSize, cities):
    q = deque()
    answer = 0
    for c in cities:
        c = c.upper()
        if cacheSize == 0:
            answer = 5 * len(cities)
        else:
            if c in q:
                q.remove(c)
                q.append(c)
                answer += 1
            else:
                answer += 5
                if cacheSize == len(q):
                    q.popleft()
                    q.append(c)
                else:
                    q.append(c)
    return answer