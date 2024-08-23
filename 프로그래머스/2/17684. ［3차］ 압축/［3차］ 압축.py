from string import ascii_uppercase
def solution(msg):
    answer = []
    d = {a:i+1 for i, a in enumerate(ascii_uppercase)}
    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1,len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d) + 1
                msg = msg[i-1:]
                break
    return answer

# def solution(msg):
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
#     answer = []

#     while True:
#         if msg in d:
#             answer.append(d[msg])
#             break
#         for i in range(1, len(msg)+1):
#             if msg[0:i] not in d:
#                 answer.append(d[msg[0:i-1]])
#                 d[msg[0:i]] = len(d)+1
#                 msg = msg[i-1:]
#                 break

#     return answer