from operator import itemgetter
def solution(genres, plays):
    answer = []
    dic = {}
    sum_dic = {}
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]].append((plays[i], i))
            sum_dic[genres[i]] += plays[i]
        else:
            dic[genres[i]] = [(plays[i], i)]
            sum_dic[genres[i]] = plays[i]
    for k,v in sorted(sum_dic.items(), key=itemgetter(1), reverse=True):
#       dict는 sorted를 적용할 때 items로 안하고 바로 사용하면 키를 기준으로 정렬한다
        count = 0
        for x,i in sorted(dic[k], key=lambda x: (-x[0], x[1])):
            if count < 2:
                answer.append(i)
                count += 1
    return answer