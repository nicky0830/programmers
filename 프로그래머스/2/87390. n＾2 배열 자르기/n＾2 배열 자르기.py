def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        row, col = i//n, i%n
        m = max(row, col)
        answer.append(m+1)
    return answer