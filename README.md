# programmers

# 알고리즘 
## 1. dfs
- 스택 자료구조 사용
- 깊이 우선 탐색
- 자신을 호출하는 함수
  
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
      # 해당 노드와 연결된 노드를 돈다
      # 가장 깊은 노드까지 반복
      # 더 이상 방문할 노드가 없으면 이전 노드의 연결 리스트로 돌아가게 됨
      #  : 이게 stack의 pop과 pop한 노드의 연결 리스트를 도는 것과 같음
      if not visited[g]:
        dfs(visited, g)
  dfs(visited, 1)
```

## 2. bfs
- 큐 자료구조 사용
- 넓이 우선 탐색

```python
  from collections from deque
  # collections는 기본 라이브러리라 코테에서 사용 가능

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
  def bfs(visited, start):
    queue = deque([start])
    visited[start] = True
    while queue:
      v = queue.popleft()
      for i in graph[v]:
        # 인접 리스트를 다 돌면서 queue에 추가
        # 다 돌았으면 popleft를 사용해서 첫번째 원소의 인접리스트를 다시 돈다
        if not visited[i]:
          queue.append(i)
          visited[i] = True
  bfs(visited, 1)
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

## 6. dfs
- [콜라츠 추측](https://school.programmers.co.kr/learn/courses/30/lessons/12943)
- [멀리 뛰기](https://school.programmers.co.kr/learn/courses/30/lessons/12914) 

## 몰라
- [둘만의 암호](https://school.programmers.co.kr/learn/courses/30/lessons/155652#)

## 7. stack
- [햄버거 만들기](https://school.programmers.co.kr/learn/courses/30/lessons/133502)
- [짝지어 제거하기](https://school.programmers.co.kr/learn/courses/30/lessons/12973)

## 8. 시간초과
- [달리기 경주](https://school.programmers.co.kr/learn/courses/30/lessons/178871)

## 9. 투포인터
- [숫자의 표현](https://school.programmers.co.kr/learn/courses/30/lessons/12924)

## 10. 레벨2
- [점프와 순간이동](https://school.programmers.co.kr/learn/courses/30/lessons/12980)
- [예상 대진표](https://school.programmers.co.kr/learn/courses/30/lessons/12985)
- [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885)
- [연속 수열](https://school.programmers.co.kr/learn/courses/30/lessons/131701)
# 라이브러리
## fraction
1. gcd
   
## itertools 
1. combination
   
## string
1. ascii_lowercase

## collections
1. Counter : key별로 개수를 세는 딕셔너리를 만들어야 할 때 바로 만들 수 있다
     ex. 귤 고르기 문제 
