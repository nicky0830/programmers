from string import ascii_uppercase
def solution(msg):
    dic = {a: i+1 for i,a in enumerate(ascii_uppercase)}
    last = len(ascii_uppercase)+1
    answer = []
    pass_i = []
    for i in range(len(msg)):
        if i in pass_i:
            continue
        for j in range(len(msg), i, -1):
            letter = msg[i:j]
            if letter in dic:
                for k in range(i+1, j):
                    pass_i.append(k)
                answer.append(dic[letter])
                dic[msg[i:j+1]] = last
                last += 1
                break
    return answer