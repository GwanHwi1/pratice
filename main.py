t=int(input())
for i in range(1,t+1):
  n,k=map(int, input().split())
  puzzel=[list(map(int,input().split()))for _ in range(n)]
  result=0
  for j in range(n):
    count=1
    for l in range(n):
      if l==n-1:
        if count==k: result+=1 
      else:
        if puzzel[j][l]==puzzel[j][l+1]==1: count+=1
        else: 
          if count==k: 
            result+=1
            count=1
          else: count=1
  for j in range(n):
    count=1
    for l in range(n):
      if l==n-1:
        if count==k: result+=1 
      else:
        if puzzel[l][j]==puzzel[l+1][j]==1: count+=1
        else: 
          if count==k: 
            result+=1
            count=1
          else: count=1
  print("#"+str(i),result)