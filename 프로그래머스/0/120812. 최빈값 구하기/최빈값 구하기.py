def solution(array):
    answer = 0
    while len(array) != 0:
        for i, a in enumerate(set(array)):
#           집합을 기준으로 for문을 돌아서 한번씩 다 삭제
#           삭제된 배열이 다시 집합이 되어 하나라도 더 개수가 많은 값만 남게 된다
            array.remove(a)
        if i == 0:
            return a
    return -1
# len(array)가 0이면 최빈값의 개수가 같다는 것
    return answer