from collections import Counter
def solution(participant, completion):
    count = Counter(participant)
    for c in completion:
        if count[c] >.0:
            count[c] -= 1
    for k,v in count.items():
        if v>0:
            return k

        

