def solution(k, score):
    answer = []
    heap = []
    for i,s in enumerate(score):
        heap.append(s)
        heap.sort()
        heap = heap[-k:]
        answer.append(heap[0])
    return answer
            
        