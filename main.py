def dfs(position,a):
  global result
  tf=True
  for i in lst[position]:
    if not visited[i]:
      tf=False
      break
  if tf:
    result=max(result,a)
    return
  for i in lst[position]:
    if not visited[i]:
      visited[i]=True
      dfs(i,a+1)
      visited[i]=False

test_case=int(input())
for t in range(1,test_case+1):
  n,m=map(int, input().split())
  lst=[[] for _ in range(n+1)]
  for i in range(1,n+1):
    lst[0].append(i)
  visited=[False]*(n+1)
  result=0
  for _ in range(m):
    x,y=map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)
  # print(lst)
  dfs(0,0)
  print(f"#{t} {result}")