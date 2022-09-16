t=int(input())
for i in range(1,t+1):
  n,m=map(int, input().split())
  arr=[list(map(int,input().split()))for _ in range(n)]
  maxValue=0
  total=0
  for j in range(n-m+1):#세로
    for k in range(n-m+1):#가로
      for l in range(m):
        total+=sum(arr[j+l][k:k+m])
      maxValue=max(maxValue,total)
      total=0
  print("#"+str(i),maxValue)