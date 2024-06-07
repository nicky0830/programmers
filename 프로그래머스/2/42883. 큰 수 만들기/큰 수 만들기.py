def solution(number, k):
    answer = ''
    while k > 0:
        if '9' in number[:k+1]:
            max_num = '9'
        else:
            max_num = max(number[:k+1])
        idx = number.index(max_num)
        k -= idx
        answer += max_num
        number = number[idx+1:]
        if len(number) == k:
            return answer
    return answer + ''.join(number)