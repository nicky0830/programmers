def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    count = 0
    while count < len(word):
        for i in range(5 - count):
            answer += alpha.index(word[count]) * (5 ** (i))
        answer += 1
        count += 1
    return answer