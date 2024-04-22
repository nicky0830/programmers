def solution(num_list, n):
    answer = []
    m = 0
    while m < len(num_list):
        answer.append(num_list[m: m+n])
        m = m + n
    return answer