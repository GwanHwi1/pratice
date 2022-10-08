from collections import deque

n,m=map(int, input().split())
maze=[list(map(int, input()))for _ in range(n)]
count=[[0 for _ in range(m)]for _ in range(n)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]
q=deque()
q.append((0,0))
maze[0][0]=0
count[0][0]=1
while q:
  x,y=q.popleft()
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx>=0 and nx<n and ny>=0 and ny<m:
      if count[nx][ny]==0 and maze[nx][ny]==1:
        q.append((nx,ny))
        count[nx][ny]=count[x][y]+1
    if nx+1==n and ny+1==m:
      break
print(count[n-1][m-1])


