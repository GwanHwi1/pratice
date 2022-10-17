def RightCrossPlus(x,y):
  global right
  if x==100: return
  right+=arr[x][y]
  RightCrossPlus(x+1,y+1)

def LeftCrossPlus(x,y):
  global left
  if x==100: return
  left+=arr[x][y]
  LeftCrossPlus(x+1,y-1)

for t in range(1,11):
  n=int(input())
  arr=[list(map(int,input().split()))for _ in range(100)]
  right=0
  left=0
  result=0
  total=0
  RightCrossPlus(0,0)
  LeftCrossPlus(0,99)
  for i in range(100): #행
    if result<sum(arr[i]): result=sum(arr[i])
  for i in range(100): #열
    for j in range(100):
      total+=arr[j][i]
    if result<total: result=total
    total=0
  result=max(left,right,result)
  print(f"#{n} {result}")

