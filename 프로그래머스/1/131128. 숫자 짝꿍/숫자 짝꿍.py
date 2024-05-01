from collections import Counter
def solution(X, Y):
    answer = ''
    z = Counter(X) & Counter(Y)
#   set 교집합으로 구하려고 했는데 counter를 이용하면 교집합 + 개수까지 한번에 알 수 있음
    z = sorted([[k,v,k*v]for k,v in z.items()], key=lambda x: x[0], reverse=True)
#   개수만큼 종류별 string을 합칠 수 있다
    if not z:
        return "-1"
    answer = answer.join([x[2] for x in z]).lstrip('0')
    if answer == "":
        return "0"
    return answer