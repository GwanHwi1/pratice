for t in range(1,11):
  n=int(input())
  a=[list(map(int,input().split()))for _ in range(n)]
  result=0
  b=[[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      b[i][j]=a[j][i]

  for i in range(n):
    tf=0
    cnt=0
    for j in range(n):
      if tf==0 and b[i][j]==1:
        cnt+=1
        tf=b[i][j]
      if b[i][j]==1 and tf==2:
        cnt+=1
        tf=b[i][j]
      if b[i][j]==2 and tf==1:
        cnt+=1
        tf=b[i][j]
    result+=cnt//2
  print(f"#{t} {result}")