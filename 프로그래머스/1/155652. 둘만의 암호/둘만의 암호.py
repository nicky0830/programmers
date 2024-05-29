def solution(s, skip, index):
    answer = ''
    for a in s:
        count = 0
        for i in range(ord(a)+1, ord(a)+index+1):
            check = ''
            if i>ord('z'):
                check = chr(i-ord('z')+ord('a')-1)
            else:
                check = chr(i)
            if check in skip:
                count += 1
        end = ord(a)+index+count
        if end > ord('z'):
            end = end - ord('z') + ord('a') - 1
        answer += chr(end)
    return answer