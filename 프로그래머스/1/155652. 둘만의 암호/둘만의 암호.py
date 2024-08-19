def solution(s, skip, index):
    answer = ''
    avoid = [ord(s) for s in skip]
    for x in s:
        x = ord(x)
        for i in range(index):
            x += 1
            while x > ord('z') or x in avoid:
                if x > ord('z'): 
                    x = x - ord('z') + ord('a') - 1
                if x in avoid:
                    x += 1
        answer += chr(x)
    return answer