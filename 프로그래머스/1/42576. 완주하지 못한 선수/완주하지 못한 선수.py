def solution(participant, completion):
    answer = ''
    p_dic = {i:0 for i in participant}
    c_dic = {i:0 for i in participant}
    for p in participant:
        p_dic[p] += 1
    for c in completion:
        c_dic[c] += 1
        
    for p in participant:
        if p_dic[p] - c_dic[p] == 1:
            return p