def solution(n, computers):    
    def BFS(node, visit):
        que = [node]
        visit[node] = 1
        while que:
            v = que.pop(0)
#           현재 노드
            for i in range(n):
                if computers[v][i] == 1 and visit[i] == 0:
#                현재 노드 연결 노드 + 방문 안한 노드
                    visit[i] = 1
                    que.append(i)
        return visit
#     visit 갱신
    visit = [0 for i in range(n)]
    answer = 0
    for i in range(n):
        try:
            visit = BFS(visit.index(0), visit)
#           visit 값을 계속 갱신, 새로바뀐 visit 중 안 방문한 첫번째 값을 node로(시작 노드)
            answer += 1
        except:
#           visit에 0이 없을 때
            break
    return answer