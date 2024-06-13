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

## 3. heap
파이썬 heapq 모듈
K번째 원소가 항상 자식 원소들(2k, 2k+1)보다 작거나 같은 최소 힙의 형태로 정렬된다
내장 모듈의 별도 설치 작업 없이 바로 사용 가능

```python
- heapq.heqppush(heap, item) : item을 heap에 추가
- heapq.heappop(heap): heap에서 가장 작은 원소를 pop & 리턴. 비어 있는 경우 indexError
- heapq.heapify(X): 리스트 X를 즉각적으로 heap으로 변환함 (O(N))
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
- [괄호 회전하기](https://school.programmers.co.kr/learn/courses/30/lessons/76502)

## 8. 시간초과
- [달리기 경주](https://school.programmers.co.kr/learn/courses/30/lessons/178871)

## 9. 투포인터
- [숫자의 표현](https://school.programmers.co.kr/learn/courses/30/lessons/12924)

## 10. 레벨2
- [점프와 순간이동](https://school.programmers.co.kr/learn/courses/30/lessons/12980)
- [예상 대진표](https://school.programmers.co.kr/learn/courses/30/lessons/12985)
- [구명보트](https://school.programmers.co.kr/learn/courses/30/lessons/42885)
- [연속 수열](https://school.programmers.co.kr/learn/courses/30/lessons/131701)

## 11. 튜플
- [튜플](https://school.programmers.co.kr/learn/courses/30/lessons/64065)

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

## python
- [1,2,3,4] == [1,2,3,4] : True
- [1,2,3,4] == [4,3,2,1] : False
- dictionary 비교 가능: {a:1, b:2} == {a:1, b:2}
  ex. 할인행사 문제

## 시간복잡도
- len(n) : O(1)
- max(...): O(n) //max의 인수가 몇 개가 되든
- 배열.index(n): O(n) 

## bracket notation
- [start : end : step]
- step이 음수면 뒤집어서
  (step이 음수여도 start, end는 원래 배열의 index 기준으로 함.)
  (만약 뒤집은 기준으로 배열의 index를 사용하고 싶으면 한번 뒤집고 아예 다른 bracket으로 잡기)

## 그리디
- [보물](https://www.acmicpc.net/problem/1026)
- [ATM](https://www.acmicpc.net/problem/11399)
- [거스름돈](https://www.acmicpc.net/problem/5585)
- [동전 0](https://www.acmicpc.net/problem/11047)
- [로프](https://www.acmicpc.net/problem/2217)
- [수들의 합](https://www.acmicpc.net/problem/1789)
- [주유소](https://www.acmicpc.net/problem/13305)
- [전자레인지](https://www.acmicpc.net/problem/10162)
- [카드 정렬](https://www.acmicpc.net/problem/1715)

백준 10816, 백준 1439, 백준 10799, 백준 1992, 백준 9012, 백준 2447, 백준 10101, 백준 14503, 백준 3040, 백준 11403, 백준 11651, 백준 1789, 백준 15649, 백준 15650, 백준 11497, 프로그래머스 42895, 백준 9663, 백준 2630, 백준 1446, 백준 1094, 백준 4307, 백준 4485, 백준 1520, 백준 9084, 백준 11758, 백준 1991, 백준 17779, 백준 11053, 백준 13869, 백준 9251, 백준 1766, 백준 11725, 백준 10845, 백준 1004, 백준 4256, 백준 11724, 백준 1337, 백준 7490, 백준 2022, 백준 1340, 백준 17140, 백준 1389, 백준 1158, 백준 1316, 백준 10815, 백준 17266, 백준 7795, 백준 11054, 백준 8958, 백준 7576, 백준 1912, 백준 9020, 백준 16236, 백준 1167, 백준 2437, 백준 15686, 백준 9095, 백준 1194, 백준 25644, 백준 2170, 백준 1922, 백준 17070, 백준 1525, 백준 18352, 백준 1918, 백준 14725, 백준 7569, 백준 2887, 백준 12015, 백준 1007, 백준 1197, 백준 10942, 백준 1509, 백준 1194, 백준 1562, 백준 1799
