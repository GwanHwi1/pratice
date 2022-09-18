t=int(input())

def rotate(arr):
  length=len(arr)
  rotation=[[0 for _ in range(length)]for _ in range(length)]
  for i in range(length):
    for j in range(length):
      rotation[j][length-i-1]=arr[i][j]
  return rotation

for i in range(1,t+1):
  n=int(input())
  mat=[list(map(int, input().split()))for _ in range(n)]
  result1=rotate(mat) #90도
  result2=rotate(result1) #180도
  result3=rotate(result2) #270도
  print("#"+str(i))
  for j in range(n):
    for k in range(n):
      if k==n-1: print(result1[j][k],end=" ")
      else: print(result1[j][k],end="")
    for k in range(n):  
      if k==n-1: print(result2[j][k],end=" ")
      else: print(result2[j][k],end="")
    for k in range(n):
      if k==n-1: print(result3[j][k],end="\n")
      else: print(result3[j][k],end="")
