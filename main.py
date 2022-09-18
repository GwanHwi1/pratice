t=int(input())
for i in range(1,t+1):
  n,m=map(int,input().split())
  a=list(map(int, input().split()))
  b=list(map(int, input().split()))
  result=0
  if n==m:
    for j in range(n):
      result+=a[j]*b[j]
  elif n>m:
    for j in range(n-m+1):
      total=0
      for k in range(m):
        total+=a[j+k]*b[k]
      result=max(result,total)
  else:
    for j in range(m-n+1):
      total=0
      for k in range(n):
        total+=a[k]*b[j+k]
      result=max(result,total)
  print("#"+str(i),result)
