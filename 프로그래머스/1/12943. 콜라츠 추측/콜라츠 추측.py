def solution(num):
    return dfs(num, 0)

def dfs(n, answer):
    if answer == 500:
        return -1
    if n == 1:
        return answer
    
    if n % 2 == 0:
        return dfs(int(n/2), answer+1)
    else:
        return dfs(int(n*3+1), answer+1)