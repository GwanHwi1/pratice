def dfs(goal,x):
  global cnt
  if goal==k:
    cnt+=1
    return
  elif goal>k: return
  for i in range(x,n):
    dfs(goal+a[i],i+1)
    
test_case=int(input())
for t in range(1,test_case+1):
  n,k=map(int,input().split())
  a=list(map(int,input().split()))
  cnt=0
  dfs(0,0)
  print(f"#{t} {cnt}")