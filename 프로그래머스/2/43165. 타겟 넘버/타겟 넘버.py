def solution(numbers, target):
    global answer
    answer = 0
    def dfs(idx, total):
        global answer
        if idx == len(numbers)-1:
            if total == target:
                answer += 1
            return
        dfs(idx+1, total+numbers[idx+1])
        dfs(idx+1, total-numbers[idx+1])
        return 
    dfs(0,numbers[0])
    dfs(0,-1*numbers[0])
    return answer


