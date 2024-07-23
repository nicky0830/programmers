n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = []
visited = []

def dfs():
    check = 0
    # 얘 때문에 1 1의 1이 각각 다른 수로 취급 된다
    # dfs로 깊이 +1을 했을 때 check 값을 갱신해서
    if len(s) == m:
        print(*s)
    else:
        for i in range(n):
            # 이 for문을 도는 건 여기서 check 값이 갱신 되니까 
            # 같은 수, 다른 index여도 중복 없이 만든다 ex. 1 1 3일 때 1,3이 하나만 만들어짐
            if check != arr[i] and i not in visited:
                # dfs 돌 때마다 (한 열마다) check = 0이어서 같은 수여도 가능
                # arr에 같은 수가 여러 개 있으면
                visited.append(i)
                s.append(arr[i])
                check = arr[i]
                dfs()
                visited.pop()
                s.pop()

dfs()
