def dfs(x,y,now):
  global result
  if y>l: return
  result=max(result,x)
  for i in range(now,len(arr)):
    dfs(x+arr[i][0],y+arr[i][1],i+1)

test_case=int(input())
for t in range(1,test_case+1):
  n,l=map(int,input().split())  
  arr=[list(map(int,input().split())) for _ in range(n)]
  result=0
  dfs(0,0,0)
  print(f"#{t} {result}")
