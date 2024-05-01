def solution(score):
    answer = []
    score_list = sorted(list(map(lambda x: sum(x), score)), reverse=True)
    for s in score:
        answer.append(score_list.index(sum(s))+1)
    return answer