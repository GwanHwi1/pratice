t=int(input())
for i in range(1,t+1):
  puzzel=[list(map(int, input().split()))for _ in range(9)]
  result=1
  for j in range(9): #가로 1~9 확인
    arr=set(puzzel[j])
    if len(arr) !=9:
      result=0
      break
  for j in range(9): #세로 1~9 확인
    arr=set()
    for k in range(9):
      arr.add(puzzel[k][j])      
    if len(arr)!=9: 
      result=0
      break
  for j in range(0,9,3): #3*3 1~9 확인
    for k in range(0,9,3):
      arr=set()
      for l in range(3):
        arr.update(puzzel[j+l][k:k+3])
      if len(arr)!=9:
        result=0
        break
  print("#"+str(i),result) 
