n=int(input())
array=list(map(int, input().split()))

d=[1]*n
d[0]=array[0]
for i in range(1,n):
  for j in range(i):
    if array[j]<array[i]:
      d[i]=max(d[i], d[j]+array[i])
    else:
      d[i]=max(d[i], array[i])
    # array[j]는 무관하니까
    # 본인 값을 넣는 것
    # d[i]가 1일 때 제외하고는 d[i]가 항상 더 크지 않나
print(max(d))