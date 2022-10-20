def search(nowX,nowY):
  if nowX<=0 or nowX>n or nowY<=0 or nowY>n: return
  if othello[nowX][nowY]==0: return
  if othello[nowX][nowY]==c: 
    arr[0]=nowX
    arr[1]=nowY
    return
  search(nowX+x,nowY+y)

def color(nowx,nowy):
  if nowx==arr[0] and nowy==arr[1]: return
  othello[nowx][nowy]=c
  color(nowx+x,nowy+y)

test_case=int(input())
for t in range(1,test_case+1):
  n,m=map(int,input().split())
  othello=[[0 for _ in range(n+1)]for _ in range(n+1)]
  othello[n//2][n//2]=2
  othello[n//2][n//2+1]=1
  othello[n//2+1][n//2]=1
  othello[n//2+1][n//2+1]=2
  dx=[-1,1,0,0,-1,1,-1,1]
  dy=[0,0,-1,1,-1,-1,1,1]
  for _ in range(m):
    a,b,c=map(int,input().split())
    othello[a][b]=c
    for i in range(8):
      nx=a+dx[i]
      ny=b+dy[i]
      x=dx[i]
      y=dy[i]
      arr=[0,0]
      if nx>0 and nx<=n and ny>0 and ny<=n and othello[nx][ny]!=c: 
        search(nx,ny)
        # print(arr)
      if 0 not in arr: color(a,b)
    # for i in range(len(othello)):
    #   print(othello[i])
  cntW=0
  cntB=0
  for i in range(len(othello)):
    for j in range(len(othello)):
      if othello[i][j]==1: cntB+=1
      elif othello[i][j]==2: cntW+=1
  print(f"#{t} {cntB} {cntW}")
 
        

