m,n= map(int, input().split())
chess=[list(map(str,input()))for _ in range(m)]
dx=[-1,0]
dy=[0,-1]
result=64

def color(arr):
  tf=False
  cnt=0
  for i in range(8):
    for j in range(8):
      for k in range(2):
        nx=i+dx[k]
        ny=j+dy[k]
        if nx>=0 and nx<=7 and ny>=0 and ny<=7:
          if arr[i][j]==arr[nx][ny]: 
            tf=True
      if tf==True:
        if arr[i][j]=="W": arr[i][j]="B"
        elif arr[i][j]=="B": arr[i][j]="W"
        tf=False
        cnt+=1
  if cnt>32: cnt=64-cnt
  return cnt

for i in range(m-7):
  for j in range(n-7):
    lst=[]
    for k in range(8):
      lst.append(chess[i+k][j:j+8])
    result=min(result,color(lst))
print(result)