test_case=int(input())
for t in range(1,test_case+1):
  n=int(input())
  farm=[list(map(int,input()))for _ in range(n)]
  result=0
  half=n//2
  a=n//2+1
  for i in range(n):
    if i<=half: a-=1
    else: a+=1
    for j in range(a,n-a):
      result+=farm[i][j]
  print(f"#{t} {result}")


