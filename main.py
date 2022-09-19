t=int(input())
for i in range(1,t+1):
  n=int(input())
  v=0
  dis=0
  for j in range(n):
    a=list(map(int, input().split()))
    if a[0]==1:
      if a[1]==2: v+=2
      else: v+=1
    elif a[0]==2:
      if a[1]==1: v-=1
      else: v-=2
    if v<0: v=0
    dis+=v
  print("#"+str(i),dis)
