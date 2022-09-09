n, m = map(int,input().split())
dx,dy,direction = map(int,input().split())
arr = [list(map(int,input().split())) for row in range(n)]
count=0

def dir(direction, dx, dy):
  x=[0,1,0,-1]
  y=[1,0,-1,0]
  global count
  count+=1
  arr[dx][dy]+=1
  for i in range (4):
    if dx+x[direction]>m-1 or dy+y[direction]>n-1 or dx+x[direction]<0 or dy+y[direction]<0: direction-=1
    if direction==-1: direction=3
    if arr[dx+x[direction]][dy+y[direction]]==1 : direction-=1
    if direction==-1: direction=3
  if dx+x[direction]>m-1 or dy+y[direction]>n-1 or dx+x[direction]<0 or dy+y[direction]<0: return count
  if arr[dx+x[direction]][dy+y[direction]] != 0: return count
  else: 
    dx+=x[direction]
    dy+=y[direction]
    return dir(direction, dx, dy)

print(dir(direction, dx, dy))