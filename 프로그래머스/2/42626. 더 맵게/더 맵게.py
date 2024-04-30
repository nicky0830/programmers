from heapq import *
def solution(heap, K):
    answer = 0
    heapify(heap)
    while heap[0] < K:
        first = heappop(heap)
        second = heappop(heap)
        heappush(heap, first + second * 2)
        answer += 1
        if len(heap) == 1 and heap[0] < K:
            return -1
    return answer