t=int(input())
for i in range(1,t+1):
  n=int(input())
  arr=[[0 for _ in range(n)]for _ in range(n)]
  a=b=0
  way=1
  while(way<=n**2):
    while(b<n): #오른쪽으로 이동
      if arr[a][b]!=0: break
      else: 
        arr[a][b]=way
        way+=1
        b+=1
    b-=1
    a+=1
    while(a<n): #아래로 이동
      if arr[a][b]!=0: break
      else: 
        arr[a][b]=way
        way+=1
        a+=1
    a-=1
    b-=1
    while(b>=0): #왼쪽으로 이동
      if arr[a][b]!=0: break
      else:
        arr[a][b]=way
        way+=1
        b-=1
    b+=1
    a-=1
    while(a>=0): #위로 이동
      if arr[a][b]!=0: break
      else:
        arr[a][b]=way
        way+=1
        a-=1
    a+=1
    b+=1
  print("#"+str(i))
  for j in range(n):
    print(*arr[j])
