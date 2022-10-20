test_case=int(input())
for t in range(1,test_case+1):
  n,m=map(int,input().split())
  for _ in range(n):
    a=list(map(int,input()))
    if 1 in a: arr=a
  for i in range(len(arr)-1,-1,-1):
    if arr[i]==1:
      arr=arr[i-55:i+1]
      break
  decode=[[0,0,0,1,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,0,1,1],[0,1,1,1,1,0,1],[0,1,0,0,0,1,1],
          [0,1,1,0,0,0,1],[0,1,0,1,1,1,1],[0,1,1,1,0,1,1],[0,1,1,0,1,1,1],[0,0,0,1,0,1,1]]
  even=[]
  odd=[]
  for i in range(0,63,7):
    a=arr[i:i+7]
    for j in range(len(decode)):
      if a==decode[j] and ((i+7)//7)%2==1: odd.append(j)
      elif a==decode[j] and ((i+7)//7)%2==0: even.append(j)
  result=(sum(odd)*3)+sum(even)
  if result%10==0: print(f"#{t} {sum(even)+sum(odd)}")
  else: print(f"#{t}",0)