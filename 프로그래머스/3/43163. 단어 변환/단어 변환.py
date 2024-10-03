from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    q = deque([(begin, 0, [])])
    ll = len(target)
    while q:
        (nex, count, visited) = q.popleft()
        if nex == target:
            return count
        for w in words:
            check = 0
            for i in range(ll):
                if w[i] != nex[i]:
                    check += 1
            if check == 1 and w not in visited:
                visited.append(w)
                q.append((w,count+1,visited))
    return 0