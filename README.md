# programmers
This is a auto push repository for Baekjoon Online Judge created with [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub).

# 자료구조
## dfs
```python
  graph = [
    [],
    [2,3,8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
  ]

  # 인접 행렬
  visited = [False] * node 개수
  def dfs(visited, node):
    visited[node] = True
    for g in graph[node]:
      if not visited[g]:
        dfs(visited, g)
  dfs(graph, 1, visited)
```

# 다시 풀어야 하는 문제들
## 1. 문자열 다루기
- [문자열 밀기](https://github.com/nicky0830/programmers/commit/47758fbf61f1e57f6bd5269689f5328b4c1c57fc)
- [옹알이](https://school.programmers.co.kr/app/courses/17584/curriculum/lessons/197243#part-46571)

## 2. 구현
- [연속된 수의 합](https://school.programmers.co.kr/app/courses/17584/curriculum/lessons/197245)
- [치킨 쿠폰](https://school.programmers.co.kr/app/courses/17584/curriculum/lessons/197246#part-46572)
- [바탕화면 정리](https://github.com/nicky0830/programmers/commit/fdf82ee0a1bca2b009a899e459434c2358ab5780)

## 3. 딕셔너리
- [숫자 문자열과 영단어](https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=python3)
- [전화번호 목록](https://school.programmers.co.kr/learn/courses/30/lessons/42577?language=python3)

## 4.셋
- [신고 받기](https://school.programmers.co.kr/learn/courses/30/lessons/92334?language=python3)

## 5. 힙
- [명예의 전당](https://school.programmers.co.kr/tryouts/85933/challenges?language=python3)
- [더 맵게](https://school.programmers.co.kr/tryouts/85934/challenges)
