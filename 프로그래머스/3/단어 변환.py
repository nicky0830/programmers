from collections import deque
def solution(begin, target, words):
    global answer
    answer = []
    if target not in words:
        return 0
    words.append(begin)
    words.sort()
    def match(before, after):
        count = 0
        for i in range(len(begin)):
            if before[i] != after[i]:
                count +=1
        if count == 1:
            return True
    dic = {w:[] for w in words}
    for w in words:
        for word in words:
            if w != word and match(w, word):
                dic[w].append(word)
    visited = {w:False for w in words}
    
    global min_count
    min_count = len(words)
    global count_c
    count_c = 0
    
    def dfs(start):
        visited[start] = True
        global count_c, min_count
        count_c +=1
        if start == target:
            if min_count > count_c:
                min_count = count_c
        for x in dic[start]:
            if not visited[x]:
                dfs(x)
    dfs(begin)
    return min_count - 1
